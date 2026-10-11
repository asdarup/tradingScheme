import utilities as utl

from pathlib import Path


# Constants
# Project directory paths 
BASE_DIRECTORY_PATH: Path = Path(__file__).resolve().parent.parent
LOG_DIRECTORY_PATH: Path = BASE_DIRECTORY_PATH/"log"

# User specific parameters


# User actions
INITIAL_ACTIONS: dict[str, str] = {
    "0": "exit_program",
    "1": "open_new_entry",
    "2": "update_active_entry",
    "3": "close_active_entry",
    "4": "find_entry",
    "5": "delete_entry"
}
VALID_INITIAL_ACTIONS: str = ", ".join(INITIAL_ACTIONS.keys())


OPEN_NEW_ENTRY_SECONDARY_ACTION: dict[str, str] = {
    "0": "return_to_main_menu",
    "1": "operational_entry",
    "2": "preliminary_entry"
}
VALID_OPEN_NEW_ENTRY_SECONDARY_ACTION: str = ", ".join(OPEN_NEW_ENTRY_SECONDARY_ACTION.keys())


# Logic
while True:
    # Get initial user input 
    initial_action: str = input("""
Index   Action
0       Exit program
1       Open new entry
2       Update active entry 
3       Close active entry
4       Find entry
    1       All
    2       By ticker symbol
    3       By date
    4       By date range
5       Delete entry 
Choose Index: """
    )
    initial_action: str = INITIAL_ACTIONS.get(initial_action)

    # Evaluate user input
    if initial_action not in INITIAL_ACTIONS.values():
        # Wrong input error handling 
        print (f"Invalid input. Valid inputs: {VALID_INITIAL_ACTIONS}")

    elif initial_action == "exit_program":
        # Exsit program 
        break

    elif initial_action == "open_new_entry":
        # Get secondary user input 
        open_new_entry_secondary_action: str = input("""
Index   Action
0       Return to main menu
1       Operational entry
2       Preliminary entry 
Choose Index: """)
        open_new_entry_secondary_action: str = OPEN_NEW_ENTRY_SECONDARY_ACTION.get(open_new_entry_secondary_action)

        # Evaluate user input
        if open_new_entry_secondary_action not in OPEN_NEW_ENTRY_SECONDARY_ACTION.values():
            # Wrong input error handling 
            print (f"Invalid input. Valid inputs: {VALID_OPEN_NEW_ENTRY_SECONDARY_ACTION}")
        
        elif open_new_entry_secondary_action == "return_to_main_menu":
            # Restart loop  
            continue

        elif open_new_entry_secondary_action == "operational_entry": 
            # Set initial parameters
            portfolio_size:float = float(input("Portfolio size in stock currency:"))
            ticker_symbol: str = input("Ticker Symbol: ").upper()
            sector: str = input("Sector: ")
            entry_open_date: str = input("Open trade, YYMMDD: ")
            buy_order_placed_date: str = input("Order sent to market,date: ")
            action: str = "open"

            # Make entry
            entry_directory_path: Path = utl.make_directory(
                base_directory_path=LOG_DIRECTORY_PATH,
                new_directory_name=f"{entry_open_date}_{ticker_symbol}"
            )
            raw_directory_path: Path = utl.make_directory(
                base_directory_path=entry_directory_path,
                new_directory_name="raw"
            )

            # Download raw data file
            raw_file_path: Path = utl.make_file(
                base_directory_path=raw_directory_path,
                new_file_name=f"{entry_open_date}_{ticker_symbol}_{action}.csv"
            ) 
            utl.download_price_data_to_csv(
                ticker_symbol,
                utl.OPEN_PRICE_DATA_PERIOD,
                utl.OPEN_PRICE_DATA_INTERVAL,
                raw_file_path
            )

            # Initialize meta data
            meta_data: utl.Meta_Data = utl.Meta_Data(
                ticker_symbol=ticker_symbol,
                sector=sector,
                entry_open_date=entry_open_date,
                entry_directory_path=entry_directory_path
            )
            meta_data.set_portfolio_size(
                portfolio_size=portfolio_size
            )
            meta_data.set_buy_order_placed_date(
                buy_order_placed_date=buy_order_placed_date
            )
            meta_data.set_average_true_range()
            meta_data.set_max_price()
            meta_data.set_buy_order_placed_trigger()
            meta_data.set_trailing_stop_placed_trigger()
            meta_data.set_risk_adjusted_position_size()
            meta_data.set_buy_order_placed_quantity()

            # Compile meta data file 
            meta_file_path: Path = utl.make_file(
                base_directory_path=entry_directory_path,
                new_file_name="meta.csv" )
            utl.write_meta_file(
                meta_data=meta_data,
                meta_file_path=meta_file_path
            )

        




    #elif initial_action == "update_active_entry":

    #elif initial_action == "close_active_entry":





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
