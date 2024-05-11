# Ocean Temperature Is Rising

## Introduction

Within the realm of oceanic research, the Mediterranean Sea stands as a dynamic and vital body of water, boasting a unique blend of environmental factors that profoundly influence global climate patterns. In this project, I have worked on a comprehensive analysis of the sea surface temperature within the Mediterranean Sea, aiming to unravel its intricate fluctuations and trends. By employing statistical techniques and deep learning model, I tried to construct a robust model capable of forecasting future sea surface temperatures with precision.

![](https://www.nationsonline.org/gallery/Mediterranean-Sea/USA-Mediterranean-Sea-comp.jpg)

## Dataset

The dataet used to analyze and build model was taken from [Copernicus Marine Service](https://data.marine.copernicus.eu/product/SST_MED_SST_L4_REP_OBSERVATIONS_010_021/description) which provides free and open marine services data. 

In this project we have specifically used Reprocessed (REP) Mediterranean (MED) dataset which has a stable and consistent long-term Sea Surface Temperature (SST) time series over the Mediterranean Sea (and the adjacent North Atlantic box) developed for climate applications.

The below description is taken from the overview section of the CMS website for our data:

*This product consists of daily (nighttime), optimally interpolated (L4), satellite-based estimates of the foundation SST (namely, the temperature free, or nearly-free, of any diurnal cycle) at 0.05° resolution grid covering the period from January 1st 1982 to present (currently, up to one month before real time). The MED-REP-L4 product is built from a consistent reprocessing of the collated level-3 (merged single-sensor, L3C) climate data record provided by the ESA Climate Change Initiative (CCI) and the Copernicus Climate Change Service (C3S) initiatives, but also includes in input an adjusted version of the AVHRR Pathfinder dataset version 5.3 to increase the input observation coverage. Due to Brexit, an interim production guarantees the temporal extension of the MED-REP-L4 product since 1st January 2023 to present.*

## Steps
1. Create an account on the CMS website to use their API to download data
2. Download the data from 1981 to 2024 using the script `data_download.py`. (Feel free to change the dates in the script to download specific year data or change the range)
3. The dataset contains the sea surface temperature values in kelvin of each day for all the points that fall between the latitude and longitude of the sea. To reduce the data size, I have take the average across the whole surface of sea on a given day along with other statistical values like variance, standard deviation, minimum and maximum values. This is created using the notebook `data_creation.ipynb`
4. The `train_and_predict.ipynb` notebook analyzes this compressed data and builds a model to predict the mean, variance, standard deviation, minimum and maximum sea surface temperature on a given day.

## Analysis

The sea surface temperature for Mediterranean sea seems to follow an yearly cycle where the temperature starts to rise from the month of April up till Septempber and then slowly starts to cool down again as shown in the picture below.

![](https://github.com/Ayush-Mi/Ocean-Temperature-Is-Rising/blob/main/img/fluctuations.png)


The same is reflected in the variance and standard deviation of the surface temperature which shows that it fluctuates a lot during this time.
![](https://github.com/Ayush-Mi/Ocean-Temperature-Is-Rising/blob/main/img/var_std.png)


If we look at the monthly distribution of the past 40 years we see on average there is more variability in the month of June which is when the temperature rises more steeply.
![](https://github.com/Ayush-Mi/Ocean-Temperature-Is-Rising/blob/main/img/monthly.png)

## Model & Prediction

The model used for the prediction is a simple three layer LSTM model which takes in the data for the past 30 time stamps and predicts the values for the 31st time stamp. It uses mean squared error as the loss function for training the model and achieves a MSE score of 0.0007 in only 10 epochs. The dataset was normalized using the min_max scaler before feeding in to the model. 

It was trained on past approximately 42 years of dataset, that is from 1982 to 2022-23 and tested on one year of data which is 2023-2024. Below is the graph of the predictions.
![](https://github.com/Ayush-Mi/Ocean-Temperature-Is-Rising/blob/main/img/test.png)

Later the model was used to forecast the next 90 days of sea surface temperature, that is from April 2024 to June 2024 and we see a rise in temperature, as expected:

![](https://github.com/Ayush-Mi/Ocean-Temperature-Is-Rising/blob/main/img/forecast.png)

## Conclusion & Future Work

In conclusion, there has been a yearly mean increase of 2 kelvin degrees of temperature in past 4 decades for the Mediterranean Sea. However, further analyses of specific portions of sea surface would help better understand and reason the fulctuations which will aid in taking sustainable actions in preserving marine life.

**In the below graph, ignore the sudden uptick after 2020 which is due the availibility of only 3 months of data year 2024**
![](https://github.com/Ayush-Mi/Ocean-Temperature-Is-Rising/blob/main/img/yearly.png)

## References
[Copernicus Marine Service](https://data.marine.copernicus.eu/product/SST_MED_SST_L4_REP_OBSERVATIONS_010_021/description)
