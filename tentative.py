from telegram.ext import *
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import *
from fonctions import *
import time

def user_prop(user_data):
    #affichage
    return "{} avec {} dans {} ".format(user_data["meurtrier"],
                                   user_data["arme"],
                                   user_data["lieu"])

def proposer(update, context):
    #débute la proposition en demandant le meurtrier
    user_id = update.effective_user.id

    update.message.reply_text(debut_proposition, reply_markup=ReplyKeyboardRemove())

    keyboard = [[KeyboardButton(prop)] for prop in perso]
    update.message.reply_text(proposition[MEURTRIER], reply_markup=ReplyKeyboardMarkup(keyboard))
    return MEURTRIER

def meurtrier(update, context):
    #reçoit le meurtrier et demande l'arme
    user_id = update.effective_user.id
    user_input = update.message.text[:30].strip().replace("\n", " ")

    if user_input not in perso:
        update.message.reply_text(invalid_input)
        return MEURTRIER

    context.user_data["meurtrier"] = user_input

    keyboard = [[KeyboardButton(prop)] for prop in armes]
    update.message.reply_text(proposition[ARME], reply_markup=ReplyKeyboardMarkup(keyboard))
    return ARME

def arme(update, context):
    #reçoit l'arme et demande le lieu
    user_id = update.effective_user.id
    user_input = update.message.text[:30].strip().replace("\n", " ")

    if user_input not in armes:
        update.message.reply_text(invalid_input)
        return ARME

    context.user_data["arme"] = user_input

    keyboard = [[KeyboardButton(prop)] for prop in lieux]
    update.message.reply_text(proposition[LIEU], reply_markup=ReplyKeyboardMarkup(keyboard))
    return LIEU

def lieu(update, context):
    #reçoit le lieu et vérifie si la proposition a déjà était faite et est juste
    user_id = update.effective_user.id
    user_input = update.message.text[:30].strip().replace("\n", " ")

    if user_input not in lieux:
        update.message.reply_text(invalid_input)
        return LIEU

    context.user_data["lieu"] = user_input
    prop = [context.user_data["meurtrier"], context.user_data["arme"], context.user_data["lieu"]]
    update.message.reply_text(recap_data + "\n" + user_prop(context.user_data), reply_markup=ReplyKeyboardRemove())

    if prop in context.bot_data["users"][user_id]["essais"]:
        update.message.reply_text(deja_prop)
    else:
        context.bot_data["users"][user_id]["essais"] += [prop]
        if prop == solution:
            context.bot_data["users"][user_id]["end_time"] = time.time()
            update.message.reply_text(bravo)
            print(context.bot_data["users"][user_id]["prenom"] + " a trouvé !")
            print(user_recap(context.bot_data["users"][user_id]) + "\n")
            context.bot.send_message(chat_id=id_BDAmour, text=context.bot_data["users"][user_id]["prenom"] + " a trouvé !\n" + user_recap(context.bot_data["users"][user_id]))
        else:
            update.message.reply_text(dommage)
    return ConversationHandler.END
