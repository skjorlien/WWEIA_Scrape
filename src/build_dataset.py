import pandas as pd
from pathlib import Path
from settings import DATA_DIR 
'''
Notes on data availability:

There is no way to figure out what year a participant's data are from. So the "time" is 1 for nov-Apr, 2 may - oct. But
Each survey period is multi-year.

Geographic information is restricted but available to those who have access. 

'''

def generate_annual_IF_df(year):
    '''
    Not all participants are observed for both days. I take the average over the two days.

    this function assumes you have downloaded the required datasets already
    '''
    
    day1_fname = "interview_IF_day1.xpt"
    day2_fname = "interview_IF_day2.xpt"

    rename_day1 = {
        "SEQN": "i",
        "DR1IFDCD": "j",
        "DR1IGRMS": "grams"
    }

    day1 = pd.read_sas(DATA_DIR / year / day1_fname).rename(columns=rename_day1)[rename_day1.values()]
    day1 = day1.groupby(['i', 'j'])['grams'].sum().reset_index()
    day1["day"] = 1   

    rename_day2 = {
        "SEQN": "i",
        "DR2IFDCD": "j",
        "DR2IGRMS": "grams"
    }
    day2 = pd.read_sas(DATA_DIR / year / day2_fname).rename(columns=rename_day2)[rename_day2.values()]
    day2 = day2.groupby(['i', 'j'])['grams'].sum().reset_index()
    day2["day"] = 2

    ### Commenting out - price data is missing about a quarter of the food codes observed
    # prices = pd.read_csv(DATA_DIR / "pp_national_average_prices.csv")
    # prices = prices.loc[prices["year"].str.contains(year), ["food_code", "price_100gm"]]
    # prices.columns = ["j", "price_100g"]
    
    df = pd.concat([day1, day2], ignore_index=True)
    df["t"] = year
    df["m"] = "USA"
    df = df.groupby(["i", "j", "t", "m"])["grams"].mean().reset_index()

    food_names = generate_annual_product_info(year)

    df = df.merge(food_names, how="left", on=["j", "t"])
    # df = df.merge(prices, how="left", on="j")
    return df


def generate_annual_demog_df(year):
    rename_demog = {
        "SEQN": "i",
        "RIDAGEYR": "age",
        "RIAGENDR": "sex",
        "DMDHHSIZ": "HH_size"
    }
    
    demogs = pd.read_sas(DATA_DIR / year / "demographics.xpt").rename(columns=rename_demog)[rename_demog.values()]
    demogs["m"] = "USA"
    demogs["t"] = year
    demogs["sex"] = demogs["sex"].astype(int).astype(str)
    demogs["sex"] = demogs["sex"].map({"1": "Male", "2": "Female"})
    return demogs.loc[:, ["i", "t", "m", "age", "sex", "HH_size"]]


def generate_annual_product_info(year):
    product = pd.read_sas(DATA_DIR / year /  "interview_support_file.xpt")
    product.columns = ["j", "food_name", "long_name"]
    product["t"] = year
    product["food_name"] = product["food_name"].str.decode('utf-8').str.capitalize()
    return product[["j", "t", "food_name"]]


def generate_annual_dataproducts(year):
    df = generate_annual_IF_df(year)
    df.to_csv(DATA_DIR / "clean" / f"Food_Expenditures_{year}.csv", index=False)
    
    df = generate_annual_demog_df(year)
    df.to_csv(DATA_DIR / "clean" / f"Household_Characteristics_{year}.csv", index=False)
    
    # df = generate_annual_product_info(year) 
    # df.to_csv(DATA_DIR / "clean" / f"Product_names_{year}.csv", index=False)

    
if __name__ == "__main__":
    years = ["2015", "2017", "2021"]
    for y in years:
        generate_annual_dataproducts(y)
    
