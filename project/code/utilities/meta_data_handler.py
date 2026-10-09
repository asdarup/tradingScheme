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
        trade_initialization_date: str,
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
        self.trade_initialization_date: str = trade_initialization_date
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
    def set_opening_average_true_range(self, periode) -> float:
        opening_raw_file_path: Path = self.entry_directory_path/"raw"/f"{self.ticker_symbol}_{self.trade_initialization_date}_open"
        

# Functions 
def download_price_data_to_csv(
    ticker_symbol: str,
    period: str,
    interval: str,
    target_file_path: Path
) -> None:
    """
    Download price data from Yahoo Finance and write that data to a .csv file at "target_file_path"
    """

    if target_file_path.suffix != ".csv":
        raise ValueError(f"{target_file_path.name} is not .csv file")

    data = yf.download(
        tickers=ticker_symbol, 
        period=period, 
        interval=interval
    )

    # period="1m"     interval="1m"     1 minute
    # period="2m"     interval="2m"     2 minutes
    # period="5m"     interval="5m"     5 minutes
    # period="15m"    interval="15m"    15 minutes
    # period="30m"    interval="30m"    30 minutes
    # period="60m"    interval="60m"    1 hour
    # period="1d"     interval="1d"     1 day
    # period="5d"     interval="5d"     5 days
    # period="1wk"    interval="1wk"    1 week
    # period="1mo"    interval="1mo"    1 month
    # period="3mo"    interval="3mo"    3 months

    data.columns = data.columns.get_level_values(0)

    data.to_csv(target_file_path)


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
        