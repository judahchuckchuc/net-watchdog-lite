### 📘 `README.md`

````markdown
# 🐍 net-watchdog-lite

A lightweight Python-based network monitoring and alerting tool for Linux/Termux systems.

It watches for suspicious traffic patterns like port scans, high packet rates, or strange IP behavior — and then logs or alerts you via email, webhook, or console.

---

## ⚡ Features

- 📡 Real-time traffic sniffing with `scapy`
- 🕵️ Port scan detection
- 📈 High traffic spike alerts
- 📬 Sends alerts via console, webhook, or email
- 🌐 Flask dashboard for live alert view
- 🛠️ Run as a systemd background service

---

## 🧰 Requirements

Install Python packages:

```bash
pip install -r requirements.txt
````

Also ensure you have:

* Python 3.7+
* Root access for sniffing
* `scapy`, `requests`, `flask`

---

## 🔧 Configuration

Edit `config.json` to set detection thresholds:

```json
{
  "scan_threshold": 20,
  "scan_timeframe": 5,
  "traffic_threshold": 100,
  "traffic_timeframe": 10
}
```

To enable email or webhook alerts, update `alert.py`:

```python
EMAIL_ENABLED = True
WEBHOOK_ENABLED = True
```

And configure the SMTP or webhook section.

---

## ▶️ How to Run

### 1. Direct (Console Mode)

```bash
sudo python3 main.py --interface eth0
```

> Replace `eth0` with your active interface (e.g. `wlan0`, `enp0s3`, etc.)

### 2. Flask Dashboard

```bash
python3 dashboard.py
```

Open your browser at: [http://localhost:5000](http://localhost:5000)

---

## ⚙️ systemd Service (Optional)

To run it in the background on boot:

1. Move the project:

```bash
sudo mkdir -p /opt/net-watchdog-lite
sudo cp -r * /opt/net-watchdog-lite
```

2. Install the service:

```bash
sudo cp net-watchdog.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl enable --now net-watchdog
```

Check logs:

```bash
sudo journalctl -u net-watchdog -f
```

---

## 📁 Project Structure

```
net-watchdog-lite/
├── main.py               # Monitoring logic
├── alert.py              # Alert sending logic (email/webhook)
├── config.json           # Alert thresholds
├── suspicious.log        # Detected issues
├── dashboard.py          # Flask dashboard
├── requirements.txt      # Python deps
├── net-watchdog.service  # Background service
└── README.md
```

---

## 🧪 Sample Output

```
[ALERT] High traffic from 104.23.7.88 — 150 packets in 10s
[ALERT] Possible port scan from 192.168.1.10 — 25 ports in 5s
```

---

## 🛡️ Disclaimer

Use responsibly. This tool is for educational and internal network monitoring purposes only. Don't sniff traffic on networks you don't own or manage.

---

## 📬 Feedback

Pull requests and issues are welcome! Built by Judah Lotto Madilola with ❤️ for security tinkering.

```

---


