
import yfinance as yf 
import pandas as pd 

from pathlib import Path
from shutil import move


def download_price_data_to_csv(
    ticker_symbol: str,
    period: str,
    interval: str,
    file_path: Path
) -> None:
    """
    Download price data from Yahoo Finance and write that data to a .csv file at "file_path"
    """

    if file_path.suffix != ".csv":
        raise ValueError(f"{file_path.name} is not .csv file")

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

    print(data)

    data.to_csv(file_path)


def make_directory(
    base_directory_path: Path,
    new_directory_name: str
) -> Path:
    """
    Create a new directory, "new_directory_name", at "base_directory_path"
    return new directory path 
    """
    new_directory_path = base_directory_path/new_directory_name

    new_directory_path.mkdir(exist_ok=False)

    return new_directory_path


def make_file(
        base_directory_path: Path,
        new_file_name: str
) -> Path:
    """
    Create a new file, "new_file_name", at "base_directory_path"
    return file path
    """
    new_file_path = base_directory_path/new_file_name

    new_file_path.touch(exist_ok=False)

    return new_file_path






























def get_csv_file_path(
    base_directory_path: Path
) -> Path:
    """
    Get the file path of a .cvs file at "base_directory_path"
    if any → return file path
    if not → raise "FileNotFoundError" 
    """
    file_path = next(base_directory_path.glob("*.csv"), None)

    if file_path is None:
        raise FileNotFoundError(f"No .csv file found in {base_directory_path}")

    return file_path


def has_csv_file(
    base_directory_path: Path
) -> bool:
    """
    Check if there are .csv files at "base_directory_path"
    if any → return True 
    if not → return False
    """
    return any(base_directory_path.glob("*.csv"))


def move_file(
    old_file_path: Path,
    new_directory_path: Path
) -> Path:
    """ 
    Move the file at "old_file_path" to "new_directory_path"
    return new file path
    """
    new_file_path = new_directory_path/f"{old_file_path.name}"

    move(old_file_path, new_file_path)

    return new_file_path


def parse_file_stem(
    file_path: Path
) -> dict[str, str]:
    """
    Parse filename, from [symbol_date_action] to [symbol], [date] and [action] 
    if format good → return parts in a dictionary 
    if format bad  → raise "ValueError"
    """
    parts = file_path.stem.split("_")

    if len(parts) != 3:
        raise ValueError(f"{file_path.stem} is not formated as '[symbol]_[date]_[action]'") 

    symbol, date, action = parts

    return {
        "symbol": symbol.lower(),   # symbol
        "date": date,               # date of action
        "action": action.lower()    # open, update or close  
    }


