# main.py
import time
import machine
from splunk import send_to_splunk  # Importation de notre module dédié

print("Démarrage de l'application principale...")

# Exemple de boucle de surveillance
while True:
    # Simulation de lecture de capteurs (remplacez par vos vrais capteurs)
    donnees_capteur = {
        "device_id": "ESP32_WROOM_Prod",
        "message": "Hello, Splunk! Voici les données de capteur.",
        "uptime_seconds": time.ticks_ms() // 1000
    }
    
    print("Envoi des métriques à Splunk...")
    send_to_splunk(donnees_capteur)
    
    # Attendre 60 secondes avant le prochain envoi
    time.sleep(60)