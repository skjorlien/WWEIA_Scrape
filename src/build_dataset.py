import pandas as pd
from pathlib import Path
from settings import DATA_DIR 
'''
Notes on data availability:

There is no way to figure out what year a participant's data are from. So the "time" is 1 for nov-Apr, 2 may - oct. But
Each survey period is multi-year.

Geographic information is restricted but available to those who have access. 

I have "day" 

'''

files = [x for x in DATA_DIR.iterdir() if "interview_IF" in x.name]

day1_fname = "interview_IF_day1.xpt"
day2_fname = "interview_IF_day2.xpt"

rename_day1 = {
    "SEQN": "i",
    "DR1IFDCD": "j",
    "DR1IGRMS": "grams"
    }

day1 = pd.read_sas(DATA_DIR / day1_fname).rename(columns=rename_day1)[rename_day1.values()]
day1 = day1.groupby(['i', 'j'])['grams'].sum().reset_index()
day1["day"] = 1


rename_day2 = {
    "SEQN": "i",
    "DR2IFDCD": "j",
    "DR2IGRMS": "grams"
    }
day2 = pd.read_sas(DATA_DIR / day2_fname).rename(columns=rename_day2)[rename_day2.values()]
day2 = day2.groupby(['i', 'j'])['grams'].sum().reset_index()
day2["day"] = 2


rename_demog = {
    "SEQN": "i",
    "RIDAGEYR": "age",
    "RIAGENDR": "sex",
    "RIDEXMON": "time"
}

demogs = pd.read_sas(DATA_DIR / "demographics.xpt").rename(columns=rename_demog)[rename_demog.values()]
df = pd.concat([day1, day2], ignore_index=True)

product = pd.read_sas(DATA_DIR / "interview_support_file.xpt")
product.columns = ["j", "del", "food_name"]
product = product[["j", "food_name"]]

df.to_csv(DATA_DIR /  "WWEIA_intake.csv", index=False)
product.to_csv(DATA_DIR / "food_name_map.csv", index=False)
demogs.to_csv(DATA_DIR / "demographics.csv", index=False)
