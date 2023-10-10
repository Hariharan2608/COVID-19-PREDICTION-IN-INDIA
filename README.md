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
### Attribute Information:
1.Date → format of date-month-year(30-Jan-20)

2.Date_YMD → in format of month / date /year (1/30/2020)

3.Daily Confirmed → daily confirmed cases

4.Total Confirmed → cumulative confirmed cases

5.Daily Recovered → daily cured cases

6.Total Recovered → cumulative cured cases

7.Daily Deceased → daily confirmed deaths

8.Toal Deceased → cumulative deaths

## MODEL DEVELOPMENT
### FBPROPHET
In this segment, we’re going to generate a week ahead forecast of
confirmed cases of COVID-19 using Prophet, with specific prediction
intervals by creating a base model both with and without tweaking of
seasonality-related parameters and additional regressors.
### What is Prophet?
Prophet is open source software released by Facebook’s Core Data
Science team. It is available for download on CRAN and PyPI.
We use Prophet, a procedure for forecasting time series data based on
an additive model where non-linear trends are fit with yearly, weekly,
and daily seasonality, plus holiday effects. It works best with time series
that have strong seasonal effects and several seasons of historical data.
Prophet is robust to missing data and shifts in the trend, and typically
handles outliers well.

• Ability to handle more frequent timeseries data

• Stress Tester and scenario builder

• More data sources

Prophet follows the sklearn model API. We create an instance of the
Prophet class and then call its fit and predict methods.
The input to Prophet is always a dataframe with two columns: ds and y.
The ds (datestamp) column should be of a format expected by Pandas,
ideally YYYY-MM-DD for a date or YYYY-MM-DD HH:MM:SS for a
timestamp. The y column must be numeric, and represents the
measurement we wish to forecast.

### Why Prophet?
• Accurate and fast: Prophet is used in many applications across
Facebook for producing reliable forecasts for planning and goal
setting. Facebook finds it to perform better than any other
approach in the majority of cases. It fit models in stan, so that you
get forecasts in just a few seconds.

• Fully automatic: Get a reasonable forecast on messy data with no
manual effort. Prophet is robust to outliers, missing data, and
dramatic changes in your time series.

• Tunable forecasts: The Prophet procedure includes many
possibilities for users to tweak and adjust forecasts. You can use
human-interpretable parameters to improve your forecast by
adding your domain knowledge

• Available in R or Python: Facebook has implemented the Prophet
procedure in R and Python. Both of them share the same
underlying Stan code for fitting. You can use whatever language
you’re comfortable with to get forecasts.

### Prediction Algorithm
In machine learning, various time series forecasting models are
available like ARIMA, SARIMA, GARCH, Dynamic linear models,
TBATS, Prophet, LSTM, etc.
Here we are using Prophet. Prophet is forecasting model which
allows dealing with multiple seasonalities. It is open source software
and is released by Facebook’s Core Data Science team. The prophet
model assumes that time series can be decomposed as follows:
y(t) = g(t) + s(t) + h(t) + ε(t)
The three terms g(t), s(t) and h(t) correspond respectively to trend,
seasonality and holiday. The last term is the error term.

<img width="177" alt="image" src="https://user-images.githubusercontent.com/88303186/160346058-1d7a53da-b251-4744-953a-734e65db6624.png">

### Trend:
The trend shows the tendency of the data to increase or decrease over
a long period of time and it filters out the seasonal variations.

### Seasonality:
Seasonality is the variations that occur over a short period of time and
is not prominent enough to be called a “trend”.
Understanding the Prophet Model
The general idea of the model is similar to a generalized additive
model. The “Prophet Equation” fits, as mentioned above, trend,
seasonality and holidays. This is given by,
y(t) = g(t) + s(t) + h(t) + e(t)
where,

• g(t) refers to trend (changes over a long period of time)

• s(t) refers to seasonality (periodic or short term changes)


• h(t) refers to effects of holidays to the forecast

• e(t) refers to the unconditional changes that is specific to a
business or a person or a circumstance. It is also called the
error term.

• y(t) is the forecast.

Prophet provides us with two models(however, newer models can be
written or extended according to specific requirements). One is
the logistic growth model and the other one is piece-wise linear
model. By default, Prophet uses piece-wise linear model, but it can be
changed by specifying the model. Choosing a model is delicate as it is
dependent on a variety of factors such as company size, growth rate,
business model etc., If the data to be forecasted, has saturating and
non-linear data(grows non-linearly and after reaching the saturation
point, shows little to no growth or shrink and only exhibits some
seasonal changes), then logistic growth model is the best option.
Nevertheless, if the data shows linear properties and had a growth or
shrink trends in the past then, piece-wise linear model is a better
choice.
The logistic growth model is fit using the following statistical equation,
15
g(t) = C/(1 + 𝑒)
−𝑘(𝑡−𝑚)
where,

• C is the carry capacity

• k is the growth rate

• m is an offset parameter

an additive model is a nonparametric regression method. It was
suggested by Jerome H. Friedman and Werner Stuetzle and is an
essential part of the ACE algorithm. The AM uses a one-dimensional
smoother to build a restricted class of nonparametric regression
models. Because of this, it is less affected by the curse of dimensionality
than e.g. a p-dimensional smoother.

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



