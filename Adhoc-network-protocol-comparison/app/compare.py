import os
import pandas as pd
import matplotlib.pyplot as plt

# Get the directory path of the CSV files
results_dir = os.path.join(os.path.dirname(__file__), "Results")

# Load the data from the CSV files
dsr_data = pd.read_csv(os.path.join(results_dir, "dsr.csv"))
aodv_data = pd.read_csv(os.path.join(results_dir, "AODV.csv"))
dsdv_data = pd.read_csv(os.path.join(results_dir, "olsr.csv"))

# Calculate the total packets sent and received for DSR
total_packets_sent_dsr = dsr_data["PacketsReceived"].sum()
total_packets_received_dsr = dsr_data["SimulationSecond"].count()

# Calculate the average packet drop percentage for DSR
avg_packet_drop_dsr = ((total_packets_sent_dsr - total_packets_received_dsr) / total_packets_sent_dsr) * 100

# Calculate the total packets sent and received for AODV
total_packets_sent_aodv = aodv_data["PacketsReceived"].sum()
total_packets_received_aodv = aodv_data["SimulationSecond"].count()

# Calculate the average packet drop percentage for AODV
avg_packet_drop_aodv = ((total_packets_sent_aodv - total_packets_received_aodv) / total_packets_sent_aodv) * 100

# Calculate the total packets sent and received for DSDV
total_packets_sent_dsdv = dsdv_data["PacketsReceived"].sum()
total_packets_received_dsdv = dsdv_data["SimulationSecond"].count()

# Calculate the average packet drop percentage for DSDV
avg_packet_drop_dsdv = ((total_packets_sent_dsdv - total_packets_received_dsdv) / total_packets_sent_dsdv) * 100

# Create a bar chart to compare the average packet drop percentages
protocols = ["DSR", "AODV", "DSDV"]
avg_packet_drops = [avg_packet_drop_dsr, avg_packet_drop_aodv, avg_packet_drop_dsdv]

plt.bar(protocols, avg_packet_drops)
plt.xlabel("Routing Protocol")
plt.ylabel("Average Packet Drop (%)")
plt.title("Comparison of Average Packet Drop Percentage")
plt.show()
