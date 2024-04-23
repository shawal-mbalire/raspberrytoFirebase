from firebase_admin import storage, db
from datetime import datetime

bct = storage.bucket()

def uploadFile(src,type:str):
    dt = datetime.now()
    timestamp = dt.strftime("%Y-%m-%d-%H_%M_%S")
    name = type+str(timestamp)+".jpeg"
    bob = bct.blob(name)
    bob.upload_from_filename(src)
    if type == "captured":
        ref = db.reference('/capImg')
        refg = db.reference('/capImg/graph')
    if type == "inferenced":
        ref = db.reference('/mlImg')
        refg = db.reference('/mlImg/graph')

    ref.update({'value':name})
    refg.push({str(timestamp):name})

    return f"Successfully uploaded {name}"