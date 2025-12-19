from nubra_python_sdk.marketdata.market_data import MarketData

class MarketDataService:
    def __init__(self, nubra_sdk):
        self.md = MarketData(nubra_sdk)

    def get_orderbook(self,ref_id,levels=5):
        
        quote=self.md.quote(ref_id,levels)
        return quote.orderBook
