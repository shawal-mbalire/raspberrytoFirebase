from firebase_admin import storage

bct = storage.bucket()

def uploadFile(src,name):
    bob = bct.blob(name)
    bob.upload_from_filename(src)
    return "Success"