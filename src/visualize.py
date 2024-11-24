import matplotlib.pyplot as plt

def visualize_traffic(traffic_data):
    """
    Visualizes the traffic data using a bar chart.
    """
    if not traffic_data:
        print("No traffic data to visualize!")
        return

    pairs = [f"{src}->{dst}" for src, dst in traffic_data.keys()]
    traffic = list(traffic_data.values())

    plt.figure(figsize=(12, 6))
    plt.bar(pairs, traffic, color="blue")
    plt.xlabel("Source -> Destination")
    plt.ylabel("Traffic (Bytes)")
    plt.title("Network Traffic Analysis")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
