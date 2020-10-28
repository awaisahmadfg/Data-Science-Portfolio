# airbnb.analysis
Showcases data analysis of Airbnb listings

# Git hub url
https://github.com/manjukiruthika/airbnb.analysis.git

# Blog post link
https://medium.com/@manjukiruthika/under-the-lens-seattle-airbnb-listings-993d6311cf44

## Motivation
The aim of the project is to perform analysis on airbnb listings and provide useful insights.
The project currently analyses Seattle dataset

## Contents
The repository contains a data_analysis jupyter notebook. Data and plots folder and requirements.txt file


Libraries required are
- Anaconda distribution v 4.3.30
- Folium map library
	- conda install -c conda-forge folium


## Analysis

Data was pre-processed to remove nulls, convert datetime records to datetime format, handle categorical variables etc.
Descriptive statistics of the data was obtained.

The following business questions were answered by the analysis


```
Question 1. At Airbnb, we would want to know which months of the year are busier in Seattle than others?

- Approach:From the calendar data, get all the available listing dates and price. Summing the price and grouping the data by month should mention how busy each month is.
When a listing as not available in the calendar data we consider those records as missing values and remove them from our analysis.

- Observation: Month of december seems to be the most busiest indicating winter holiday period around Xmas and new year. 
The month of august is next busiest indicating school holiday period in summer. Jan is least busier than all the other months.
```
![Alt Total_Listings_Price_per_month](plots/Total_Listings_Price_per_month.png)


```		
Question 2. Which neighbourhoods in Seattle provide the most revenue?

- Approach: Listings have neighbourhood information.I've joined/combined listings and calendar data. Summing the price and grouping the data by neighbourhood helps one to determine how much revenue each neighbourhood is making.
- Observation:Capitoal hill neighbourhood seems to make the most revenue. Either it has more listings available or it has listings which are priced higher

```
![Alt Top_10_neighbourhood_by_listings_revenue](plots/Top_10_neighbourhood_by_listings_revenue.png)

```
Question 3. Are there any property related factors that affect the price?


- Approach: Extracting the numeric columns, I check whether there is any linear relationship between the numeric variables and price by running a correlation plot.
- Observation: From the hierarchical correlation plot, above one could observe that there are blocks of sections which are correlated within each other. Let us take the first block which has the price field. We could observe that price is correlated with bathrooms, bedrooms, accomodates (number of people it accomodates), beds, guests included and square feet. Negative correlation between reviews per month and price indicating that high priced  properties have fewer reviews.
```
![Alt Correlation plot Price and property Variables](plots/Corr_plot_Price_and_Property_Variables.png)

```
Question 4. Does location / neighbourhood have an effect on price? Are we seeing any pattern of listings / price on the location map?

- Approach: From the percentiles obtained for price, we divide the price into 3 ranges - low, medium and high. Any value below 25th percentile is low and between 25th and 75th percentile is medium and above 75th percentile is high.We then plot the listings and their price ranges on the map based on longitude and latitude. The idea is to observe are there any locations which have more low price listings?. Are there locations which have high price and medium price listings?
- Observation: Studying the map, one could observe prevalance of low/medium/high listings. For instance, around Univeristy of Washington there are many low and medium priced listings. Around capitol hill area, there are more prevalance of medium and high price listings

```
![Alt Seattle location and Price Ranges](plots/Seattle_Price_on_Map1.png)

```
Question 5. Are we able to predict price ranges (low/medium/high) based on property, host and review information?


- Approach: Combining the categorical variables like the property, host and review information - I check whether we are able to predict the price range of a property as low / medium and high? Instead of predicting price with the small volume of data, I've turned it into a classification problem where I'm predicting price ranges(low/medium/high). 
I choose a machine learning algorithm - Random Forests Classifier. This tree based algorithm, could handle combination of categorical and numeric data to help predict the price ranges. The data is split into 80% train and 20% test sets. 5 fold cross validation is carried out on the training data for different number of estimators. The optimal hyperparameter is chosen and the algorithm is trained with the optimal parameter. It is then tested on 20% data. Accuracy metric is used for evaluation of the algorithm.
- Observation: The features are ranked based on their importance and the visualisation shows the top 20 variables which have an impact on determining the price range. We could observe that room type entire home/appt, reviews per month, number of bedrooms and availability all have an impact on determining the price ranges.
Note on data processing
Handling Categorical values - I dummy encode the categorical values so that the data could be used by any classification algorithm. Handling missing values - I observe that 75% of the data is without nulls and most of the missing information is in review scores. I decide to remove the rows with null review scores as i conduct experiments filling missing review scores with mean and observe that adding these rows did not improve the prediction.

```
![Alt Top features that influence price](/plots/Top_20_features_price_ranges.png)
```
Summary:
- Through visualization and analysis, one could observe time of the year and neighbourhood which yield more revenue.
- Through visualization able to understand the distribution of listing price ranges in various locations
- Through correlation analysis, one could observe the relations between price and property variables
- Through machine learning analysis, one could understand what features are important in predicting price ranges. 
Able to predict price ranges with 75% accuracy on test data
```
