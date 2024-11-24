def check_congestion(traffic_data, threshold=5000):
    """
    Analyzes the traffic data for congestion.
    """
    print("Analyzing traffic for congestion...")
    congested_routes = [(src, dst, traffic) for (src, dst), traffic in traffic_data.items() if traffic > threshold]
    if not congested_routes:
        print("No congestion detected!")
    else:
        print("Congestion detected on the following routes:")
        for src, dst, traffic in congested_routes:
            print(f"{src} -> {dst}: {traffic} Bytes")

    return congested_routes
