import json
import time
import random

class BitrateCalculator:
    def __init__(self):
        self.previous_data = {}
        self.polling_interval = 0.5  # 2Hz (0.5s interval)

    def calculate_bitrate(self, nic_data):
        for nic in nic_data:
            mac_address = nic["MAC"]
            rx_octets = int(nic["Rx"]) 
            tx_octets = int(nic["Tx"])

            if mac_address in self.previous_data:
                prev_rx = self.previous_data[mac_address]["Rx"]
                prev_tx = self.previous_data[mac_address]["Tx"]

                # Calculate bitrate (bits per second)
                rx_bitrate = ((rx_octets - prev_rx) * 8) / self.polling_interval
                tx_bitrate = ((tx_octets - prev_tx) * 8) / self.polling_interval

                print(f"NIC: {nic['Description']} (MAC: {mac_address})")
                print(f"Timestamp: {nic['Timestamp']}")
                print(f"Rx Bitrate: {rx_bitrate:.2f} bits/sec")
                print(f"Tx Bitrate: {tx_bitrate:.2f} bits/sec\n")

            # Store current values for the next polling cycle
            self.previous_data[mac_address] = {"Rx": rx_octets, "Tx": tx_octets}

