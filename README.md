# Ghost Keylogger Project

## ⚠️ Disclaimer
**This tool is for ethical learning purposes only. Do not deploy it on systems you do not own or control.**

## 🔒 Purpose
A stealthy Python-based keylogger that captures keystrokes and exfiltrates data via Gmail, demonstrating offensive security tactics.

## 🚀 Features
- Global keyboard logging via `pynput`
- Logs sent automatically every 5 minutes
- Uses Gmail SMTP over SSL
- Basic obfuscation (base64)
- Minimal footprint (threaded, no local files)

## 📦 Requirements
- Python 3.7+
- pip install pynput

## How to Run

1.Enable Gmail App Passwords

    Go to https://myaccount.google.com/security

    Turn on 2FA

    Generate a 16-character App Password for "Mail"

2.Edit the Script

    Replace the encoded_email and encoded_pass fields with your base64-encoded credentials:

    import base64
    print(base64.b64encode(b"your_email@gmail.com"))
    print(base64.b64encode(b"your_app_password"))

3.Run it

python red_keylogger.py

    Will silently log all keys

    Sends logs via email every 5 minutes

4.Stop it

    Press Ctrl+C in terminal

    Or kill from Task Manager / ps command


