from firebase_admin import db
from datetime import datetime

def getfiles(folder=''):
    ref = db.reference('/'+folder)
    return ref.get()

def updateTemperature(temp):
    dt = datetime.now()
    timestamp = dt.strftime("%Y-%m-%d-%H_%M_%S")
    ref = db.reference('/temp')
    refg = db.reference('/temp/graph')

    ref.update({'value':temp})
    refg.push({str(timestamp):temp})

    return f"Succesfully updated temperature to {temp}"

def updateHumidity(hum):
    dt = datetime.now()
    timestamp = dt.strftime("%Y-%m-%d-%H_%M_%S")
    ref = db.reference('/hum')
    refg = db.reference('/hum/graph')

    ref.update({'value':hum})
    refg.push({str(timestamp):hum})

    return f"Succesfully updated temperature to {hum}"
