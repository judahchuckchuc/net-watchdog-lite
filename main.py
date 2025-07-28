from scapy.all import sniff, IP, TCP
from collections import defaultdict
import time, json, threading, argparse
from alert import alert

with open('config.json') as f:
    config = json.load(f)

scan_data = defaultdict(list)
traffic_data = defaultdict(list)

def monitor_packet(pkt):
    if IP in pkt:
        ip = pkt[IP].src
        ts = time.time()

        traffic_data[ip].append(ts)
        traffic_data[ip] = [t for t in traffic_data[ip] if ts - t <= config["traffic_timeframe"]]
        if len(traffic_data[ip]) > config["traffic_threshold"]:
            alert(f"[ALERT] High traffic from {ip} — {len(traffic_data[ip])} packets in {config['traffic_timeframe']}s")

        if TCP in pkt:
            dport = pkt[TCP].dport
            scan_data[ip].append((dport, ts))
            recent_ports = [(p, t) for p, t in scan_data[ip] if ts - t <= config["scan_timeframe"]]
            unique_ports = set(p for p, _ in recent_ports)
            if len(unique_ports) > config["scan_threshold"]:
                alert(f"[ALERT] Possible port scan from {ip} — {len(unique_ports)} ports in {config['scan_timeframe']}s")

def start_sniffing(interface):
    sniff(prn=monitor_packet, store=False, iface=interface)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--interface", "-i", required=True, help="Network interface to monitor")
    args = parser.parse_args()
    print(f"[*] Starting net-watchdog-lite on {args.interface}...")
    thread = threading.Thread(target=start_sniffing, args=(args.interface,))
    thread.start()