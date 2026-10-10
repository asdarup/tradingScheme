import utilities as utl

from pathlib import Path


# Constants
# Project directory paths 
BASE_DIRECTORY_PATH: Path = Path(__file__).resolve().parent.parent
LOG_DIRECTORY_PATH: Path = BASE_DIRECTORY_PATH/"log"

# User specific parameters
PORTFOLIO_SIZE: float = None
POSITION_SIZE: float = None
AVG_TRANSACTION_FEES: float = None

# User actions
ACTIONS: dict[str, str] = {
    "0": "exit_program",
    "1": "open_position",
    "2": "update_position",
    "3": "close_position",
    "4": "delete_entry",
    "5": "add_test_data"
}
VALID_ACTIONS: str = ", ".join(ACTIONS.keys())


# Logic
while True:
    # Get user input 
    action: str = input("""
Index   Action
0       Exit program
1       Open position
2       Update position
3       Close position
4       Delete entry
5       Add test data 
Choose Index: """
    )
    action = ACTIONS.get(action)

    # Evaluate user input
    if action not in ACTIONS.values():
        # Wrong input error handling 
        print (f"Invalid input. Valid inputs: {VALID_ACTIONS}")

    elif action == "exit_program":
        # Exsit program 
        break

    elif action == "open_position":
        # Get user Input
        ticker_symbol: str = input("Ticker Symbol: ").upper()
        sector: str = input("Sector: ")
        trade_initialization_date: str = input("Date: ")
        action: str = "open"

        # Make entry
        entry_directory_path: Path = utl.make_directory(
            base_directory_path=LOG_DIRECTORY_PATH,
            new_directory_name=f"{ticker_symbol}_{trade_initialization_date}"
        )
        raw_directory_path: Path = utl.make_directory(
            base_directory_path=entry_directory_path,
            new_directory_name="raw"
        )

        # Download price data 
        raw_file_path: Path = utl.make_file(
            base_directory_path=raw_directory_path,
            new_file_name=f"{ticker_symbol}_{trade_initialization_date}_{action}.csv"
        ) 
        utl.download_price_data_to_csv(
            ticker_symbol,
            utl.OPEN_PRICE_DATA_PERIOD,
            utl.OPEN_PRICE_DATA_INTERVAL,
            raw_file_path
        )

        # Make meta file 
        meta_file_path: Path = utl.make_file(
            base_directory_path=entry_directory_path,
            new_file_name="meta.csv" )
        utl.initialize_meta_file(
            meta_file_path=meta_file_path
        )

        # 
        

    #elif action == "update_position":

    #elif action == "close_position":

    #elif action == "add_test_data":




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
