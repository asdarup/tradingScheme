"""
The goal with this code is to find the optimal values for 'BUY_ORDER_SCALING_FACTOR' and 'TRAILING_STOP_SCALING_FACTOR'
"""

from pathlib import Path

from tasks.input_handeler import(
    has_input_file,
    get_input_filepath,
)

from tasks.data_handeler import(
    parse_filename,
    create_directory,
    move_file
)

PORTFOLIO_SIZE: float = None
POSITION_SIZE: float = None
AVG_TRANSACTION_FEES: float = None

BUY_ORDER_SCALING_FACTOR: float = None
TRAILING_STOP_SCALING_FACTOR:float = None

while has_input_file():
    input_filepath: Path = get_input_filepath()

    filename: dict[str, str] = parse_filename(input_filepath)

    symbol: str = filename.get("symbol")
    date: str = filename.get("date")
    action: str = filename.get("action")

    if action == "open":
        data_directory: Path = create_directory(symbol, date)

        data_filepath: Path = move_file(input_filepath, data_directory)

        




    elif action == "update":

    elif action == "close":

    else:
        raise ValueError(f"Formating error, {filename.get("action")} does not correspond to 'open', 'update' or 'close'") 


    