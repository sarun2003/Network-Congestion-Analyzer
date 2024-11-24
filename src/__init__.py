# src/__init__.py

# Package metadata
__version__ = "1.0.0"
__author__ = "Your Name"
__description__ = "Network Congestion Analysis Tool"

# Import key modules for convenience
from .capture import start_sniffing, get_traffic_data
from .analyze import check_congestion
from .visualize import visualize_traffic
from .export import save_to_csv
from .config import CAPTURE_DURATION, TRAFFIC_THRESHOLD, OUTPUT_FILE
