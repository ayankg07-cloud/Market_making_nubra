class MarketMakingStrategy:
    def __init__(self, spread_paise=20):
       
        self.spread=spread_paise

    def compute_quotes(self, orderbook):
      
        mid=orderbook.mid_price()

        if mid is None:
            return None, None

        half_spread=self.spread//2

        bid_price=mid-half_spread
        ask_price=mid+half_spread

        return bid_price, ask_price
