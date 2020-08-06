from telegram.ext import *
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import *
from random import choice
from fonctions import *

def salle(update, context):
    #demande ce que le joueur veut faire
    user_id = update.effective_user.id
    position = context.bot_data["users"][user_id]["salle"]

    update.message.reply_text(endroit(position), reply_markup=ReplyKeyboardRemove())
    keyboard = [[KeyboardButton(action)] for action in ["Voir la salle", "Répondre à l'énigme", "Se déplacer"]]
    update.message.reply_text(debut_salle, reply_markup=ReplyKeyboardMarkup(keyboard))
    return ACTION

def endroit(position):
    return "Tu es dans {}".format(lieux_description[position][0])

def action(update, context):
    #reçoit l'action que le joueur veut faire et redirige vers la bonne fonction
    user_id = update.effective_user.id
    user_input = update.message.text[:30].strip().replace("\n", " ")

    if user_input not in ["Voir la salle", "Répondre à l'énigme", "Se déplacer"]:
        update.message.reply_text(invalid_input)
        return ACTION
    update.message.reply_text("T'es chaud on le fait ?\nT'as pas le choix de toute façon.", reply_markup=ReplyKeyboardRemove())
    if user_input == "Voir la salle":
        return PHOTO
    elif user_input == "Répondre à l'énigme":
        return ENIGME
    else:
        return DEPLACEMENT

def photo(update, context):
    #envoie la photo de la salle
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    position = context.bot_data["users"][user_id]["salle"]

    context.bot.send_photo(chat_id, lieux_description[position][2])
    update.message.reply_text(piece + lieux_description[position][0], reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def enigme(update, context):
    #envoie l'énigme
    user_id = update.effective_user.id
    position = context.bot_data["users"][user_id]["salle"]

    update.message.reply_text(debut_enigme, reply_markup=ReplyKeyboardRemove())
    update.message.reply_text(enigmes[position]["question"])
    update.message.reply_text(hide_answer(enigmes[position]["reponse"]))

    return TENTATIVE

def tentatives(update, context):
    #reçoit la tentative et répond si c'est bon ou non
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    position = context.bot_data["users"][user_id]["salle"]
    user_input = update.message.text[:30].strip().replace("\n", " ").lower()

    if user_input == "fin":
        update.message.reply_text(a_plus)
        return ConversationHandler.END
    elif remove_accents(user_input) == remove_accents(enigmes[position]["reponse"].lower()):
        update.message.reply_text(choice(well_dones) + indice)
        context.bot.send_photo(chat_id, lieux_description[position][3])
        return ConversationHandler.END
    else:
        update.message.reply_text(choice(try_agains) + encore)
        return TENTATIVE

def deplacement(update, context):
    #demande où il veut aller
    user_id = update.effective_user.id
    position = context.bot_data["users"][user_id]["salle"]

    keyboard = [[KeyboardButton(lieux[action])] for action in lieux_description[position][1]]
    update.message.reply_text(ou_aller, reply_markup=ReplyKeyboardMarkup(keyboard))
    return NEXT_PLACE

def next_place(update, context):
    #change de salle
    user_id = update.effective_user.id
    user_input = update.message.text[:30].strip().replace("\n", " ")

    if user_input not in lieux:
        update.message.reply_text(invalid_input)
        return NEXT_PLACE

    context.bot_data["users"][user_id]["salle"] = lieux.index(user_input)
    update.message.reply_text(direction + user_input + arrivee, reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END
