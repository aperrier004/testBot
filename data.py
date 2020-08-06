intro = "Bienvenue sur le Cluedo de l'ENSC ! 🤩\nIl te faut trouver qui a tué Joseph, où, et de quelle manière. Pour cela tu pourras naviguer dans les différentes pièces à la recherche d'indices. 🔍"
already_started = "Tu es déjà inscrit ! Tu peux d'hors et déjà partir à la recherche du coupable !"
ask_data = "Avant de commencer, nous allons te demander quelques informations pour mieux te connaître. 🤓\nMerci de répondre sérieusement pour que nous puissions t'identifier ! Ce serait dommage de gagner mais de ne pas pouvoir récupérer sa récompense. 🙄\nAttention, je ne retiens pas plus de 30 caractères."
inform_cancel = "Tu peux annuler à tout moment avec la commande /cancel"
invalid_input = "Je n'ai pas compris, essaie encore."
recap_data = "On récapitule :"
incorrect_data = "Tu peux recommencer avec la commande /start_again s'il y a une erreur."
finish_start = "Tu connais peut-être déjà le principe du Cluedo, mais je réexplique rapidement.\nIl y a 5 suspects, ainsi que 5 armes et pièces possibles (retrouve la liste avec la commande /suspects). Il te faudra procéder par élimination en fonction des indices que tu trouveras dans les différentes salles. Dans chaque salle, tu pourras répondre à une énigme pour obtenir un indice, examiner la pièce pour essayer de trouver un indice, ou te déplacer dans une autre pièce adjacente.\nPour commencer je t'invite à lancer la commande /help pour découvrir la liste de toutes les commandes, et un rappel du fonctionnement."
success_cancel = "Ok on s'arrête là. 😢"
debut_proposition = "Tu t'apprêtes à accuser quelqu'un, j'espère que tu es sûr de toi ! 😲"
deja_prop = "Tu as déjà fais cette proposition, on est gentil on te la compte pas. 😊"
bravo = "Bravo tu as trouvé le meurtrier ! Grâce à toi la mort de Joseph sera vengée. 🎉\nOn espère que cette activité t'as plu, et on hâte de te retrouver à tous les autres évènements organisés par l'école !"
dommage = "Oula malheureux ! N'essaie pas d'accuser un innocent tu pourrais avoir des problèmes ! 🚓"
debut_salle = "Que veux-tu faire ici ?"
ou_aller = "Où veux-tu aller maintenant ?"
direction = "Tu te diriges vers "
arrivee = ". Et tu y arrives ! 🏁"
piece = "Voilà "
debut_enigme = "Voici l'énigme !"
encore = "\nUne autre idée ?"
a_plus = "Une autre fois peut-être."
indice = " Voici ton indice."
aide = "Voici le rappel."
carte = "Voici l'organisation des salles."
chambre_secrets = "Ah tu veux entrer dans la chambre des secrets ? Nous n'allons pas te simplifier la tâche.\nEn connais tu le mot de passe ? 🗝️"
penetration = "Hmm, je vous que tu n'es pas un moldu comme les autres... Tu gagnes le droit de penérer dans la Chambre des Secrets ! 🚽"
echec = "C'est bien ce que je pensais, tu n'es qu'un simple moldu... Passes ton chemin. 👉"
suspect = "Voici la liste des suspects."

PRENOM, NOM, PROMO, PSEUDO, END = range(5)

ask = [ "C'est quoi ton prénom ?",
        "Quel est ton nom de famille ?",
        "En quelle année es-tu ?",
        "Quel pseudo veux-tu utiliser ?",
        "Merci ! Je note tout ça dans mon Death Note. 😏"]

promos = [ "1A",
          "2A",
          "3A"]
empty_user = {"nom": "",
              "prenom": "",
              "pseudo": "",
              "promo": "",
              "salle": 0,
              "essais": []}

LIEU1, LIEU2, LIEU3, LIEU4, LIEU5 = range(5)

image1 = "AgACAgQAAxkBAAN8XvdvF7OhrJXwDb5vAAHZ5Eq_zufeAAIstDEbNSC4U0SHNmyRcrnuesVOJF0AAwEAAwIAA3kAA6JgAQABGgQ"
image2 = "AgACAgQAAxkBAAN7Xvdu_wniMubLC2XMxGVjaXiKo14AAiu0MRs1ILhTd6QlPmrdSkhw52EiXQADAQADAgADeQADBA4EAAEaBA"
image3 = "AgACAgQAAxkBAAN6Xvdu39p_7RMD3lYOpvIsBQVcRKsAAiq0MRs1ILhTjx14OyowA9CoPU0kXQADAQADAgADeQADKVsBAAEaBA"
image4 = "AgACAgQAAxkBAAN5XvduxKRqS7P6vFO_CDVnDuF9beYAAim0MRs1ILhTUtIBSahb2ZFGuH0jXQADAQADAgADeQADpAoDAAEaBA"
image5 = "AgACAgQAAxkBAAN4XvduqBtG65N5mamL_JZHj6BiVfsAAii0MRs1ILhT0ykFir6of_6IB_wiXQADAQADAgADeQADyI4DAAEaBA"
image6 = "AgACAgQAAxkBAAN3Xvdujc_qmRj8as1cBsNMrtyGm0kAAie0MRs1ILhTMksPDiX3Jlc9_T0kXQADAQADAgADeQADCDQCAAEaBA"
indice1 = "AgACAgQAAxkBAAN1XvduSJpHJ-Om4ZKhLZBd31pMfXMAAiS0MRs1ILhTU1iGHiSx8Ee8W9QiXQADAQADAgADeQADt5cDAAEaBA"
indice2 = "AgACAgQAAxkBAAN0XvduLzukZzY9-enVdRE9Xu3xOLAAAiO0MRs1ILhTidw9nkxE430mPs4iXQADAQADAgADeQAD9ZUDAAEaBA"
indice3 = "AgACAgQAAxkBAANzXvduEBOygi7efFaaHEn8KSaQ91EAAiK0MRs1ILhTLAxtUyO-fCiVgPoiXQADAQADAgADeQADN5ADAAEaBA"
indice4 = "AgACAgQAAxkBAANyXvdt9Qq-4JWf5nWcVFbqiOd7zqwAAiG0MRs1ILhTRwjhpDzwoCvLp-YiXQADAQADAgADeQADv5gDAAEaBA"
indice5 = "AgACAgQAAxkBAANxXvdt12OyuJ1VEE2CmaTBDRuh3bIAAiC0MRs1ILhTDBhdkUeAjC6QZtciXQADAQADAgADeQADkJcDAAEaBA"
indice6 = "AgACAgQAAxkBAANwXvdtvlmpmpLe4UgeEaul1f7FwP0AAh-0MRs1ILhT1HUdFI7zaB7A8bcbAAQBAAMCAAN5AAPGQAgAARoE"

aide_photo = "AgACAgQAAxkBAAN2XvdudKDYZthnmuEtTvvNydnTnScAAiW0MRs1ILhTYGo8kfYVcEYNknQjXQADAQADAgADeQAD11wBAAEaBA"
carte_photo = "AgACAgQAAxkBAANvXvdtowO10F1mXYRtNwN8bkr5H84AAh60MRs1ILhTqDAIXBc67kIlaNciXQADAQADAgADeQADFZkDAAEaBA"
suspects_photo = "AgACAgQAAxkBAANuXvdtNWOOnNyYe9mGiS06sBUEXKoAAhm0MRs1ILhTM6hM1lNl5zXgnXcjXQADAQADAgADeQAD_18BAAEaBA"
# envoyer une image au bot, choper son file_id dans la console avec photoecho et le coller ici

lieux_description = [["le Lieu 1", [LIEU2, LIEU3], image1, indice1],
                     ["le Lieu 2", [LIEU1, LIEU4], image2, indice2],
                     ["le Lieu 3", [LIEU1, LIEU5], image3, indice3],
                     ["le Lieu 4", [LIEU2, LIEU5], image4, indice4],
                     ["le Lieu 5", [LIEU3, LIEU4], image5, indice5],
                     ["la Chambre des Secrets", [LIEU1, LIEU2, LIEU3, LIEU4, LIEU5], image6, indice6]]

perso = ["Perso1", "Perso2", "Perso3", "Perso4", "Perso5"]

armes = ["Arme1", "Arme2", "Arme3", "Arme4", "Arme5"]

lieux = ["le Lieu 1", "le Lieu 2", "le Lieu 3", "le Lieu 4", "le Lieu 5"]

MEURTRIER, ARME, LIEU = range(3)

solution = ["Perso1", "Arme1", "le Lieu 1"]

proposition = ["Qui est le meurtrier ?",
               "Quelle arme a-t'il utilisé ?",
               "Où ça ?"]

ACTION, PHOTO, ENIGME, DEPLACEMENT, NEXT_PLACE, TENTATIVE = range(6)

enigmes = {0: {"question": "question",
               "reponse": "reponse"},
           1: {"question": "question",
               "reponse": "reponse"},
           2: {"question": "question",
               "reponse": "reponse"},
           3: {"question": "question",
               "reponse": "reponse"},
           4: {"question": "question",
               "reponse": "reponse"},
           5: {"question": "question",
               "reponse": "reponse"}}

well_dones = ["Bien joué !",
              "Oui c'est ça, bravo !",
              "Super !",
              "Génial !",
              "T'es trop fort 💪🏻",
              "Comment t'as deviné ?"]

try_agains = ["Essaie encore !",
              "Non, ce n'est pas ça...",
              "Non, désolé",
              "Ce n'est pas la bonne réponse",
              "Cherche encore !"]

MDP = "pantoufle"
INTREPIDES = range(1)

id_BDAmour = -430587684
