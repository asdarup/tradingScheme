from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
INPUT_DIR: Path = BASE_DIR/"input"

def has_input_file() -> bool:
    """
    Checks if there are .csv files in ./input
    if any → return True 
    if not → return False
    """
    return any(INPUT_DIR.glob("*.csv"))

def get_input_filepath() -> Path:
    """
    Gets the directory of a file in ./input
    if any → return Path
    if not → raise FileNotFoundError 
    """
    file = next(INPUT_DIR.glob("*.csv"), None)

    if file is None:
        raise FileNotFoundError("File not found, no files in ./input")

    return file


