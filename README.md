# Market Making Strategy using Nubra Trading API (UAT)

This project implements and compares multiple **market-making strategies** using **real-time order book data** from the **Nubra Trading API (UAT environment)**.  
The objective is to study the trade-off between **profitability** and **risk control** through systematic experimentation.

The system simulates live market making, tracks inventory and PnL, logs results to CSV, and visualizes performance across strategies.

---

## Key Features

- Live order book ingestion using Nubra Python SDK
- Real-time bid–ask quote generation
- Paper-trading fill simulation
- Inventory and PnL tracking (realized + unrealized)
- Risk controls via inventory limits
- CSV logging for analysis
- Comparative visualization of strategies

---

## Implemented Strategies

### 1. Baseline Strategy
- Fixed spread around mid-price
- Always quotes both bid and ask
- Maximizes spread capture
- **No active inventory risk control**

> Purpose: Benchmark / control strategy

---

### 2. Adaptive Strategy (Inventory-Aware)
- Quotes are skewed based on current inventory
- Reduces exposure as inventory grows
- Lower trading frequency, safer behavior

> Purpose: Demonstrate inventory risk management

---

### 3. Adaptive Strategy (Inventory + Order Book Imbalance)
- Inventory-aware skew
- Additional skew based on order book imbalance
- Avoids toxic order flow
- Most stable and robust strategy

> Purpose: Production-style market making

---

## Strategy Comparison Summary

| Strategy                        | Profitability     | Inventory Risk | Stability |
|---------------------------------|-------------------|----------------|-----------|
| Baseline                        | High (short-term) | High           | Low       |
| Adaptive (Inventory)            | Low–Medium        | Low            | High      |
| Adaptive (Inventory + Imbalance)| Medium            | Very Low       | Very High |

---

## Project Structure

```
Market_making_nubra/
│
├── core/                              # Core engine modules
│   ├── __init__.py
│   ├── market_data.py                 # Market data access via Nubra SDK
│   ├── orderbook.py                   # Order book wrapper & imbalance calc
│   ├── simulator.py                   # Paper-trade fill simulation
│   ├── pnl.py                         # PnL tracking (realized + unrealized)
│   ├── nubra_client.py                # Nubra SDK client wrapper
│   └── instruments.py                 # Instrument lookup service
│
├── strategies/                        # Trading strategies
│   ├── __init__.py
│   ├── base_strategy.py               # Baseline fixed-spread strategy
│   └── adaptive_strategy.py           # Inventory & imbalance aware strategy
│
├── utils/                             # Utility modules
│   ├── __init__.py
│   └── csv_logger.py                  # CSV logging for simulation data
│
├── analysis/                          # Visualization & analysis scripts
│   ├── __init__.py
│   ├── plot.py                        # Individual strategy plots
│   └── comparision_plot.py            # Cross-strategy comparison plots
│
├── data/                              # Simulation output data (CSV)
│   ├── baseline_strategy.csv
│   ├── adaptive_inventory.csv
│   └── adaptive_inventory_imbalance.csv
│
├── plots/                             # Generated plot images
│   ├── pnl_comparison.png.png
│   ├── inventory_comparison.png.png
│   └── ...
│
├── baseline_strategy_simulator.py     # Entry point: baseline strategy
├── adaptive_strategy_simulator.py     # Entry point: adaptive strategy
├── config.yaml                        # Configuration
├── credentials.env                    # Nubra credentials (git-ignored)
├── requirements.txt                   # Python dependencies
├── .gitignore
├── README.md
└── report.pdf                         # Analysis report
```

---

## Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Nubra credentials

Create a `credentials.env` file in the project root:

```env
NUBRA_ENV=uat
NUBRA_MOBILE=your_mobile
NUBRA_MPIN=your_mpin
```

> **Note:** This file is git-ignored and should never be committed to a public repository.

---

## Running the Strategies

### Baseline strategy
```bash
python baseline_strategy_simulator.py
```

### Adaptive strategy
```bash
python adaptive_strategy_simulator.py
```

---

## Visualization

After running the strategies, performance is compared using:
- **Total PnL vs Time**
- **Inventory vs Time**

Run analysis scripts from the project root:

```bash
python -m analysis.plot
python -m analysis.comparision_plot
```

All plots are generated from the CSV logs using matplotlib.

---

## Key Insights

- Baseline strategies may show higher short-term PnL but accumulate dangerous inventory risk.
- Inventory-aware strategies significantly reduce exposure.
- Incorporating order book imbalance improves robustness and stability.
- Sustainable market making prioritizes risk-adjusted returns, not raw PnL.

---

## Disclaimer

This project is for educational and research purposes only.  
No real trading or financial advice is implied.

---

## Acknowledgements

- Nubra Trading API & Python SDK
- Concepts from market microstructure and quantitative finance
