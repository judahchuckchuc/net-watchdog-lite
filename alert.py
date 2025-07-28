import smtplib
import requests

WEBHOOK_URL = "https://your-webhook-url.com"
EMAIL_ENABLED = False
WEBHOOK_ENABLED = False

EMAIL_CONFIG = {
    "smtp_server": "smtp.example.com",
    "port": 587,
    "sender": "your@email.com",
    "password": "yourpassword",
    "receiver": "receiver@email.com"
}

def send_email(message):
    try:
        server = smtplib.SMTP(EMAIL_CONFIG["smtp_server"], EMAIL_CONFIG["port"])
        server.starttls()
        server.login(EMAIL_CONFIG["sender"], EMAIL_CONFIG["password"])
        server.sendmail(EMAIL_CONFIG["sender"], EMAIL_CONFIG["receiver"], message)
        server.quit()
    except Exception as e:
        print(f"[ERROR] Email failed: {e}")

def send_webhook(message):
    try:
        requests.post(WEBHOOK_URL, json={"text": message})
    except Exception as e:
        print(f"[ERROR] Webhook failed: {e}")

def alert(message):
    print(message)
    with open("suspicious.log", "a") as f:
        f.write(message + "\n")
    if EMAIL_ENABLED:
        send_email(message)
    if WEBHOOK_ENABLED:
        send_webhook(message)