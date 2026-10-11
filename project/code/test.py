import utilities as utl
import pandas as pd
from pathlib import Path


# Project directory paths 
TEST_DIRECTORY_PATH: Path = (Path(__file__).resolve().parent.parent)/"test"
TEST_FILE_PATH: Path = TEST_DIRECTORY_PATH/"price_data.csv"

# test 1 (new_file_name=f"{ticker_symbol}_{entry_open_date}_{action}.csv")
ticker_symbol:str = "603588.SS"
price_data_file_path: Path = utl.make_file(
    target_directory_path=TEST_DIRECTORY_PATH,
    new_file_name=f"261011_{ticker_symbol}_open.csv"
    )
utl.download_price_data_to_csv(
    ticker_symbol=ticker_symbol,
    period="1y",
    interval="1d",
    target_file_path=price_data_file_path)

# test 2 
#full_data = pd.read_csv(TEST_FILE_PATH)
#periode_data = full_data.tail(14)
#
#close = periode_data.get("Close")
#high = periode_data.get("High")
#low = periode_data.get("Low")
#
#print(close)
#print(close.shift(-1))

# test 3 
#atr: float = utl.find_average_true_range(14, TEST_FILE_PATH)
#print(atr)

