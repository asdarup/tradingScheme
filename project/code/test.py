import utilities as utl

from pathlib import Path


# Project directory paths 
TEST_DIRECTORY_PATH: Path = (Path(__file__).resolve().parent.parent)/"test"

price_data_file_path: Path = utl.make_file(TEST_DIRECTORY_PATH, "price_data.csv")
utl.download_price_data_to_csv("KOG.OL","1y", "1d", price_data_file_path)