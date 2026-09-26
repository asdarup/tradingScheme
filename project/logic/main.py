"""
The goal with this code is to find the optimal values for 'BUY_ORDER_SCALING_FACTOR' and 'TRAILING_STOP_SCALING_FACTOR'
"""

from pathlib import Path
from project.logic.tasks.file_handler import (
    get_csv_filepath,
    has_csv_file,
    make_csv_file,
    make_directory,
    move_file,
    parse_filename
)
from project.logic.tasks.data_handler import (
    ini
)


PORTFOLIO_SIZE: float = None
POSITION_SIZE: float = None
AVG_TRANSACTION_FEES: float = None

BUY_ORDER_SCALING_FACTOR: float = None
TRAILING_STOP_SCALING_FACTOR:float = None

BASE_DIR: Path = Path(__file__).resolve().parent.parent
INPUT_DIR: Path = BASE_DIR/"input"
LOG_DIR: Path = BASE_DIR/"log"


while has_csv_file(INPUT_DIR):
    input_filepath: Path = get_csv_filepath(INPUT_DIR)

    filename: dict[str, str] = parse_filename(input_filepath)

    symbol: str = filename.get("symbol")
    date: str = filename.get("date")
    action: str = filename.get("action")

    if action == "open":
        entry_directory: Path = make_directory(LOG_DIR, symbol, date)

        raw_filepath: Path = move_file(input_filepath, entry_directory)

        meta_filepath: Path = make_csv_file(entry_directory, )

        

 


    elif action == "update":

    elif action == "close":

    else:
        raise ValueError(f"Formating error, {filename.get("action")} does not correspond to 'open', 'update' or 'close'") 


    