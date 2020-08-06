from telegram.ext import *
from telegram import ReplyKeyboardRemove
from data import *

def help(update, context):
    #envoie une photo où il y a les explications
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    update.message.reply_text(aide, reply_markup=ReplyKeyboardRemove())
    context.bot.send_photo(chat_id, aide_photo)
    return ConversationHandler.END

def map(update, context):
    #envoie une photo de la map
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    update.message.reply_text(carte, reply_markup=ReplyKeyboardRemove())
    context.bot.send_photo(chat_id, carte_photo)
    return ConversationHandler.END

def suspects(update, context):
    #envoie une photo avec la liste des suspects
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    update.message.reply_text(suspect, reply_markup=ReplyKeyboardRemove())
    context.bot.send_photo(chat_id, suspects_photo)
    return ConversationHandler.END
