import yfinance as yf 

from pathlib import Path
from shutil import move


def download_price_data(
    ticker_symbol: str,
    period: str,
    interval: str,
    base_directory_path: Path
) -> None:
    """
    
    """
    data = yf.download(
        tickers=ticker_symbol, 
        eriod=period, 
        interval=interval)

    data.to_csv(base_directory_path)


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


def make_directory(
    base_directory_path: Path,
    new_directory_name: str
) -> Path:
    """
    Create a new directory, "new_directory_name", at "base_directory_path" .
    return new directory path 
    """
    new_directory_path = base_directory_path/new_directory_name

    new_directory_path.mkdir(exist_ok=False)

    return new_directory_path


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


