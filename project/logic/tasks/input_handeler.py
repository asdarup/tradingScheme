from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
INPUT_DIR: Path = BASE_DIR/"input"

def has_input_file() -> bool:
    """
    Checks if there are .csv files in input/
    if any → return True 
    if not → return False
    """
    return any(INPUT_DIR.glob("*.csv"))

def get_input_file() -> Path:
    """
    Gets a directory of a file in input/
    if any → return Path
    if not → raise FileNotFoundError 
    """
    file = next(INPUT_DIR.glob("*.csv"), None)

    if file is None:
        raise FileNotFoundError("File not found, ./input/")

    return file

def parse_input_filename(file: Path) -> dict[str, str]:
    """
    Parse a filename, [symbol_date_action], to [symbol], [date] and [action] 
    return {"symbol": [symbol], "date": [date], "action": [action]}  
    """
    parts = file.stem.split("_")

    if len(parts) != 3:
        raise ValueError(f"Formating error, {file.name} not symbol_date_action.csv") 

    symbol, date, action = parts

    return {
        "symbol": symbol,
        "date": date,
        "action": action
    }


