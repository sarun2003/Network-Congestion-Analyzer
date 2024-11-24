import sys
import os

# Here I added the project root to the pythonpath
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.capture import start_sniffing, get_traffic_data
from src.analyze import check_congestion
from src.visualize import visualize_traffic
from src.export import save_to_csv
from src.config import CAPTURE_DURATION, TRAFFIC_THRESHOLD, OUTPUT_FILE

def main():
    print("Starting Network Congestion Analysis Tool...")

    # Step 1 is to capture the traffic
    start_sniffing(CAPTURE_DURATION)
    traffic_data = get_traffic_data()

    # Step 2 is to analyze the congestion
    check_congestion(traffic_data, TRAFFIC_THRESHOLD)

    # Step 3 is to visualize the same traffic
    visualize_traffic(traffic_data)

    # Step 4 the final one is to save the data
    save_to_csv(traffic_data, OUTPUT_FILE)

    print("Analysis complete!")

if __name__ == "__main__":
    main()
