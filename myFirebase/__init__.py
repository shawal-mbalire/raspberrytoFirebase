from firebase_admin import credentials, initialize_app

cred = credentials.Certificate("./myFirebase/creds.json")
myApp = initialize_app(
    cred,
    {
        'apiKey': "AIzaSyAi1q5puRg4RqjMpjdQCB5Ozwe0h2BxKTk",
        'authDomain': "green-coffee-beans-75fe4.firebaseapp.com",
        'databaseURL': "https://green-coffee-beans-75fe4-default-rtdb.europe-west1.firebasedatabase.app",
        'projectId': "green-coffee-beans-75fe4",
        'storageBucket': "green-coffee-beans-75fe4.appspot.com",
        'messagingSenderId': "392123065",
        'appId': "1:392123065:web:55f57eb6ccb709ca23c168",
        'measurementId': "G-VD7KLJHSZY"
    }
)