import csv
import os
from datetime import datetime

class CSVLogger:
    def __init__(self,filepath):
        self.filepath=filepath
        self.file_exists = os.path.exists(filepath)

        self.file = open(filepath, "a", newline="")
        self.writer = csv.writer(self.file)

        if not self.file_exists:
            self.writer.writerow([
                "timestamp",
                "mid_price",
                "bid_price",
                "ask_price",
                "inventory",
                "realized_pnl",
                "total_pnl"
            ])
            self.file.flush()

    def log(self, mid, bid, ask, inventory, realized, total):
        self.writer.writerow([
            datetime.now().isoformat(),
            mid,
            bid,
            ask,
            inventory,
            realized,
            total
        ])
        self.file.flush()

    def close(self):
        self.file.close()
