# Libraries to import data
from pathlib import Path
import pandas as pd
import tarfile
import urllib.request

def load_housing_data():
    # Retrieve the data
    tarball_path = Path("../data/raw_data/datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("../data/raw_data/datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    print("✅ data has been loaded")
    return pd.read_csv(Path("datasets/housing/housing.csv"))
