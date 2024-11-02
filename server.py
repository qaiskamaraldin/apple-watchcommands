import os
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

# Initialize Firebase Admin SDK
config_file = "./private_key.json"
cred = credentials.Certificate(config_file)

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://apple-watchcommands-default-rtdb.firebaseio.com/'
})

firstpath = False
ref = db.reference('/')

def listener(data):
    global firstpath
    
    if firstpath:
        # Extract the command from the data received
        command = data['data']['command']  # Adjust according to your data structure
        print(f"Received command: {command}")
        
        # Execute commands based on input
        if command == '1':
            os.system('shutdown /s /t 1')  # Shutdown
        elif command == '2':
            os.system('shutdown /r')  # Reboot
        elif command == '3':
            os.system('shutdown /l')  # Log off
    
    firstpath = True

# Listen for changes in the database
db.reference('/').listen(listener)
