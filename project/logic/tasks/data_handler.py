import csv

from pathlib import Path


def initialize_meta_file(
    meta_file_path: Path
) -> None:
    """
    Initialize the file at "meta_file_path"
    """
    with open(
        file=meta_file_path,
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            # Sock properties
            "Symbol",
            "Sector",
            # Buy order placed properties
            "Buy order placed date [Date]",
            "Buy order placed price [Price]",
            "Buy order placed quantity [Number]",
            # Buy order filed properties
            "Buy order filed date [Date]",
            "Buy order filed price [Price]",
            "Buy order filed quantity [Number]",
            "Buy order filed fees [Price]",
            # Trailing stop placed properties
            "Trailing stop placed date [Date]",
            "Trailing stop placed trigger [%]",
            "Trailing stop placed quantity [Number]",
            # Trailing stop filed properties
            "Trailing stop filed date [Date]",
            "Trailing stop filed price [Price]",
            "Trailing stop filed quantity [Number]",
            "Trailing stop filed fees [Price]"
        ]),


        writer.writerow()
        

def initialize_swep_file(
    filepath: Path,


)-> None:


    

