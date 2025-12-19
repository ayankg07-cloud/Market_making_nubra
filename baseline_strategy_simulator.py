import time
from nubra_python_sdk.start_sdk import InitNubraSdk, NubraEnv
from nubra_python_sdk.refdata.instruments import InstrumentData
from core.market_data import MarketDataService
from core.orderbook import OrderBookWrapper
from strategies.base_strategy import MarketMakingStrategy
from core.simulator import MarketSimulator
from core.pnl import PnLTracker
from utils.csv_logger import CSVLogger

nubra = InitNubraSdk(NubraEnv.UAT)

# Instrument lookup 
instruments = InstrumentData(nubra)
instrument = instruments.get_instrument_by_symbol("HDFCBANK", exchange="NSE")
ref_id = instrument.ref_id

print("Live simulation started for ref_id:", ref_id)

# Services
md = MarketDataService(nubra)
strategy = MarketMakingStrategy(spread_paise=20)

simulator = MarketSimulator(fill_probability=0.3)
pnl = PnLTracker()
logger = CSVLogger("data/baseline_strategy.csv")

while True:
    try:
        #Fetching LIVE orderbook
        raw_ob = md.get_orderbook(ref_id, levels=5)
        orderbook = OrderBookWrapper(raw_ob)

        best_bid = orderbook.best_bid()
        best_ask = orderbook.best_ask()
        mid = orderbook.mid_price()

        if not best_bid or not best_ask:
            time.sleep(1)
            continue

        #Compute strategy quotes
        bid, ask = strategy.compute_quotes(orderbook)

        #Simulate fills (paper trading)
        fills = simulator.simulate(
            bid,
            ask,
            best_bid=best_bid[0],
            best_ask=best_ask[0]
        )

        for side, price, qty in fills:
            
            pnl.on_fill(side, price, qty)
            print(f"FILL {side} ₹{price/100:.2f}")
        #loading data and division by 100 to convert paise
        logger.log(
            mid/100,
            bid/100 if bid is not None else None,
            ask/100 if ask is not None else None,
            pnl.inventory,
            pnl.realized/100,
            pnl.total_pnl(mid)/100
        )


        # Printing live stats
        print(
            f"Mid: ₹{mid/100:.2f} | "
            f"Inv: {pnl.inventory} | "
            f"Realized: ₹{pnl.realized/100:.2f} | "
            f"Total: ₹{pnl.total_pnl(mid)/100:.2f}"
        )

        time.sleep(1)  # control speed

    except KeyboardInterrupt:
        print("\nStopping live simulation...")
        logger.close()
        break

    except Exception as e:
        print("Error:", e)
        time.sleep(2)
