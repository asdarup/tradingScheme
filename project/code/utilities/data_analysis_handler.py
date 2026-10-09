import pandas as pd

from pathlib import Path

def find_average_true_range(
    period: int,
    source_file_path: Path
) -> float:
    
    full_data = pd.read_csv(source_file_path)
    periode_data = full_data.tail(period + 1)

    close = periode_data.get("Close")
    high = periode_data.get("High")
    low = periode_data.get("Low")

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