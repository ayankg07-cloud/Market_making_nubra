class InventoryAwareMarketMaker:
    def __init__(self,spread_paise,skew_factor,max_inventory=50,imbalance_factor=10):
        self.spread=spread_paise
        self.skew_factor=skew_factor
        self.max_inventory=max_inventory
        self.imbalance_factor=imbalance_factor
        self.inventory=0

    def update_inventory(self,qty,side):
        if side == "BUY":
            self.inventory += qty
        elif side == "SELL":
            self.inventory -= qty

    def compute_quotes(self,orderbook):
        mid = orderbook.mid_price()
        if mid is None:
            return None, None

        half_spread=self.spread // 2
        inv_skew=-self.skew_factor*self.inventory#inventory skew
        imb=orderbook.imbalance(levels=5)#using depth=5 of orderbook
        imb_skew=self.imbalance_factor*imb#imbalance skew
        # Inventory-based directional skew
        bid=mid-half_spread+inv_skew+imb_skew
        ask=mid+half_spread+inv_skew-imb_skew

        # if maximum inventory limit crosses
        if self.inventory>=self.max_inventory:
            bid=None
        if self.inventory<=-self.max_inventory:
            ask=None

        return (
            int(bid) if bid is not None else None,
            int(ask) if ask is not None else None
        )

