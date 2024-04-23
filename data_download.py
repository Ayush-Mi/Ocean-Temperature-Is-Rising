'''
The below code is used to download the data for Mediteranean Sea from year 1991 to 2024.
A user account needs to be created https://www.copernicus.eu/en to use the below code.
'''
import copernicusmarine

# change to your username & password
username = 'username'
password = 'password'

year_list = list(range(1991,2025,1))

# typical file format
# 19920106000000-GOS-L4_GHRSST-SSTfnd-OISST_HR_REP-MED-v02.0-fv03.0.nc
# to extract a particular day of month and year
# change the filter to f"{i}010100000*.nc" - this gives data for 1st January of all the year

for i in year_list:
    get_result_monthlymean_july = copernicusmarine.get(
        dataset_id = "cmems_SST_MED_SST_L4_REP_OBSERVATIONS_010_021",
        # filter = f"{i}010100000*.nc",
        filter = f"{i}*.nc",
        no_directories = True,
        output_directory = f"data/",
        username= username,
        password=password,
        force_download = True
    )

print("All the files have been downloaded")