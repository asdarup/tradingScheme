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
        company_name: str,
        ticker_symbol: str,
        sector: str,
        entry_open_date: str,
        entry_directory_path: Path
    ) -> None:

        # portfilio properties
        self.portfolio_size: Optional[float] = None
        self.portfolio_risk_limit: float = cnf.PORTFOLIO_RISK_LIMIT
        self.position_size_limit: float = cnf.POSITION_SIZE_LIMIT

        # Stock properties
        self.company_name: str = company_name
        self.ticker_symbol: str = ticker_symbol
        self.sector: str = sector
        self.market_capitalization: Optional[float] = None
        self.earnings_date: Optional[str] = None

        # Stock price patern properties
        self.pattern_this_q: Optional[str] = None
        self.pattern_earnings_w: Optional[str] = None
        self.pattern_earnings_w_minus_1: Optional[str] = None
        self.pattern_earnings_w_minus_2: Optional[str] = None
        self.percentage_depth_of_q_pattern: Optional[float] = None
        self.percentage_depth_of_earnings_w_pattern: Optional[float] = None
        self.percentage_depth_of_earnings_w_minus_1_pattern: Optional[float] = None
        self.percentage_depth_of_earnings_w_minus_2_pattern: Optional[float] = None
        self.percentage_movement_of_q_pattern: Optional[float] = None
        self.percentage_movement_of_earnings_w_pattern: Optional[float] = None
        self.percentage_movement_of_earnings_w_minus_1_pattern: Optional[float] = None
        self.percentage_movement_of_earnings_w_minus_2_pattern: Optional[float] = None

        # Stock price properties
        self.percentage_increase_this_q: Optional[float] = None
        self.percentage_increase_this_q_minus_1: Optional[float] = None
        self.percentage_increase_this_q_minus_2: Optional[float] = None
        self.percentage_increase_after_earnings_q_minus_1: Optional[float] = None
        self.percentage_increase_after_earnings_q_minus_2: Optional[float] = None

        # Stock price analysis
        self.average_true_range: Optional[float] = None
        self.period_max_price: Optional[float] = None
        self.q_max_price: Optional[float] = None
        self.percentage_from_period_max_price: Optional[float] = None
        self.percentage_from_q_max_price: Optional[float] = None
        self.risk_adjusted_position_size: Optional[float] = None

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

        # Lifecycle properties
        self.entry_open_date: str = entry_open_date
        self.entry_triggered: Optional[bool] = None
        self.entry_close_date: Optional[str] = None

        # profit loss properties
        self.realized_profit_loss_price: Optional[float] = None
        self.realized_profit_loss_percent: Optional[float] = None
        self.trade_duration_days: Optional[int] = None

        # Utilities 
        self.entry_directory_path: Path = entry_directory_path

    # portfilio properties
    def set_portfolio_size(
        self,
        portfolio_size
    ) -> None:
        
        self.portfolio_size = portfolio_size 

        
    # Stock properties
    def set_market_capitalization(
        self
    ) -> None:
        
        
    # def set_earnings_date(
    #     self
    # ) -> None:

        
    # Stock price patern properties
    # def set_pattern_this_q(
    #     self
    # ) -> None:
        
    # def set_pattern_earnings_w(
    #     self
    # ) -> None:
        
    # def set_pattern_earnings_w_minus_1(
    #     self
    # ) -> None:
        
    # def set_pattern_earnings_w_minus_2(
    #     self
    # ) -> None:
        
    # def set_percentage_depth_of_q_pattern(
    #     self
    # ) -> None:
        
    # def set_percentage_depth_of_earnings_w_pattern(
    #     self
    # ) -> None:
        
    # def set_percentage_depth_of_earnings_w_minus_1_pattern(
    #     self
    # ) -> None:
        
    # def set_percentage_depth_of_earnings_w_minus_2_pattern(
    #     self
    # ) -> None:
        
    # def set_percentage_movement_of_q_pattern(
    #     self
    # ) -> None:
        
    # def set_percentage_movement_of_earnings_w_pattern(
    #     self
    # ) -> None:
        
    # def set_percentage_movement_of_earnings_w_minus_1_pattern(
    #     self
    # ) -> None:
        
    # def set_percentage_movement_of_earnings_w_minus_2_pattern(
    #     self
    # ) -> None:

        
    # Stock price properties
    # def set_percentage_increase_this_q(
    #     self
    # ) -> None:
        
    # def set_percentage_increase_this_q_minus_1(
    #     self
    # ) -> None:
        
    # def set_percentage_increase_this_q_minus_2(
    #     self
    # ) -> None:
        
    # def set_percentage_increase_after_earnings_q_minus_1(
    #     self
    # ) -> None:
        
    # def set_percentage_increase_after_earnings_q_minus_2(
    #     self
    # ) -> None:
        
    # def set_percentage_increase_after_earnings_q_minus_3(
    #     self
    # ) -> None:

        
    # Stock price analysis
    def set_average_true_range(
        self
    ) -> None:
        
        self.average_true_range = dah.find_average_true_range(
            period=cnf.AVERAGE_TRUE_RANGE_PERIODE,
            source_file_path=self.get_raw_open_file_path()
        )
        
    def set_periode_max_price(
        self
    ) -> None:
        
        self.period_max_price = dah.find_max_price(
            period=cnf.PERIOD_MAX_PRICE_PERIOD,
            source_file_path=self.get_raw_open_file_path()
        )
        
    def set_q_max_price(
        self
    ) -> None:
        
        self.max_price = dah.find_max_price(
            period=cnf.Q_MAX_PRICE_PERIOD,
            source_file_path=self.get_raw_open_file_path()
        )

    # def set_percentage_from_period_max_price(
    #     self
    # ) -> None:  

    # def set_percentage_from_q_max_price(
    #     self
    # ) -> None:
        
    def set_risk_adjusted_position_size(
        self
    ) -> None:

        if self.trailing_stop_placed_trigger is None:
            raise ValueError("trailing_stop_placed_trigger is not initialized")

        self.risk_adjusted_position_size = dah.find_risk_adjusted_position_size(
            portfolio_risk_limit=cnf.PORTFOLIO_RISK_LIMIT,
            position_risk=self.trailing_stop_placed_trigger,
            position_size_limit=cnf.POSITION_SIZE_LIMIT
        )

        
    # Buy order placed properties
    def set_buy_order_placed_date(
        self,
        buy_order_placed_date: str
    ) -> None:
        
        self.buy_order_placed_date = buy_order_placed_date
        
    def set_buy_order_placed_trigger(
        self
    ) -> None:

        if self.average_true_range is None:
            raise ValueError("average_true_range is not initialized")
        if self.max_price is None:
            raise ValueError("max_price is not initialized")

        self.buy_order_placed_trigger = self.max_price + self.average_true_range*cnf.BUY_ORDER_SCALING_FACTOR
        
    def set_buy_order_placed_quantity(
        self,
    ) -> None:

        if self.portfolio_size is None:
            raise ValueError("portfolio_size is not initialized")
        if self.buy_order_placed_trigger is None:
            raise ValueError("buy_order_placed_trigger is not initialized")
        if self.risk_adjusted_position_size is None:
            raise ValueError("risk_adjusted_position_size is not initialized")
        
        self.buy_order_placed_quantity = math.trunc(self.portfolio_size*self.risk_adjusted_position_size/self.buy_order_placed_trigger)

        
    # Buy order filled properties
    # def set_buy_order_filled_date(
    #     self
    # ) -> None:
        
    # def set_buy_order_filled_price(
    #     self
    # ) -> None:
        
    # def set_buy_order_filled_quantity(
    #     self
    # ) -> None:
        
    # def set_buy_order_filled_fees(
    #     self
    # ) -> None:

        
    # Trailing stop placed properties
    # def set_trailing_stop_placed_date(
    #     self
    # ) -> None:
        
    def set_trailing_stop_placed_trigger(
        self
    ) -> None:

        if self.buy_order_placed_trigger is None:
            raise ValueError("buy_order_placed_trigger is not initialized")
        if self.average_true_range is None:
            raise ValueError("average_true_range is not initialized")

        self.trailing_stop_placed_trigger = self.average_true_range*cnf.TRAILING_STOP_SCALING_FACTOR/self.buy_order_placed_trigger
        
    def set_trailing_stop_placed_quantity(
        self
    ) -> None:

        if self.buy_order_filled_quantity is None:
            raise ValueError("buy_order_filled_quantity is not initialized")
    
        self.trailing_stop_placed_quantity = self.buy_order_filled_quantity

        
    # Trailing stop filled properties
    # def set_trailing_stop_filled_date(
    #     self
    # ) -> None:
        
    # def set_trailing_stop_filled_price(
    #     self
    # ) -> None:
        
    # def set_trailing_stop_filled_quantity(
    #     self
    # ) -> None:
        
    # def set_trailing_stop_filled_fees(
    #     self
    # ) -> None:

        
    # Lifecycle properties
    # def set_entry_close_date(
    #     self
    # ) -> None:

        
    # profit loss properties
    # def set_realized_profit_loss_price(
    #     self
    # ) -> None:
        
    # def set_realized_profit_loss_percent(
    #     self
    # ) -> None:
        
    # def set_trade_duration_days(
    #     self
    # ) -> None:

        
    # Utilities 
    def get_raw_open_file_path(
        self,
    ) -> Path:
        
        raw_open_file_path = self.entry_directory_path/"raw"/f"{self.ticker_symbol}_{self.entry_open_date}_open.csv"
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

        if self.entry_close_date is None:
            raise ValueError("entry_close_date is not initialized")
        
        raw_close_file_path = self.entry_directory_path/"raw"/f"{self.ticker_symbol}_{self.entry_close_date}_close.csv"
        return raw_close_file_path







# Functions 
def write_meta_file(
    meta_data: Meta_Data,
    meta_file_path: Path
) -> None:
    """
    Write data to the file at "meta_file_path"
    """
    with open(
        file=meta_file_path,
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        # Write header row
        writer.writerow([
            # portfilio properties
            "portfolio_size",
            "portfolio_risk_limit",
            "position_size_limit",
            
            # Stock properties
            "company_name",
            "ticker_symbol",
            "sector",
            "market_capitalization",
            "earnings_date",
            
            # Stock price patern properties
            "pattern_this_q",
            "pattern_earnings_w",
            "pattern_earnings_w_minus_1",
            "pattern_earnings_w_minus_2",
            "percentage_depth_of_q_pattern",
            "percentage_depth_of_earnings_w_pattern",
            "percentage_depth_of_earnings_w_minus_1_pattern",
            "percentage_depth_of_earnings_w_minus_2_pattern",
            "percentage_movement_of_q_pattern",
            "percentage_movement_of_earnings_w_pattern",
            "percentage_movement_of_earnings_w_minus_1_pattern",
            "percentage_movement_of_earnings_w_minus_2_pattern",
            
            
            # Stock price properties
            "percentage_increase_this_q",
            "percentage_increase_this_q_minus_1",
            "percentage_increase_this_q_minus_2",
            "percentage_increase_after_earnings_q_minus_1",
            "percentage_increase_after_earnings_q_minus_2",
            
            # Stock price analysis
            "average_true_range",
            "period_max_price",
            "q_max_price",
            "percentage_from_period_max_price",
            "percentage_from_q_max_price",
            "risk_adjusted_position_size",
            
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
            "trailing_stop_filled_fees",
            
            # Lifecycle properties
            "entry_open_date",
            "entry_triggered",
            "entry_close_date",
            
            # profit loss properties
            "realized_profit_loss_price",
            "realized_profit_loss_percent",
            "trade_duration_days"
        ])

        # Write data row
        writer.writerow([
            # portfilio properties
            meta_data.portfolio_size,
            meta_data.portfolio_risk_limit,
            meta_data.position_size_limit,

            # Stock properties
            meta_data.company_name,
            meta_data.ticker_symbol,
            meta_data.sector,
            meta_data.market_capitalization,
            meta_data.earnings_date,

            # Stock price patern properties
            meta_data.pattern_this_q,
            meta_data.pattern_earnings_w,
            meta_data.pattern_earnings_w_minus_1,
            meta_data.pattern_earnings_w_minus_2,
            meta_data.percentage_depth_of_q_pattern,
            meta_data.percentage_depth_of_earnings_w_pattern,
            meta_data.percentage_depth_of_earnings_w_minus_1_pattern,
            meta_data.percentage_depth_of_earnings_w_minus_2_pattern,
            meta_data.percentage_movement_of_q_pattern,
            meta_data.percentage_movement_of_earnings_w_pattern,
            meta_data.percentage_movement_of_earnings_w_minus_1_pattern,
            meta_data.percentage_movement_of_earnings_w_minus_2_pattern,


            # Stock price properties
            meta_data.percentage_increase_this_q,
            meta_data.percentage_increase_this_q_minus_1,
            meta_data.percentage_increase_this_q_minus_2,
            meta_data.percentage_increase_after_earnings_q_minus_1,
            meta_data.percentage_increase_after_earnings_q_minus_2,

            # Stock price analysis
            meta_data.average_true_range,
            meta_data.period_max_price,
            meta_data.percentage_from_period_max_price,
            meta_data.q_max_price,
            meta_data.percentage_from_q_max_price,
            meta_data.risk_adjusted_position_size,

            # Buy order placed properties
            meta_data.buy_order_placed_date,
            meta_data.buy_order_placed_trigger,
            meta_data.buy_order_placed_quantity,

            # Buy order filled properties
            meta_data.buy_order_filled_date,
            meta_data.buy_order_filled_price,
            meta_data.buy_order_filled_quantity,
            meta_data.buy_order_filled_fees,

            # Trailing stop placed properties
            meta_data.trailing_stop_placed_date,
            meta_data.trailing_stop_placed_trigger,
            meta_data.trailing_stop_placed_quantity,

            # Trailing stop filled properties
            meta_data.trailing_stop_filled_date,
            meta_data.trailing_stop_filled_price,
            meta_data.trailing_stop_filled_quantity,
            meta_data.trailing_stop_filled_fees,

            # Lifecycle properties
            meta_data.entry_open_date,
            meta_data.entry_triggered,
            meta_data.entry_close_date,

            # profit loss properties
            meta_data.realized_profit_loss_price,
            meta_data.realized_profit_loss_percent,
            meta_data.trade_duration_days
        ])

