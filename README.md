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

## Model & Prediction

## Conclusion & Future Work

## References
