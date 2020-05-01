import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyDUIrWAOBnic9bKIs18AU_SBkiAQuhXio8",
    "authDomain": "rottenonions-28d94.firebaseapp.com",
    "databaseURL": "https://rottenonions-28d94.firebaseio.com",
    "projectId": "rottenonions-28d94",
    "storageBucket": "rottenonions-28d94.appspot.com",
    "messagingSenderId": "647937849917",
    "appId": "1:647937849917:web:408be5feedb5f496a58854",
    "measurementId": "G-SX2NDJ6MH9"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def push_db(enterParamsHere):
    """
    ----------------------------------------
    Inserts given data into firebase db
    ---------------------------------------
    :param params
    --------------------------------------
    :return: result - boolean
    """
    data = {
        'data': enterParamsHere,
    }
    result = db.collection("collection").set(data)
    return result

