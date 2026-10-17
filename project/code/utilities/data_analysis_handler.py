import pandas as pd

from pathlib import Path

# Stock price properties
def find_percentage_movement_in_range(
        start_index: int,
        end_index: int,
        source_file_path: Path
) -> float:

    parsed_data_set = find_data_in_range(
        start_index=start_index,
        end_index=end_index,
        source_file_path=source_file_path
    )

    close = parsed_data_set["Close"]

    percentage_movement_in_range = (close.iloc[0] - close.iloc[-1])/close.iloc[-1]
    return percentage_movement_in_range


 # Stock price analysis
def find_average_true_range_in_range(
    start_index: int,
    end_index: int,
    source_file_path: Path
) -> float:
    
    parsed_data_set = find_data_in_range(
        start_index=start_index,
        end_index=end_index + 1,
        source_file_path=source_file_path
    )

    high = parsed_data_set["High"]
    low = parsed_data_set["Low"]
    close = parsed_data_set["Close"]

    previous_close = close.shift(-1)

    true_range = pd.concat(
        [
            high - low,
            abs(high - previous_close),
            abs(low - previous_close)
        ],
        axis=1
        ).max(axis=1)

    average_true_range = true_range.iloc[:-1].mean()
    return float(average_true_range)

def find_max_price_in_range(
    start_index: int,
    end_index: int,
    source_file_path: Path
) -> float:

    parsed_data_set = find_data_in_range(
        start_index=start_index,
        end_index=end_index,
        source_file_path=source_file_path
    )

    high = parsed_data_set["High"]

    max_price = high.max()
    return float(max_price)

def find_percentage_from_max_price_in_range(
        start_index: int,
        end_index: int,
        source_file_path: Path
) -> float:

    parsed_data_set = find_data_in_range(
        start_index=start_index,
        end_index=end_index,
        source_file_path=source_file_path
    )

    high = parsed_data_set["High"]
    close = parsed_data_set["Close"]

    percentage_movement_in_range = (close.iloc[0] - high.max())/high.max()
    return percentage_movement_in_range

def find_risk_adjusted_position_size(
    portfolio_risk_limit: float,
    position_risk: float,
    position_size_limit: float
) -> float:
    
    risk_adjusted_position_size = min(
        position_size_limit,
        portfolio_risk_limit/position_risk
    )
    return risk_adjusted_position_size


# Utilities
def find_data_in_range(
    start_index: int,
    end_index: int,
    source_file_path: Path
) -> pd.DataFrame:

    raw_data_set = pd.read_csv(source_file_path)
    inverted_data_set = raw_data_set[::-1].reset_index(drop=True)
    parsed_data_set = inverted_data_set.iloc[start_index: end_index + 1]
    return parsed_data_set