import pandas as pd

from pathlib import Path

def find_average_true_range(
    period: int,
    source_file_path: Path
) -> float:
    
    full_data = pd.read_csv(source_file_path)
    period_data = full_data.tail(period + 1)

    close = period_data["Close"]
    high = period_data["High"]
    low = period_data["Low"]

    previous_close = close.shift(1)

    true_range = pd.concat(
        [
            high - low,
            abs(high - previous_close),
            abs(low - previous_close)
        ],
        axis=1
        ).max(axis=1)

    average_true_range = true_range.mean()

    return float(average_true_range)


def find_max_price(
    period: int,
    source_file_path: Path
) -> float:

    full_data = pd.read_csv(source_file_path)
    periode_data = full_data.tail(period)

    high = periode_data["High"]

    max_price = high.max()

    return float(max_price)
    