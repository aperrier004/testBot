from telegram.ext import *
from telegram import ReplyKeyboardRemove
from data import *
from random import choice
from fonctions import *

def secrets(update, context):
    #demande le mot de passe à l'utilisateur
    user_id = update.effective_user.id

    update.message.reply_text(chambre_secrets, reply_markup=ReplyKeyboardRemove())
    return INTREPIDES

def intrepides(update, context):
    #vérifie le mdp
    user_id = update.effective_user.id
    user_input = update.message.text[:30].strip().replace("\n", " ").lower()

    if remove_accents(user_input) == remove_accents(MDP.lower()):
        update.message.reply_text(penetration)
        context.bot_data["users"][user_id]["salle"] = 5
        return ConversationHandler.END
    else:
        update.message.reply_text(echec)
        return ConversationHandler.END
