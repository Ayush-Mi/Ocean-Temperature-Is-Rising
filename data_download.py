'''
The below code is used to download the data for Mediterranean Sea from year 1991 to 2024.
A user account needs to be created https://www.copernicus.eu/en to use the below code.
'''
import copernicusmarine
from datetime import datetime, timedelta


# change to your username & password
username = 'username'
password = 'password'

def generate_dates(start_year, end_year):
    dates = []
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year + 1, 1, 1)  # Adding 1 to end_year to include the end year
    delta = timedelta(days=1)

    while start_date < end_date:
        dates.append(start_date.strftime('%Y%m%d'))
        start_date += delta

    return dates

def download_data(dataset_id, start_year, end_year):
    year_list = generate_dates(start_year, end_year)
    for i in year_list:
        #print(f"{i}000000.nc")
        get_results = copernicusmarine.get(
            dataset_id = dataset_id,
            # filter = f"{i}0101000000*.nc",
            filter = f"{i}000000*.nc",
            no_directories = True,
            output_directory = "data/download/",
            username= username,
            password=password,
            force_download = True)
    

dataset_id = 'cmems_SST_MED_SST_L4_REP_OBSERVATIONS_010_021'
start_year = 1991
end_year = 2023

download_data(dataset_id, start_year, end_year)

print("All the files have been downloaded")