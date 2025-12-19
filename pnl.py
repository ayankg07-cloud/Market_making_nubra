class PnLTracker:
    def __init__(self):
        self.inventory = 0
        self.avg_price = 0.0  # paise
        self.realized = 0.0  # paise

    def on_fill(self, side, price, qty):
        if side == "BUY":
            if self.inventory >= 0:
                # increasing long
                total_cost=self.avg_price*self.inventory+price*qty
                self.inventory+=qty
                self.avg_price=total_cost/self.inventory
            else:
                # covering short
                closing_qty=min(qty,abs(self.inventory))
                self.realized+=(self.avg_price - price)*closing_qty
                self.inventory+=closing_qty
                if self.inventory==0:
                    self.avg_price=0.0

        elif side == "SELL":
            if self.inventory <= 0:
                # increasing short
                total_cost=self.avg_price*abs(self.inventory)+price*qty
                self.inventory-=qty
                self.avg_price=total_cost/abs(self.inventory)
            else:
                # closing long
                closing_qty=min(qty, self.inventory)
                self.realized+=(price-self.avg_price)*closing_qty
                self.inventory-=closing_qty
                if self.inventory==0:
                    self.avg_price=0.0

    def unrealized(self,mid_price):
        if self.inventory==0:
            return 0.0
        return (mid_price-self.avg_price)*self.inventory

    def total_pnl(self,mid_price):
        return self.realized+self.unrealized(mid_price)
