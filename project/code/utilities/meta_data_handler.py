import csv 
import pandas as pd
import yfinance as yf

import utilities.data_analysis_handler as dah

from pathlib import Path
from typing import Optional

# Classes
class Meta_Data:
    """
    
    """
    def __init__(
        self,
        ticker_symbol: str,
        sector: str,
        trade_open_date: str,
        entry_directory_path: Path
    ) -> None:

        # Stock properties
        self.ticker_symbol: str = ticker_symbol
        self.sector: str = sector
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
        self.trailing_stop_filled_fees: Optional[float] = None
        # Lifecycle 
        self.trade_open_date: str = trade_open_date
        self.trade_update_dates: list[str] = []
        self.trade_close_date: Optional[str] = None
        # Analysis
        self.opening_average_true_range: Optional[float] = None
        # Utilities 
        self.entry_directory_path: Path = entry_directory_path

        
    # Set buy order placed properties
    #def set_buy_order_placed_date() -> None:
    #def set_buy_order_placed_price(self, max_price_periode: int, scaling_factor: float) -> None:
    #    average_true_range = 
    #    buy_order_placed_price = max_price_periode
    #
    #
    #def set_buy_order_placed_quantity() -> None:self.ticker_symbol: str = ticker_symbol
    #    self.sector: str = sector
    #    self.trade_initialization_date = trade_initia
    # Set buy order filled properties
    #def set_buy_order_filled_date() -> None:
    #def set_buy_order_filled_price() -> None:
    #def set_buy_order_filled_quantity() -> None:
    #def set_buy_order_filled_fees() -> None:
    # Set trailing stop placed properties
    #def set_trailing_stop_placed_date() -> None:
    #def set_trailing_stop_placed_trigger() -> None:
    #def set_trailing_stop_placed_quantity() -> None:
    # Set trailing stop filled properties
    #def set_trailing_stop_filled_date() -> None:
    #def set_trailing_stop_filled_price() -> None:
    #def set_trailing_stop_filled_quantity() -> None:
    #def set_trailing_stop_filled_fee() -> None:
    # Analysis
    def set_average_true_range(
        self,
        period: int,
        source_file_path: Path
    ) -> None:
        
        self.opening_average_true_range = dah.find_average_true_range(
            period=period,
            source_file_path=source_file_path
        )


    # Utilities 
    def get_raw_open_file_path(
        self,
    ) -> Path:
        
        return (
            self.entry_directory_path
            / "raw"
            / f"{self.ticker_symbol}_{self.trade_open_date}_open.csv"
        )


    def get_raw_update_file_path(    
        self,
        action_date: str
    ) -> Path:
        
        return (
            self.entry_directory_path
            / "raw"
            / f"{self.ticker_symbol}_{action_date}_update.csv"
        )


    def get_raw_close_file_path(
            self,
        ) -> Path:
        
        return (
            self.entry_directory_path
            / "raw"
            / f"{self.ticker_symbol}_{self.trade_open_date}_open.csv"
        )
    


# Functions 
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
        