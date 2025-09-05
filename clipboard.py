import json
import os
import pyperclip
import keyboard
from datetime import datetime

DB_FILE = r"C:\Users\K.G.S.Aman\history.json"

# Load existing history
if os.path.exists(DB_FILE):
    with open(DB_FILE, "r", encoding="utf-8") as f:
        try:
            history = json.load(f)
        except json.JSONDecodeError:
            history = []
else:
    history = []

def save_history():
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def add_entry(content):
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "content": content
    }
    history.append(entry)
    save_history()
    print(f"[+] Saved (Ctrl+B): {content[:40]}...")

def on_hotkey():
    text = pyperclip.paste()
    if text:
        add_entry(text)
    else:
        print("[!] Clipboard is empty.")

if __name__ == "__main__":
    print("📋 Clipboard watcher running. Press Ctrl+B to save clipboard content.")
    keyboard.add_hotkey("ctrl+b", on_hotkey)

    # Keep the script running
    keyboard.wait()
