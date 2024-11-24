# Network Congestion Analyzer

## Overview
The **Network Congestion Analyzer** is a Python-based tool designed to monitor and analyze network traffic. It captures live network packets, analyzes traffic patterns, detects potential congestion, and visualizes the results. The tool can be useful for network administrators, students, and researchers interested in studying network behavior.

---

## Features
- **Traffic Capture**: Captures live TCP network packets.
- **Congestion Detection**: Identifies routes with traffic exceeding a defined threshold.
- **Visualization**: Visualizes traffic patterns using bar charts.
- **Data Export**: Saves analyzed traffic data to a CSV file for further analysis.
- **Customizable Configuration**: Modify capture duration and congestion thresholds in the `config.py` file.

---

## How It Works
1. Captures network packets using **Scapy**.
2. Analyzes traffic to detect congestion based on predefined thresholds.
3. Visualizes the captured traffic as a bar chart.
4. Saves the traffic data to a CSV file (`traffic_data.csv`).

---

## Project Structure
Network Congestion Analyzer/
├── main.py                 # Entry point for the program
├── src/
│   ├── __init__.py         # Makes 'src' a Python package
│   ├── capture.py          # Handles network traffic capture
│   ├── analyze.py          # Contains logic for analyzing traffic data
│   ├── visualize.py        # Handles visualization of traffic
│   ├── export.py           # Saves traffic data to a CSV file
│   ├── config.py           # Configuration and constants
├── venv/                   # Virtual environment
├── traffic_data.csv        # Exported traffic data
└── README.md               # Project documentation

---

## Requirements
- Python 3.6 or higher
- Virtual Environment (recommended)

### Python Libraries:
- [Scapy](https://pypi.org/project/scapy/)
- [Matplotlib](https://pypi.org/project/matplotlib/)

---

## Installation
1. **Clone the Repository**:
   git clone https://github.com/your-username/network-congestion-analyzer.git
   cd network-congestion-analyzer

2. **Clone the Repository**:
   python3 -m venv venv
source venv/bin/activate  
Since I made it on my Mac you can use use this one on **Windows**: venv\Scripts\activate
4. **Install Dependencies**:
   Run the Program:
5. **Run the Program**:
   python main.py

---

## Testing The Tool
1. **Generate Network Traffic**: Open a new terminal and create network activity (e.g., ping, curl).
2. **Analyze and Visualize**: Run the program to capture and analyze traffic. Results will be visualized and exported as traffic_data.csv.

---

## Configuration
Let's modify the config.py file to customize settings:
**Capture Duration**: Time (in seconds) to capture packets.
**Traffic Threshold**: Threshold for detecting congestion.

---

**Example**:
CAPTURE_DURATION = 20  # Capturing for 20 seconds
TRAFFIC_THRESHOLD = 10000  # It will be the bytes

---

## Example Output

**Congestion Detection**
Starting Network Congestion Analysis Tool...
Capturing traffic for 10 seconds...
Traffic capture complete!
Analyzing traffic for congestion...
Congestion detected on the following routes:
192.168.1.1 -> 8.8.8.8: 15000 Bytes
Traffic data saved to traffic_data.csv
Analysis complete!

---

## Visualization
Captured traffic is saved in traffic_data.csv with the following structure:

Source, Destination, Traffic (Bytes)
192.168.1.1, 8.8.8.8, 15000
192.168.1.2, 8.8.4.4, 5000

---

## Limitations

1. Requires administrative privileges to access network interfaces.
2. Limited to analyzing TCP traffic by default (modifiable in capture.py).

---

## Contributing
Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests to improve the project.

---

## Contact
For any questions or suggestions, feel free to contact me:
Email: sarunshrestha03@gmail.com
GitHub: sarun2003

---




