from pathlib import Path
from shutil import move


def has_csv_file(
    directory: Path
) -> bool:
    """
    Checks if there are .csv files in "directory"
    if any → return True 
    if not → return False
    """
    return any(directory.glob("*.csv"))


def get_csv_filepath(
    directory: Path
) -> Path:
    """
    Gets the filepath of a file .cvs in "directory"
    if any → return filepath
    if not → raise "FileNotFoundError" 
    """
    filepath = next(directory.glob("*.csv"), None)

    if filepath is None:
        raise FileNotFoundError(f"No .csv file found in {directory}")

    return filepath


def parse_filename(
    filepath: Path
) -> dict[str, str]:
    """
    Parse filename, from [symbol_date_action] to [symbol], [date] and [action] 
    if format good → return parts in a dictionary 
    if format bad  → raise "ValueError"
    """
    parts = filepath.stem.split("_")

    if len(parts) != 3:
        raise ValueError(f"{filepath.stem} is not formated as '[symbol]_[date]_[action]'") 

    symbol, date, action = parts

    return {
        "symbol": symbol.lower(),   # symbol
        "date": date,               # date of action
        "action": action.lower()    # open, update or close  
    }


def create_directory(
    base_directory: Path,
    symbol: str,
    date: str
) -> Path:
    """
    Create a new directory, /[symbol]_[date], in "base_directory" .
    return new directory path 
    """
    new_directory = base_directory/f"{symbol}_{date}"

    new_directory.mkdir()

    return new_directory


def move_file(
    old_filepath: Path,
    new_directory: Path
) -> Path:
    """ 
    Move file to new directory
    return new filepath
    """
    new_filepath = new_directory/f"{old_filepath.name}"

    move(old_filepath, new_directory)

    return new_filepath


def create_file(
        filename: str,
        directory: Path
) -> Path:
    """
    Create a new directory in ./data, ./data/[symbol]_[date]
        return Path
    """
