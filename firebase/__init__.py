from firebase_admin import credentials, initialize_app

cred = credentials.Certificate("./firebase/creds.json")
myApp = initialize_app(
    cred,
    {
        "databaseURL":"https://green-coffee-beans-75fe4-default-rtdb.europe-west1.firebasedatabase.app/",
        "storageBucket":"gs://green-coffee-beans-75fe4.appspot.com",
    }
)