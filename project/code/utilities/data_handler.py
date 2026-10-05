import csv

from pathlib import Path
from typing import Optional


class Meta_Data:
    """
    
    """
    def __init__(
        self, 
        ticker_symbol: str,
        sector: str,
        trade_initialization_date: str
    ) -> None:
        
        # Stock properties
        self.ticker_symbol: str = ticker_symbol
        self.sector: str = sector
        self.trade_initialization_date = trade_initialization_date
        # Buy order placed properties
        self.buy_order_placed_date: Optional[str] = None
        self.buy_order_placed_price: Optional[float] = None
        self.buy_order_placed_quantity: Optional[int] = None
        # Buy order filled properties
        self.buy_order_filled_date: Optional[str] = None
        self.buy_order_filled_price: Optional[float] = None
        self.buy_order_filled_quantity: Optional[int] = None
        self.buy_order_filled_fees: Optional[float] = None
        # Trailing stop placed properties
        self.trailing_stop_placed_date: Optional[str] = None
        self.trailing_stop_placed_trigger: Optional[float] = None
        self.trailing_stop_placed_quantity: Optional[int] = None
        # Trailing stop filled properties
        self.trailing_stop_filled_date: Optional[str] = None
        self.trailing_stop_filled_price: Optional[float] = None
        self.trailing_stop_filled_quantity: Optional[int] = None
        self.trailing_stop_filled_fee: Optional[float] = None

    # def set_buy_order_placed_date
    # def buy_order_placed_price

    



def initialize_meta_file(
    meta_file_path: Path
) -> None:
    """
    Initialize the file at "meta_file_path"
    """
    with open(
        file=meta_file_path,
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            # Stock properties
            "ticker_symbol",
            "sector",
            "initialization_date",
            # Buy order placed properties
            "buy_order_placed_date",
            "buy_order_placed_price",
            "buy_order_placed_quantity",
            # Buy order filled properties
            "buy_order_filled_date",
            "buy_order_filled_price",
            "buy_order_filled_quantity",
            "buy_order_filled_fees",
            # Trailing stop placed properties
            "trailing_stop_placed_date",
            "trailing_stop_placed_trigger",
            "trailing_stop_placed_quantity",
            # Trailing stop filled properties
            "trailing_stop_filled_date",
            "trailing_stop_filled_price",
            "trailing_stop_filled_quantity",
            "trailing_stop_filled_fees"
        ])

def write_meta_file(
    meta_file_path: Path,
    meta_data: Meta_Data
) -> None:
    """
    Write data to the file at "meta_file_path"
    """
        