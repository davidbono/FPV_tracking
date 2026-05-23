# splunk.py
import urequests
import json
import gc
from secrets import SPLUNK_HOST, SPLUNK_PORT, SPLUNK_TOKEN

def send_to_splunk(data, sourcetype="_json"):
    """
    Envoie un dictionnaire de données vers Splunk HEC via HTTPS.
    """
    # Utilisation du protocole https://
    url = f"https://{SPLUNK_HOST}:{SPLUNK_PORT}/services/collector/event"
    
    # Structure de l'enveloppe requise par Splunk
    payload = {
        "sourcetype": sourcetype,
        "event": data
    }
    
    headers = {
        "Authorization": f"Splunk {SPLUNK_TOKEN}",
        "Content-Type": "application/json"
    }
    
    response = None
    try:
        # Envoi de la requête POST sécurisée en convertissant le dictionnaire en chaîne JSON
        # Note : Le premier appel HTTPS peut prendre 1 à 2 secondes à cause du "handshake" SSL
        response = urequests.post(url, data=json.dumps(payload), headers=headers)
        
        if response.status_code == 200:
            print("[Splunk] Message envoyé avec succès en HTTPS !")
            return True
        else:
            print(f"[Splunk] Erreur {response.status_code}: {response.text}")
            return False
            
    except Exception as e:
        print(f"[Splunk] Erreur de connexion sécurisée : {e}")
        return False
        
    finally:
        # Nettoyage crucial pour éviter les fuites de mémoire (RAM) sur l'ESP32
        if response is not None:
            response.close()
        gc.collect() # Force la libération de la mémoire