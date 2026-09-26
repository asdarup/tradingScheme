from pathlib import Path
from shutil import move 

BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
DATA_DIR: Path = BASE_DIR/"data"

def parse_filename(file: Path) -> dict[str, str]:
    """
    Parse filename, from [symbol_date_action] to [symbol], [date] and [action] 
    if format good → return dict
    if format bad  → raise ValueError
    """
    parts = file.stem.split("_")

    if len(parts) != 3:
        raise ValueError(f"Formating error, {file.name} is not formated as 'symbol_date_action.csv'") 

    symbol, date, action = parts

    return {
        "symbol": symbol.lower(),
        "date": date,
        "action": action.lower()    # open, update or close  
    }

def create_directory(
    symbol: str,
    date: str
) -> Path:
    """
    Create a new directory in ./data, ./data/[symbol]_[date]
    return Path
    """
    new_directory = DATA_DIR/f"{symbol}_{date}"

    new_directory.mkdir()

    return new_directory

def move_file(
    old_filepath: Path,
    new_directory: Path
) -> Path:
    """ 
    Move file to new directory
    return Path
    """
    new_filepath = new_directory/f"{old_filepath.name}"

    move(old_filepath, new_directory)

    return new_filepath
    

