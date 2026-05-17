# boot.py -- run on boot-up
import network
import time
from secrets import WIFI_SSID, WIFI_PASS # Importation des secrets

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print(f"Connexion à {WIFI_SSID}...")
        wlan.connect(WIFI_SSID, WIFI_PASS)
        
        # Attente de connexion
        for _ in range(10):
            if wlan.isconnected():
                break
            time.sleep(1)
            print(".", end="")
            
    if wlan.isconnected():
        print("\nConnecté !")
        print("IP:", wlan.ifconfig()[0])
    else:
        print("\nÉchec de connexion.")

connect_wifi()