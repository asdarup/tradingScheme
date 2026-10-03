"""
The goal with this code is to find the optimal values for 'BUY_ORDER_SCALING_FACTOR' and 'TRAILING_STOP_SCALING_FACTOR'
"""

from pathlib import Path

#from project.logic.tasks.file_handler import (
#    get_csv_file_path,
#    has_csv_file,
#    make_file,
#    make_directory,
#    move_file,
#    parse_file_stem
#)
#from project.logic.tasks.data_handler import (
#    ini
#)


PORTFOLIO_SIZE: float = None
POSITION_SIZE: float = None
AVG_TRANSACTION_FEES: float = None

BUY_ORDER_MAX_PRIE_HORIZON: float = None
BUY_ORDER_SCALING_FACTOR: float = None
TRAILING_STOP_SCALING_FACTOR:float = None

BASE_DIRECTORY_PATH: Path = Path(__file__).resolve().parent.parent
LOG_DIRECTORY_PATH: Path = BASE_DIRECTORY_PATH/"log"

ACTIONS: dict[str, str] = {
    "0": "exit_program",
    "1": "open_position",
    "2": "update_position",
    "3": "close_position"
}
VALID_ACTIONS: str = ", ".join(ACTIONS.keys())


while True:
    action: str = input(
"""
Index   Action
0       Exit program
1       Open position
2       Update position
3       Close position
Choose Index: """
    )

    action = ACTIONS.get(action)

    if action not in ACTIONS.values():
        print (f"Invalid input. Valid inputs: {VALID_ACTIONS}")

    elif action == "exit_program":
        break

    elif action == "open_position":
        ticker_symbol: str = input("Ticker Symbol: ")
        sector: str = input("Sector: ")
        trade_initialization_date: str = input("Date: ")

    #elif action == "update_position":

    #elif action == "close_position":

    
        


















    
#    input_file_path: Path = get_csv_file_path(INPUT_DIRECTORY_PATH)
#
#    file_stem_parts: dict[str, str] = parse_file_stem(input_file_path)
#
#    symbol: str = file_stem_parts.get("symbol")
#    date: str = file_stem_parts.get("date")
#    action: str = file_stem_parts.get("action")
#
#    if action == "open":
#        entry_directory_path: Path = make_directory(LOG_DIRECTORY_PATH, f"{symbol}_{date}")
#
#        raw_directory_path: Path = make_directory(entry_directory_path, "raw")
#
#        raw_file_path: Path = move_file(input_file_path, raw_directory_path)
#
#        meta_file_path: Path = make_file(entry_directory_path, "meta.csv" )
#
#
#        
#
# 
#
#
#    elif action == "update":
#
#    elif action == "close":
#
#    else:
#        raise ValueError(f"Formating error, {file_stem_parts.get("action")} does not correspond to 'open', 'update' or 'close'") 
#
#
#    