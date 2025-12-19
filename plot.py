import pandas as pd
import matplotlib.pyplot as plt
# Loading CSV
df=pd.read_csv("data/adaptive_inventory_imbalance.csv")
# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])
# Plot 1: Total PnL vs Time
plt.figure()
plt.plot(df["timestamp"], df["total_pnl"])
plt.xlabel("Time")
plt.ylabel("Total PnL (₹)")
plt.title("Total PnL vs Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Plot 2: Inventory vs Time
plt.figure()
plt.plot(df["timestamp"], df["inventory"])
plt.xlabel("Time")
plt.ylabel("Inventory")
plt.title("Inventory vs Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
