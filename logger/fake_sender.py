import socket
import time
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
start = time.time()

while True:
    millis = int((time.time() - start) * 1000)
    t = 22 + random.uniform(-0.5, 0.5)
    h = 55 + random.uniform(-2, 2)
    msg = f"{millis},{t:.2f},{h:.2f}"
    sock.sendto(msg.encode(), ("127.0.0.1", 5005))
    print(msg)
    time.sleep(1)
