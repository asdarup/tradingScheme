"""
The goal with this code is to find the optimal values for 'BUY_ORDER_SCALING_FACTOR' and 'TRAILING_STOP_SCALING_FACTOR'
"""

from pathlib import Path
from project.logic.tasks.file_handler import (
    get_csv_file_path,
    has_csv_file,
    make_file,
    make_directory,
    move_file,
    parse_file_stem
)
from project.logic.tasks.data_handler import (
    ini
)


PORTFOLIO_SIZE: float = None
POSITION_SIZE: float = None
AVG_TRANSACTION_FEES: float = None

BUY_ORDER_SCALING_FACTOR: float = None
TRAILING_STOP_SCALING_FACTOR:float = None

BASE_DIRECTORY_PATH: Path = Path(__file__).resolve().parent.parent
INPUT_DIRECTORY_PATH: Path = BASE_DIRECTORY_PATH/"input"
LOG_DIRECTORY_PATH: Path = BASE_DIRECTORY_PATH/"log"


while has_csv_file(INPUT_DIRECTORY_PATH):
    input_file_path: Path = get_csv_file_path(INPUT_DIRECTORY_PATH)

    file_stem_parts: dict[str, str] = parse_file_stem(input_file_path)

    symbol: str = file_stem_parts.get("symbol")
    date: str = file_stem_parts.get("date")
    action: str = file_stem_parts.get("action")

    if action == "open":
        entry_directory_path: Path = make_directory(LOG_DIRECTORY_PATH, f"{symbol}_{date}")

        raw_directory_path: Path = make_directory(entry_directory_path, "raw")

        raw_file_path: Path = move_file(input_file_path, raw_directory_path)

        meta_file_path: Path = make_file(entry_directory_path, "meta.csv" )

        swep_file_path: Path = make_file(entry_directory_path, "meta.csv" )

        

 


    elif action == "update":

    elif action == "close":

    else:
        raise ValueError(f"Formating error, {filename.get("action")} does not correspond to 'open', 'update' or 'close'") 


    