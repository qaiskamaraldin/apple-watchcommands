import os
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

# Path to Firebase config file (replace with your actual path)
config_file = "path/to/your-firebase-adminsdk.json"
cred = credentials.Certificate(config_file)

# Initialize Firebase app with database URL
firebase_admin.initialize_app(cred, {
    'databaseURL': 'your-database-url'  # Replace with your actual database URL
})

# Track if listener has run at least once
firstpath = False
command = ""

# Listener function for database changes
def listener(event):
    global firstpath, command
    
    # Skip the initial snapshot if it's the first run
    if firstpath:
        # Retrieve the latest command
        sorted_input = dict(ref.order_by_key().limit_to_last(1).get())
        if sorted_input:
            # Extract command from the latest entry
            command = list(sorted_input.values())[0].get('command', "")
            print(f"Received command: {command}")

            # Execute commands based on the value of `command`
            if command == '1':
                os.system('shutdown /s /t 1')  # Shutdown
            elif command == '2':
                os.system('shutdown /r /t 1')  # Restart
            elif command == '3':
                os.system('shutdown /l')  # Log off

    # Set firstpath to True after the first run
    firstpath = True

# Reference to the root of the database
ref = db.reference('/')
<<<<<<< HEAD
ref.listen(listener)
=======
ref.listen(listener)
>>>>>>> 75e501db995eda6493890533016fa20a316d12f3
