===========================================================
        Encrypted Keylogger with Decryption Viewer
===========================================================

Author: Prashant Mall  
Language: Python 
Encryption: Fernet (symmetric encryption)  
UI: Tkinter  
Dependencies: pynput, cryptography, tkinter

-----------------------------------------------------------
📌 Project Overview
-----------------------------------------------------------

This project is a secure keylogger tool built for educational and research purposes. 
It captures each keystroke on a system, encrypts it in real-time using a symmetric 
encryption key, and stores it with a timestamp in a log file. A GUI viewer application 
is also included to decrypt and visualize these logs.

All sensitive logs are encrypted using the `cryptography.fernet` module to ensure data
confidentiality even if the logs are accessed directly.

-----------------------------------------------------------
📦 Project Structure
-----------------------------------------------------------

|-- keylogger.py         → Starts keylogging and logs encrypted keys
|-- encrypt_util.py      → Handles encryption and decryption logic
|-- keygeneration.py     → Generates Fernet encryption key
|-- decrypt.py           → CLI tool to read and decrypt log file
|-- gui_log_viewer.py    → GUI viewer to decrypt and display keystrokes
|-- config.json          → Stores the encryption key (used by logger/viewer)
|-- logs/
    └── keystrokes.log   → Log file storing encrypted keystrokes

-----------------------------------------------------------
🔧 Setup Instructions
-----------------------------------------------------------

1. Install dependencies:
   pip install pynput cryptography

2. Generate an encryption key:
   Run `keygeneration.py` to generate a Fernet key. Copy the key into `config.json` like:
   {
       "encryption_key": "YOUR_GENERATED_KEY"
   }

3. Start the keylogger:
   Run `main.py` to begin logging keystrokes. Logs will be stored in `logs/keystrokes.log`.

4. View logs using GUI:
   Run `logViewerGUI_InDecryptedFormat.py` to open a simple viewer:
   - Search and filter logs
   - Export logs to .txt or .csv
   - Decrypt logs in real-time

5. (Optional) Use `decrypt.py` to print logs in terminal.

-----------------------------------------------------------
🔐 Security Note
-----------------------------------------------------------

This project is intended for learning and ethical use ONLY.

DO NOT deploy or distribute this without clear permission from the system owner.
Unauthorized use may be illegal and unethical.

