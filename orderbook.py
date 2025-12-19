class OrderBookWrapper:
    def __init__(self, orderbook):
        self.ob =orderbook   

    def best_bid(self):
        if not self.ob.bid:
            return None
        b = self.ob.bid[0]
        return b.price, b.quantity, b.num_orders

    def best_ask(self):
        if not self.ob.ask:
            return None
        a = self.ob.ask[0]
        return a.price, a.quantity, a.num_orders

    def mid_price(self):
        bid=self.best_bid()
        ask=self.best_ask()
        if not bid or not ask:
            return None
        return (bid[0] + ask[0])/2

    def imbalance(self, levels=5):
        bid_qty=sum(l.quantity for l in self.ob.bid[:levels])
        ask_qty=sum(l.quantity for l in self.ob.ask[:levels])

        total=bid_qty+ask_qty
        if total==0:
            return 0.0

        return (bid_qty-ask_qty)/total
