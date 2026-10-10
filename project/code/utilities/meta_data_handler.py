import csv
import math
import pandas as pd
import yfinance as yf

import utilities.config as cnf
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
        self.buy_order_placed_trigger: Optional[float] = None
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
        self.open_average_true_range: Optional[float] = None
        self.open_max_price: Optional[float] = None
        self.open_risk_adjusted_position_size: Optional[float] = None
        # Utilities 
        self.entry_directory_path: Path = entry_directory_path

        
    # Set buy order placed properties
    def set_buy_order_placed_date(
        self,
        buy_order_placed_date: str
    ) -> None:
        
        self.buy_order_placed_date = buy_order_placed_date
    
    
    def set_buy_order_placed_trigger(
        self
    ) -> None:

        if self.open_average_true_range is None:
            raise ValueError("open_average_true_range is not initialized")

        if self.open_max_price is None:
            raise ValueError("open_max_price is not initialized")

        self.buy_order_placed_trigger = self.open_max_price + self.open_average_true_range*cnf.BUY_ORDER_SCALING_FACTOR

    
    def set_buy_order_placed_quantity(
        self,
        portfolio_size: float
    ) -> None:

        if self.buy_order_placed_trigger is None:
            raise ValueError("buy_order_placed_trigger is not initialized")

        if self.open_risk_adjusted_position_size is None:
            raise ValueError("open_risk_adjusted_position_size is not initialized")
        
        self.buy_order_placed_quantity = math.trunc(portfolio_size*self.open_risk_adjusted_position_size/self.buy_order_placed_trigger)
        

    # Set buy order filled properties
    #def set_buy_order_filled_date() -> None:
    #def set_buy_order_filled_price() -> None:
    #def set_buy_order_filled_quantity() -> None:
    #def set_buy_order_filled_fees() -> None:
    # Set trailing stop placed properties
    #def set_trailing_stop_placed_date() -> None:


    def set_trailing_stop_placed_trigger(
        self
    ) -> None:

        if self.buy_order_placed_trigger is None:
            raise ValueError("buy_order_placed_trigger is not initialized")

        if self.open_average_true_range is None:
            raise ValueError("open_average_true_range is not initialized")

        self.trailing_stop_placed_trigger = self.open_average_true_range*cnf.TRAILING_STOP_SCALING_FACTOR/self.buy_order_placed_trigger


    def set_trailing_stop_placed_quantity(
        self
    ) -> None:

        if self.buy_order_filled_quantity is None:
            raise ValueError("buy_order_filled_quantity is not initialized")
    
        self.trailing_stop_placed_quantity = self.buy_order_filled_quantity

    # Set trailing stop filled properties
    #def set_trailing_stop_filled_date() -> None:
    #def set_trailing_stop_filled_price() -> None:
    #def set_trailing_stop_filled_quantity() -> None:
    #def set_trailing_stop_filled_fee() -> None:
    # Analysis
    def set_open_average_true_range(
        self
    ) -> None:
        
        self.open_average_true_range = dah.find_average_true_range(
            period=cnf.AVERAGE_TRUE_RANGE_PERIODE,
            source_file_path=self.get_raw_open_file_path()
        )


    def set_open_max_price(
        self
    ) -> None:
        
        self.open_max_price = dah.find_max_price(
            period=cnf.MAX_PRICE_PERIODE,
            source_file_path=self.get_raw_open_file_path()
        )


    def set_open_risk_adjusted_position_size(
        self
    ) -> None:

        if self.trailing_stop_placed_trigger is None:
            raise ValueError("trailing_stop_placed_trigger is not initialized")

        self.open_risk_adjusted_position_size = dah.find_risk_adjusted_position_size(
            portfolio_risk_limit=cnf.PORTFOLIO_RISK_LIMIT,
            position_risk=self.trailing_stop_placed_trigger,
            position_size_limit=cnf.POSITION_SIZE_LIMIT
        )


    # Utilities 
    def get_raw_open_file_path(
        self,
    ) -> Path:
        
        raw_open_file_path = self.entry_directory_path/"raw"/f"{self.ticker_symbol}_{self.trade_open_date}_open.csv"

        return raw_open_file_path


    def get_raw_update_file_path(    
        self,
        action_date: str
    ) -> Path:
        
        raw_update_file_path = self.entry_directory_path/"raw"/f"{self.ticker_symbol}_{action_date}_update.csv"

        return raw_update_file_path


    def get_raw_close_file_path(
            self,
        ) -> Path:

        if self.trade_close_date is None:
            raise ValueError("trade_close_date is not initialized")
        
        raw_close_file_path = self.entry_directory_path/"raw"/f"{self.ticker_symbol}_{self.trade_close_date}_close.csv"

        return raw_close_file_path
    


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
            "buy_order_placed_trigger",
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
        