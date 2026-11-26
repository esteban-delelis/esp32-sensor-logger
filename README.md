# esp32-sensor-logger

ESP32 qui envoie température et humidité vers un script Python qui les enregistre avec l'horodatage.

## Architecture du projet
* **`firmware/`** : Code embarqué pour ESP32 (Arduino/C++) lisant un capteur **SHT31** via le bus I2C (`SDA = GPIO21`, `SCL = GPIO22`) et envoyant les données en **UDP** toutes les secondes.
* **`logger/`** : Script **Python** écoutant le port UDP `5005` et enregistrant chaque mesure dans un fichier `mesures.csv` avec l'horodatage local du PC (`heure_pc`) et l'horloge interne de la carte (`millis_esp32`).

## Installation et utilisation
1. Copier `firmware/secrets.example.h` vers `firmware/secrets.h` et renseigner les identifiants Wi-Fi ainsi que l'adresse IP du PC.
2. Téléverser `firmware/firmware.ino` sur l'ESP32 (nécessite la bibliothèque `Adafruit SHT31 Library`).
3. Lancer le récepteur sur l'ordinateur :
   ```bash
   python logger/logger.py
   ```

## État d'avancement et observations
* **Matériel non encore raccordé :** Le câblage physique (ESP32 + capteur SHT31) n'a pas encore été testé en conditions réelles par manque d'équipement.
* **Problématique visée (synchronisation des horloges) :** Le format d'enregistrement est conçu pour comparer l'intervalle régulier de la carte (`millis_esp32`) avec l'instant de réception sur le PC (`heure_pc`), afin de mesurer concrètement la gigue (variation du délai de transmission) induite par le réseau Wi-Fi.
