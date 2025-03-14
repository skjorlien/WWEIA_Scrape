import requests
import pandas as pd
from pathlib import Path
from settings import DATA_DIR


'''
Script to download all WWEIA data in the 2021 - 2023 cycle. 

There is an additional "variables_list" file that I manually saved as a csv.

https://wwwn.cdc.gov/nchs/nhanes/search/DataPage.aspx?Component=Dietary&Cycle=2021-2023 
'''

files_to_download = {
    "interview_IF_day1.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DR1IFF_L.xpt",
    "interview_IF_day2.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DR2IFF_L.xpt",
    "interview_TNI_day1.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DR1TOT_L.xpt",
    "interview_TNI_day2.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DR2TOT_L.xpt",
    "interview_support_file.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DRXFCD_L.xpt",
    "blend_info.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/1999/DataFiles/DSBI.xpt",
    "ingred_info.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/1999/DataFiles/DSII.xpt",
    "product_info.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/1999/DataFiles/DSPI.xpt"
}

for file, url in files_to_download.items():
    response = requests.get(url)
    
    with open(DATA_DIR / file, "wb") as f:
        f.write(response.content)


# also need demographics 
url = "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.xpt"
response = requests.get(url)

with open(DATA_DIR / "demographics.xpt", "wb") as f:
    f.write(response.content)
