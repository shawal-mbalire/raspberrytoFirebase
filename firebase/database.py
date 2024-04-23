from firebase_admin import db

ref = db.reference('/')
print(ref.get())