import pyrebase

Config = {
    "apiKey": "AIzaSyCYu7gE_4HGDIy7pOOiw0AY-rrUmoE7eXQ",
    "authDomain": "sensehat-51bd7.firebaseapp.com",
    "databaseURL": "https://sensehat-51bd7.firebaseio.com",
    "storageBucket": "sensehat-51bd7.appspot.com"
}

Firebase = pyrebase.initialize_app(Config)
db = Firebase.database()

Environment_Data = db.child('/Environmet').get()
print(Environment_Data)
