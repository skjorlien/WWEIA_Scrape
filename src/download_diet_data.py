import requests
import pandas as pd
from pathlib import Path
from settings import DATA_DIR


'''
Script to download all WWEIA diet data and demographics given some years. 

There is an additional "variables_list" file that I manually saved as a csv.

Link to the 2021 cycle:
https://wwwn.cdc.gov/nchs/nhanes/search/DataPage.aspx?Component=Dietary&Cycle=2021-2023 
'''



def download_data(link_dict, year):
    for file, url in link_dict.items():
        response = requests.get(url)

        with open(DATA_DIR / year / file, "wb") as f:
            f.write(response.content)

# 2021 
files_to_download_2021 = {
    "interview_IF_day1.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DR1IFF_L.xpt",
    "interview_IF_day2.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DR2IFF_L.xpt",
    "interview_support_file.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DRXFCD_L.xpt",
    "demographics.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.xpt"
}

# 2017
files_to_download_2017 = {
    "interview_IF_day1.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DR1IFF_J.xpt",
    "interview_IF_day2.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DR2IFF_J.xpt",
    "interview_support_file.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DRXFCD_J.xpt",
    "demographics.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DEMO_J.xpt"
}
        
# 2015
files_to_download_2015 = {
    "interview_IF_day1.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2015/DataFiles/DR1IFF_I.xpt",
    "interview_IF_day2.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2015/DataFiles/DR2IFF_I.xpt",
    "interview_support_file.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2015/DataFiles/DRXFCD_I.xpt",
    "demographics.xpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2015/DataFiles/DEMO_I.xpt"
}

download_data(files_to_download_2021, "2021")
