from pathlib import Path


# change this to choose where to store data.
USER_DATA_PATH = "~/Data"

# sets up a Path object for file management 
DATA_DIR = Path(USER_DATA_PATH).expanduser() / "WWEIA"

try:
    DATA_DIR.mkdir(parents=True, exist_ok=False)
except FileExistsError:
    pass
else:
    print(f"Folder {DATA_DIR} was created")
