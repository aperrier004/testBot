import unicodedata
import time

def photoecho(update, context):
    """Displays infos about a received photo in the console, no user feedback"""

    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    print(chat_id)
    print("[photoecho] user {} sent a picture, which characteristics are :".format(user_id))
    fsiz = 0
    for photosiz in update.message.effective_attachment:
        print("file size : " + str(photosiz.file_size))
        print("file id : " + photosiz.file_id)
        if photosiz.file_size>fsiz:
            fid = photosiz.file_id
            fsiz = photosiz.file_size

def hide_answer(string):
    """Returns a hint-string for string"""

    hidden = "("
    count = 0
    for i in string:
        if i in [" ", "-", "'", "’"]:
            hidden += i
        else:
            hidden += '–'
            count += 1
    hidden += " : {} lettres)".format(count)
    return hidden

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def test(update, context):
    user_input = update.message.text[:30].strip().replace("\n", " ")
    print(user_input)

def user_recap(user_data) :
    #affichage recap
    try :
        return "{} {} ({})\n{}\n{} proposistion(s)\nTrouve {}\nEn {} secondes".format(user_data["prenom"],
                                         user_data["nom"],
                                         user_data["pseudo"],
                                         user_data["promo"],
                                         len(user_data["essais"]),
                                         time.strftime("%A %d %B %Y %H:%M:%S", time.localtime(user_data["end_time"])),
                                         user_data["end_time"] - user_data["registration_time"])
    except :
        return user_data["temps"]

def recup(update, context) :
    #récupère l'id du groupe
    chat_id = update.effective_chat.id
    print(chat_id)
    return ConversationHandler.END
