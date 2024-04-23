from . import mydht

def measure():
    try:
        temperature = mydht.temperature
        humidity    = mydht.humidity

        if humidity is not None and temperature is not None:
            print(f"DHT Sensor Data - Humidity: {humidity}%, Temperature: {temperature}°C")
            return humidity, temperature
        else:
            print("Failed to retrieve data from humidity sensor")
            return -1,-1
    except RuntimeError as error:
        print(error.args[0])