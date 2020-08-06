from data import *
from copy import deepcopy
from datetime import date
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import *
import time

def user_id_str(user_data):
    #affichage
    try :
        return "{} {} ({}) {} ".format(user_data["prenom"],
                                       user_data["nom"],
                                       user_data["pseudo"],
                                       user_data["promo"])
    except :
        return user_data["nom"]

def start(update, context):
    #initialise l'enregistrement de l'utilisateur
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    if "users" in context.bot_data:
        if user_id not in context.bot_data["users"]:
            # logger.info("[/start] New user registering")
            context.bot_data["users"][user_id] = deepcopy(empty_user)
        else :
            context.bot.send_message(chat_id=chat_id, text=already_started)
            return ConversationHandler.END
    else:
        # logger.info("[/start] First user registered")
        context.bot_data["users"] = {user_id: deepcopy(empty_user)}
        context.bot_data["date"] = date.today().day
        context.bot_data["registration_open"] = True

    context.bot.send_message(chat_id=chat_id, text=intro)
    context.bot_data["users"][user_id]["nom"] = update.effective_user.name

    return update_id(update, context, first_time=True)

def update_id(update, context, first_time=False):
    #demande prénom
    update.message.reply_text(ask_data + ("\n"+inform_cancel if not first_time else ""), reply_markup=ReplyKeyboardRemove())
    update.message.reply_text(ask[PRENOM])
    return PRENOM

def prenom(update, context):
    #reçoit le prénom et demande le nom
    user_id = update.effective_user.id
    user_input = update.message.text[:30].strip().replace("\n", " ")

    if user_input == "":
        update.message.reply_text(invalid_input)
        return PRENOM

    context.bot_data["users"][user_id]["prenom"] = user_input
    update.message.reply_text(ask[NOM])
    return NOM

def nom(update, context):
    #reçoit le nom et demande la promo
    user_id = update.effective_user.id
    user_input = update.message.text[:30].strip().replace("\n", " ")

    if user_input == "":
        update.message.reply_text(invalid_input)
        return NOM

    context.bot_data["users"][user_id]["nom"] = user_input
    keyboard = [[KeyboardButton(prom)] for prom in promos]
    update.message.reply_text(ask[PROMO], reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
    return PROMO

def promo(update, context):
    #reçoit promo et demande pseudo
    user_id = update.effective_user.id
    user_input = update.message.text[:30].strip().replace("\n", " ")

    if user_input not in promos:
        update.message.reply_text(invalid_input)
        return PROMO
    context.bot_data["users"][user_id]["promo"] = user_input
    update.message.reply_text(ask[PSEUDO], reply_markup=ReplyKeyboardRemove())
    return PSEUDO

def pseudo(update, context):
    #reçoit le pseudo et finit la conversation
    user_id = update.effective_user.id
    user_input = update.message.text[:30].strip().replace("\n", " ")

    for userid in context.bot_data["users"]:
        if user_input == context.bot_data["users"][userid]["pseudo"] and not userid == user_id:
            update.message.reply_text(invalid_input + " (ce pseudo est déjà utilisé)")
            return PSEUDO

    if user_input == "":
        update.message.reply_text(invalid_input)
        return PSEUDO

    context.bot_data["users"][user_id]["pseudo"] = user_input
    update.message.reply_text(ask[END])

    user_str = user_id_str(context.bot_data["users"][user_id])
    update.message.reply_text(recap_data + "\n" + user_str + "\n" + incorrect_data)
    update.message.reply_text(finish_start)
    context.bot_data["users"][user_id]["registration_time"] = time.time()
    print(context.bot_data["users"][user_id]["prenom"] + " s'est inscrit.")
    context.bot.send_message(chat_id=id_BDAmour, text=context.bot_data["users"][user_id]["prenom"] + " s'est inscrit.")
    # logger.info("[/start] User {} updated its data : {}".format(user_id, user_str))
    # logger.info("[/start] Current users :\n" + pformat(context.bot_data["users"]))
    return ConversationHandler.END
