from nubra_python_sdk.refdata.instruments import InstrumentData

class InstrumentsService:
    def __init__(self, nubra_sdk):
        self.instruments = InstrumentData(nubra_sdk)

    def get_all_instruments_df(self):
        return self.instruments.get_instruments_dataframe()

    def get_by_symbol(self, symbol, exchange="NSE"):
        return self.instruments.get_instrument_by_symbol(symbol,exchange)
       
