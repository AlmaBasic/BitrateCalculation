import json
import time
import random
from bitrate import BitrateCalculator

# Load JSON from file
with open("data.json", "r") as file:
    device_data = json.load(file)

bitrate_calculator = BitrateCalculator()

# Simulating polling every 0.5 seconds (2Hz)
for _ in range(5): 
    for nic in device_data["NIC"]: 
        nic["Rx"] = str(int(nic["Rx"]) + random.randint(10000, 50000))
        nic["Tx"] = str(int(nic["Tx"]) + random.randint(8000, 40000))

    bitrate_calculator.calculate_bitrate(device_data["NIC"])
    time.sleep(0.5)  # Wait for the next polling cycle
