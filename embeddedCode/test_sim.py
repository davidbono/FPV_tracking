# test_sim.py
from machine import UART, Pin
import time

# 1. Configurer la broche d'allumage (si présente sur votre shield)
# Une impulsion basse/haute de 1 à 2 secondes allume la puce SIM7600
pwr_key = Pin(4, Pin.OUT)
print("Allumage du module SIM7600G...")
pwr_key.value(1)
time.sleep_ms(1500)
pwr_key.value(0)
time.sleep(5) # Attendre que le modem démarre

# 2. Configurer la liaison Série (UART 2)
# TX=17, RX=16 est le standard sur la majorité des cartes ESP32
modem = UART(2, baudrate=115200, tx=17, rx=16, timeout=2000)

def send_at_command(cmd, delay=1000):
    print(f"Envoi : {cmd}")
    modem.write(cmd + "\r\n")
    time.sleep_ms(delay)
    if modem.any():
        response = modem.read().decode('utf-8', 'ignore')
        print(f"Réponse :\n{response}")
        return response
    else:
        print("Aucune réponse du module.")
        return ""

# --- SÉQUENCE DE TEST ---
# Test de communication basique (Doit répondre OK)
send_at_command("AT")

# Vérifier que la carte SIM est bien détectée (Doit répondre +CPIN: READY)
send_at_command("AT+CPIN?")

# Vérifier la qualité du signal cellulaire (Ex: 25,99)
send_at_command("AT+CSQ")

# Vérifier si l'appareil est enregistré sur le réseau mobile
send_at_command("AT+CREG?")