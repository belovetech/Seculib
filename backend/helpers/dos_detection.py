from scapy.all import sniff, IP
from collections import defaultdict

packet_counts = defaultdict(int)
threshold = 100  # Adjust this threshold as needed
window_size = 60  # Time window in seconds

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        packet_counts[src_ip] += 1
        print(f"Packet count from {src_ip}: {packet_counts[src_ip]}")

        if packet_counts[src_ip] > threshold:
            print(f"Possible DoS attack from {src_ip}")

def monitor_network(interface):
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == '__main__':
    interface = 'lo0'  # Change this to your correct network interface
    monitor_network(interface)
