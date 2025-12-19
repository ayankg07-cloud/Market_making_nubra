import random

class MarketSimulator:
    def __init__(self, fill_probability=0.3, qty=1):#taking a probability to simulate the market
        self.fill_probability=fill_probability
        self.qty=qty

    def simulate(self,bid,ask,best_bid,best_ask):
        if random.random()>self.fill_probability:
            return []

        # Decide which side gets hit by random probabilistic model
        if bid is not None and ask is not None:
            side = random.choice(["BUY", "SELL"])
        elif bid is not None:
            side = "BUY"
        elif ask is not None:
            side = "SELL"
        else:
            return []
        
        #using market data to simulate trade
        if side=="BUY"and bid>=best_bid:
            return [("BUY", bid, self.qty)]
        if side == "SELL" and ask <= best_ask:
            return [("SELL", ask, self.qty)]

        return []
