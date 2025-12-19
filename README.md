# Market Making Strategy using Nubra Trading API (UAT)

This project implements and compares multiple **market-making strategies** using **real-time order book data** from the **Nubra Trading API (UAT environment)**.  
The objective is to study the trade-off between **profitability** and **risk control** through systematic experimentation.

The system simulates live market making, tracks inventory and PnL, logs results to CSV, and visualizes performance across strategies.

---

##  Key Features

- Live order book ingestion using Nubra Python SDK
- Real-time bid–ask quote generation
- Paper-trading fill simulation
- Inventory and PnL tracking (realized + unrealized)
- Risk controls via inventory limits
- CSV logging for analysis
- Comparative visualization of strategies

---

##  Implemented Strategies

### 1️ Baseline Strategy
- Fixed spread around mid-price
- Always quotes both bid and ask
- Maximizes spread capture
- **No active inventory risk control**

 Purpose: Benchmark / control strategy

---

### 2️ Adaptive Strategy (Inventory-Aware)
- Quotes are skewed based on current inventory
- Reduces exposure as inventory grows
- Lower trading frequency, safer behavior

 Purpose: Demonstrate inventory risk management

---

### 3️ Adaptive Strategy (Inventory + Order Book Imbalance)
- Inventory-aware skew
- Additional skew based on order book imbalance
- Avoids toxic order flow
- Most stable and robust strategy

 Purpose: Production-style market making

---

##  Strategy Comparison Summary

|      Strategy         | Profitability | Inventory Risk | Stability |
|-----------------------|---------------|----------------|-----------|
| Baseline              | High (short-term) |   High     |    Low    |
| Adaptive(Inventory)   | Low–Medium    |       Low      |    High   |
| Adaptive(Inventory+Imbalance) | Medium |   Very Low    | Very High |

---

##  Project Structure

nubra-market-making/
│
├── core/
│ ├── market_data.py # Market data access
│ ├── orderbook.py # Order book wrapper
│ ├── simulator.py # Paper-trade fill simulation
│ └── pnl.py # PnL tracking
│ └── nubra_client.py 
│ └── instruments.py #instruments access
│ 
├── strategies/
│ ├── base_strategy.py # Baseline strategy
│ └── adaptive_strategy.py #adaptive strategy
│
├── utils/
│ └── csv_logger.py # CSV logging
│
├── data/
│ ├── baseline_strategy.csv
│ ├── adaptive_inventory.csv
│ └── adaptive_inventory_imbalance.csv
│
├── plots/
│ ├── pnl_comparison.png
│ └── inventory_comparison.png
│ ├── pnl_time_baseline.png
│ └── inventory_time_baseline.png
│ ├── pnl_time_adaptive_inventory.png
│ └── inventory_time_adaptive_inventory.png
│ ├── pnl_time_adaptive_inventory_imbalance.png
│ └── inventory_time_adaptive_inventory_imbalance.png
|
├── analysis/
│ ├── comparision_plot.py
│ └── individual_plot.py
│
├── baseline_strategy_simulator.py
├── adaptive_strategy_simulator.py
|
│
├── requirements.txt
├── README.md
└── report.pdf


---

## Setup Instructions

### 1️ Install dependencies
pip install -r requirements.txt

### 2 Configure Nubra credentials
Create a .env file (or use Nubra SDK login flow):
NUBRA_ENV=uat
NUBRA_MOBILE=your_mobile
NUBRA_MPIN=your_mpin

## Running the strategies
baseline
python baseline_strategy_simulator.py
adaptive
python adaptive_strategy_simulator.py

## Visualization
After running the strategies, performance is compared using:
Total PnL vs Time
Inventory vs Time
All plots are generated from the CSV logs using matplotlib.

## Key Insights

Baseline strategies may show higher short-term PnL but accumulate dangerous inventory risk.

Inventory-aware strategies significantly reduce exposure.

Incorporating order book imbalance improves robustness and stability.

Sustainable market making prioritizes risk-adjusted returns, not raw PnL.

## Disclaimer

This project is for educational and research purposes only.
No real trading or financial advice is implied.

## Acknowledgements

Nubra Trading API & Python SDK

Concepts from market microstructure and quantitative finance


