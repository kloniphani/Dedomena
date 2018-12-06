import pyrebase
import pandas as pd

Config = {
    "apiKey": "AIzaSyCYu7gE_4HGDIy7pOOiw0AY-rrUmoE7eXQ",
    "authDomain": "sensehat-51bd7.firebaseapp.com",
    "databaseURL": "https://sensehat-51bd7.firebaseio.com",
    "storageBucket": "sensehat-51bd7.appspot.com"
}

Firebase = pyrebase.initialize_app(Config)
db = Firebase.database()

Environment_Data = db.child('Environment').get()
Movement_Data = db.child('Movement').get()

# Create a Pandas dataframe from the data.
DATA = []
for Reading in Environment_Data.each():
    KEYS = []; VALUES = []
    for key, value in Reading.val().items():
        KEYS.append(key); VALUES.append(value)
    print(VALUES)
    DATA.append(VALUES)
Environment_DataFrame = pd.DataFrame(DATA, columns = KEYS)

# Create a Pandas dataframe from the data.
DATA = []
for Reading in Movement_Data.each():
    KEYS = []; VALUES = []
    for key, value in Reading.val().items():
        if key == 'Orientation': continue;
        elif key == 'Acceleration':
            for k, v in value.items():
                KEYS.append(k); VALUES.append(v)
        else:
            KEYS.append(key); VALUES.append(value)
    print(VALUES)
    DATA.append(VALUES)
Acceleration_DataFrame = pd.DataFrame(DATA, columns = KEYS)

# Create a Pandas dataframe from the data.
DATA = []
for Reading in Movement_Data.each():
    KEYS = []; VALUES = []
    for key, value in Reading.val().items():
        if key == 'Acceleration': continue;
        elif key == 'Orientation':
            for k, v in value.items():
                KEYS.append(k); VALUES.append(v)
        else:
            KEYS.append(key); VALUES.append(value)
    print(VALUES)
    DATA.append(VALUES)
Orientation_DataFrame = pd.DataFrame(DATA, columns = KEYS)

# Create a Pandas Excel writer using XlsxWriter as the engine.
Writer = pd.ExcelWriter('SensorData.xlsx', engine = 'xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
Environment_DataFrame.to_excel(Writer, sheet_name = 'Environment', index = False)
Acceleration_DataFrame.to_excel(Writer, sheet_name = 'Acceleration', index = False)
Orientation_DataFrame.to_excel(Writer, sheet_name = 'Orientation', index = False)

# Clospd.DataFramee the Pandas Excel writer and output the Excel file.
Writer.save()
Writer.close()
