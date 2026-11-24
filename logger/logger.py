import socket
import csv
from datetime import datetime

PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", PORT))

with open("mesures.csv", "a", newline="") as f:
    writer = csv.writer(f)
    if f.tell() == 0:
        writer.writerow(["heure_pc", "millis_esp32", "temperature_C", "humidite_pct"])
    print("En écoute sur le port", PORT)
    while True:
        data, addr = sock.recvfrom(1024)
        millis, t, h = data.decode().strip().split(",")
        writer.writerow([datetime.now().isoformat(), millis, t, h])
        f.flush()
        print(millis, t, h)
