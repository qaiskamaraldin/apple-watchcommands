import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

config_file =  "./private_key.json"
cred = credentials.Certificate(config_file)

firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://apple-watchcommands-default-rtdb.firebaseio.com/'
})

firstpath = False
ref = db.reference('/')


def listener(data):
    global firstpath
    
    if firstpath:
        
    firstpath = True


    



db.reference('/').listen(listener)
