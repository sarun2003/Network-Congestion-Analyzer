import csv

def save_to_csv(traffic_data, filename="traffic_data.csv"):
    """
    Saves the traffic data to a CSV file.
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Source", "Destination", "Traffic (Bytes)"])
        for (src, dst), traffic in traffic_data.items():
            writer.writerow([src, dst, traffic])
    print(f"Traffic data saved to {filename}")
