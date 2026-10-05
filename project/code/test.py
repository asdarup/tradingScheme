from pathlib import Path

from tasks.file_handler import (
    download_price_data_to_csv,
    make_file 
)


# Project directory paths 
TEST_DIRECTORY_PATH: Path = Path(__file__).resolve().parent

price_data_file_path: Path = make_file(TEST_DIRECTORY_PATH, "price_data.csv")
download_price_data_to_csv("KOG","1y", "1d", price_data_file_path)