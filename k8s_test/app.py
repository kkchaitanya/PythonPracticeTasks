import time
import socket
while True:
    print("Hello from Euron Kubernetes!")
    print("Running on:", socket.gethostname())
    print("--------------------------", flush=True)
    time.sleep(5)