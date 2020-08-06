import telegram
from telegram.ext import messagequeue as mq
from telegram.utils.request import Request

from enregistrement import *
from tentative import *
from salles import *
from possibilites import *
from chambre import *
from fonctions import *

persistence = PicklePersistence(filename='bot_data_pickle')

# Slightly modify the Bot class to use a MessageQueue in order to avoid
# Telegram's flood limits (30 msg/sec)
class MQBot(telegram.bot.Bot):
    """A subclass of Bot which delegates send method handling to MessageQueue"""
    def __init__(self, *args, is_queued_def=True, mqueue=None, **kwargs):
        super(MQBot, self).__init__(*args, **kwargs)
        self._is_messages_queued_default = is_queued_def
        self._msg_queue = mqueue or mq.MessageQueue()
    def __del__(self):
        try:
            self._msg_queue.stop()
        except:
            pass
    @mq.queuedmessage
    def send_message(self, *args, **kwargs):
        """Wrapped method would accept new `queued` and `isgroup` OPTIONAL arguments"""
        return super(MQBot, self).send_message(*args, **kwargs)


# Limit global throughput to 25 messages per second
q = mq.MessageQueue(all_burst_limit=25, all_time_limit_ms=1000)
# Set connection pool size for bot
request = Request(con_pool_size=8)

def readToken():
    tokfile = open('BOT_TOKEN', 'r')
    token = tokfile.read()[:-1]
    tokfile.close()
    return token

token = readToken()

tgbot = MQBot(token, request=request, mqueue=q)

persistence = PicklePersistence(filename='bot_data_pickle')

updater = telegram.ext.updater.Updater(bot=tgbot, persistence=persistence, use_context=True)
dispatcher = updater.dispatcher

def cancel(update, context):
    update.message.reply_text(success_cancel, reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

cancel_handler = CommandHandler("cancel", cancel)

start_handler = ConversationHandler(
    entry_points = [CommandHandler("start", start),
                    CommandHandler("start_again", update_id)],
    states = {PRENOM: [cancel_handler, MessageHandler(Filters.text, prenom)],
              NOM: [cancel_handler, MessageHandler(Filters.text, nom)],
              PROMO: [cancel_handler, MessageHandler(Filters.text, promo)],
              PSEUDO: [cancel_handler, MessageHandler(Filters.text, pseudo)]},
    fallbacks = [cancel_handler],
    name = "start_handler",
    persistent = True)

dispatcher.add_handler(start_handler)

proposition_handler = ConversationHandler(
    entry_points = [CommandHandler("proposer", proposer)],
    states = {MEURTRIER: [cancel_handler, MessageHandler(Filters.text, meurtrier)],
              ARME: [cancel_handler, MessageHandler(Filters.text, arme)],
              LIEU: [cancel_handler, MessageHandler(Filters.text, lieu)]},
    fallbacks = [cancel_handler],
    name = "proposition_handler",
    persistent = True)

dispatcher.add_handler(proposition_handler)

salle_handler = ConversationHandler(
    entry_points = [CommandHandler("salle", salle)],
    states = {ACTION: [cancel_handler, MessageHandler(Filters.text, action)],
              PHOTO: [cancel_handler, MessageHandler(Filters.text, photo)],
              ENIGME: [cancel_handler, MessageHandler(Filters.text, enigme)],
              TENTATIVE: [cancel_handler, MessageHandler(Filters.text, tentatives)],
              DEPLACEMENT: [cancel_handler, MessageHandler(Filters.text, deplacement)],
              NEXT_PLACE: [cancel_handler, MessageHandler(Filters.text, next_place)]},
    fallbacks = [cancel_handler],
    name = "salle_handler",
    persistent = True)

dispatcher.add_handler(salle_handler)

secrets_handler = ConversationHandler(
    entry_points = [CommandHandler("secrets", secrets)],
    states = {INTREPIDES: [cancel_handler, MessageHandler(Filters.text, intrepides)]},
    fallbacks = [cancel_handler],
    name = "secrets_handler",
    persistent = True)

dispatcher.add_handler(secrets_handler)

dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler("map", map))
dispatcher.add_handler(CommandHandler("suspects", suspects))

dispatcher.add_handler(MessageHandler(Filters.photo, photoecho))
dispatcher.add_handler(MessageHandler(Filters.text, test))

print("Bonjour")

updater.start_polling()
updater.idle()
