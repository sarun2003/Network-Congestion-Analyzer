from scapy.all import sniff, IP, TCP
from collections import defaultdict

# Dictionary to store traffic data
traffic_data = defaultdict(int)

def packet_handler(packet):
    """
    Processes each captured packet and logs its size.
    """
    if IP in packet and TCP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        # Add the size of the packet to the traffic data
        traffic_data[(ip_src, ip_dst)] += len(packet)

def start_sniffing(duration=10):
    """
    Captures network traffic for a specified duration.
    """
    print(f"Capturing traffic for {duration} seconds...")
    sniff(filter="tcp", prn=packet_handler, timeout=duration)
    print("Traffic capture complete!")

def get_traffic_data():
    """
    Returns the captured traffic data.
    """
    return traffic_data
