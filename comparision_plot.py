import pandas as pd
import matplotlib.pyplot as plt
# Loading data
baseline=pd.read_csv("data/baseline_strategy.csv")
adaptive_inv=pd.read_csv("data/adaptive_inventory.csv")
adaptive_imb=pd.read_csv("data/adaptive_inventory_imbalance.csv")

# Converting timestamps
for df in [baseline,adaptive_inv,adaptive_imb]:
    df["timestamp"]=pd.to_datetime(df["timestamp"])
    df["t"]=(df["timestamp"]-df["timestamp"].iloc[0]).dt.total_seconds()

# Plot 1: Total PnL vs Time
plt.figure(figsize=(10,5))
plt.plot(baseline["t"], baseline["total_pnl"], label="Baseline")
plt.plot(adaptive_inv["t"], adaptive_inv["total_pnl"], label="Adaptive (Inventory)")
plt.plot(adaptive_imb["t"], adaptive_imb["total_pnl"], label="Adaptive (Inventory + Imbalance)")
plt.xlabel("Time (seconds)")
plt.ylabel("Total PnL (₹)")
plt.title("Total PnL vs Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
# Plot 2: Inventory vs Time
plt.figure(figsize=(10,5))
plt.plot(baseline["t"], baseline["inventory"], label="Baseline")
plt.plot(adaptive_inv["t"], adaptive_inv["inventory"], label="Adaptive (Inventory)")
plt.plot(adaptive_imb["t"], adaptive_imb["inventory"], label="Adaptive (Inventory + Imbalance)")
plt.xlabel("Time (seconds)")
plt.ylabel("Inventory")
plt.title("Inventory vs Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
