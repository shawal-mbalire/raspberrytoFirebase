from firebase_admin import credentials, initialize_app

cred = credentials.Certificate("./myFirebase/creds.json")
myApp = initialize_app(
    cred,
    {
        'apiKey': "",
        'authDomain': "",
        'databaseURL': "",
        'projectId': "",
        'storageBucket': "",
        'messagingSenderId': "",
        'appId': "",
        'measurementId': ""
    }
)
