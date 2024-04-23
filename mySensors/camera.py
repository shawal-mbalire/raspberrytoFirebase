from . import mycamera
from datetime import datetime

def capture():
    dt = datetime.now()
    timestamp = dt.strftime("%Y-%m-%d-%H_%M_%S")
    name = timestamp+".jpg"
    try:
        mycamera.capture_file(name)
        print(f"Image saved as {name}")
        return name
    except Exception as e:
        print(f"Error: {e}")
