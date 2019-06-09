import requests
import time

def internetConnected():
    while True:
        url = 'http://www.google.com'
        timeout = 5
        try:
            _ = requests.get(url, timeout=timeout)
            print("Connected")
        except requests.ConnectionError:
            print("Internet not connected -- retrying.")
        
        time.sleep(3)

internetConnected()
