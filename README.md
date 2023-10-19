# COVID-19-PREDICTION-IN-INDIA
To predict the daily covid cases in India.

Using Facebook prophet library in Python.

UI by using python’s Streamlit package.



## Objectives
We aim to create a covid 19 case (India) prediction application in 
  python which helps the user to find the upcoming one-week cases. 
  Which also predicts the daily recovered cases in India. 

## Software Used
•	Python Language
•	Streamlit
•	Fbprophet
•	Pandas

### Pandas
Pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.
 

### Streamlit
Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.
  In just a few minutes you can build and deploy powerful data apps
 
### Model(Fbprophet) 
Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several 
seasons of historical data.If you want to know more about fbprophet [click here](https://facebook.github.io/prophet/docs/quick_start.html)

### Data Analysis and Outbreak Prediction
For analysis and forecasting of number of COVID-19 patients in India, the framework shown in figure is used. The data is collected for the duration of 30th January 2020 . This dataset has everyday level data on the number of influenced cases, recovery, and deceased. It has a total of
8 columns. 
These are the columns in the dataset :Date, Date_YMD , Daily Confirmed ,Total Confirmed ,Daily Recovered ,Total Recovered ,Daily Deceased ,Toal Deceased.

## Dataset
You can find the dataset [here](https://www.covid19india.org/)

## MODEL DEVELOPMENT
### FBPROPHET
In this segment, we’re going to generate a week ahead forecast of
confirmed cases of COVID-19 using Prophet, with specific prediction
intervals by creating a base model both with and without tweaking of
seasonality-related parameters and additional regressors.

• Ability to handle more frequent timeseries data

• Stress Tester and scenario builder

<img width="177" alt="image" src="https://user-images.githubusercontent.com/88303186/160346058-1d7a53da-b251-4744-953a-734e65db6624.png">

### Trend:
The trend shows the tendency of the data to increase or decrease over
a long period of time and it filters out the seasonal variations.

## System Desgin
### Input Desgin

<img width="489" alt="image" src="https://user-images.githubusercontent.com/88303186/160350203-1a3df5ac-6045-477f-9955-ec07e21ced8e.png">

### Output Design

<img width="506" alt="image" src="https://user-images.githubusercontent.com/88303186/160350300-91ec8458-cff5-456e-9b17-7f5103113d7b.png">

## FUTURE SCOPE
As illustrated before the system can be used as a clinical assistant
for any person. The disease prediction through the risk factors can be
hosted online and hence any internet users can access the system
through a web browser.

The proposed model requires an efficient processor with good memory
configuration to implement it in real time. The proposed model has wide
area of application like grid computing, cloud computing, robotic
modeling, etc.

### Benefits

• People should get aware of the covid

• Helps us to take some precaution methods

• Helps in decision making like when should we go out

• It helps to the government to put lockdown

• Make it easier to the people for the prevention



