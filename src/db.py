from flask import *
from pymongo import *

# lien vers la base de données
client = MongoClient('mongo', 27017, username='admin', password='root')
# client = MongoClient('localhost', port=27017)

# création de la BDD ainsi que des collections
db = client.bdd_projet
utilisateur = db.utilisateur
questionnaire1 = db.questionnaire1
questionnaire2 = db.questionnaire2
questionnaire3 = db.questionnaire3
questionnaire4 = db.questionnaire4
questionnaire5 = db.questionnaire5

#  fonction permettant de sauvegarder un utilisateur
def save_user(email, password, nom, prenom):
    utilisateur.insert_one({'email': email, 'password': password, 'nom': nom, 'prenom': prenom })

# fonction renvoyant un utilisateur
def get_user(email,password): 
    print(utilisateur.find({'email': email, 'password': password}))
    return(utilisateur.find({'email': email, 'password': password}))

# fonction permettant d'enregistrer le premier questionnaire
def send_questionnaire1(question1,question2,question3,question4,question5,question6,question7,question8,question9,question10,question11,question12,question13,question14,question15,question16,question17,question18,question19,question20,question21,question22,question23,question24,question25,question26,question27,question28):
    questionnaire1.insert_one({'question1': question1,'question2': question2,'question3': question3,'question4': question4, 'question5': question5,'question6': question6,'question7': question7,'question8': question8,'question9': question9,'question10': question10,'question11': question11,'question12': question12,'question13': question13,'question14': question14,'question15': question15,'question16': question16,'question17': question17,'question18': question18,'question19': question19,'question20': question20,'question21': question21,'question22': question22,'question23': question23,'question24': question24,'question25': question25,'question26': question26,'question27': question27,'question28': question28})

# fonction permettant d'enregistrer le second questionnaire
def send_questionnaire2(question1,question2,question3,question4,question5,question6,question7,question8,question9,question10,question11,question12):
    questionnaire2.insert_one({'question1': question1,'question2': question2,'question3': question3,'question4': question4, 'question5': question5,'question6': question6,'question7': question7,'question8': question8,'question9': question9,'question10': question10,'question11': question11,'question12': question12})

# fonction permettant d'enregistrer le troisième questionnaire
def send_questionnaire3(question1,question2,question3,question4,question5,question6,question7,question8,question9,question10):
    questionnaire3.insert_one({'question1': question1,'question2': question2,'question3': question3,'question4': question4, 'question5': question5,'question6': question6,'question7': question7,'question8': question8,'question9': question9,'question10': question10})

# fonction permettant d'enregistrer le quatrième questionnaire
def send_questionnaire4(question1,question2,question3,question4,question5,question6,question7,question8,question9,question10,question11,question12):
    questionnaire4.insert_one({'question1': question1,'question2': question2,'question3': question3,'question4': question4, 'question5': question5,'question6': question6,'question7': question7,'question8': question8,'question9': question9,'question10': question10,'question11': question11,'question12': question12})

# fonction permettant d'enregistrer le cinquième questionnaire
def send_questionnaire5(question1,question2,question3,question4,question5,question6,question7,question8,question9,question10,question11,question12):
    questionnaire5.insert_one({'question1': question1,'question2': question2,'question3': question3,'question4': question4, 'question5': question5,'question6': question6,'question7': question7,'question8': question8,'question9': question9,'question10': question10,'question11': question11,'question12': question12})