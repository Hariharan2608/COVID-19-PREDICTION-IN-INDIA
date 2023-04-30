import streamlit as st
#import plotly_express as px
import pandas as pd
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from fbprophet.plot import add_changepoints_to_plot
from PIL import Image
import base64


# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)


st.title("Covid 19 Case Prediction")

img1 = Image.open("co.jpg")
img2 = Image.open("co1.jpg")


main_bg = "co3.jpg"
main_bg_ext = "jpg"


st.write(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}

    </style>
    """,
    unsafe_allow_html=True
)

home = st.sidebar.radio(
    label="Select",
    options=['Home', 'Covid 19 Prediction'])
    
if home == 'Home':
    
    st.write("This app helps you to predict the daily Cases and Recovered of covid 19 in India")
   
    st.subheader("Overview")
    st.write("Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.")
        
    st.write("Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.  Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.")
    st.write("This app helps you to predict the daily Cases,Recovery and Deaths of covid 19 in India")

    st.image(img1,width = 800)
        
    st.subheader("Prevention")
    st.write("To prevent infection and to slow transmission of COVID-19, do the following:")
    st.write("►Wash your hands regularly with soap and water, or clean them with alcohol-based hand rub.")
    st.write("►Maintain at least 1 metre distance between you and people coughing or sneezing.")
    st.write("►Avoid touching your face.")
    st.write("►Cover your mouth and nose when coughing or sneezing.")
    st.write("►Stay home if you feel unwell.")
    st.write("►Refrain from smoking and other activities that weaken the lungs.")
    st.write("►Practice physical distancing by avoiding unnecessary travel and staying away from large groups of people.")
        
    st.subheader("Modeling")
    st.write("“Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well. Prophet is open source software released by Facebook’s Core Data Science team. It is available for download on CRAN and PyPI.”")
     
    st.image(img2,width = 800)
    
    st.subheader("Advantage of prophet")
    st.write("►Accurate and Fast – Models are fit in Stan, “a state-of-the-art platform for statistical modeling and high-performance statistical computation”.")
    st.write("►Fully Automatic – Facebook understands that time series forecasting is niche. Data scientists might not have extensive training in it and find other forecasting methods to be too hard to tune or too inflexible. Prophet is supposed to be easy to use. “Prophet is robust to outliers, missing data, and dramatic changes in your time series.”")
    st.write("►Tunable – Facebook assumes that data scientists have deep domain expertise. Prophet aims to account for potentially idiosyncratic features by allowing data scientists to apply their expertise and easily tweak the forecast.")


elif home == 'Covid 19 Prediction':
    # Add a sidebar
    st.sidebar.subheader("Settings")

    # Setup file upload
    uploaded_file = st.sidebar.file_uploader(
                            label="Upload your CSV or Excel file.",
                             type=['csv', 'xlsx'])
    
    global df

    if uploaded_file is not None:
        print(uploaded_file)
        print("hello")

        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            df = pd.read_excel(uploaded_file)
       
    st.header("Data")
    st.write("If you don't have a dataset please click here https://api.covid19india.org/csv/latest/case_time_series.csv . It helps you to view the current cases.Then choose the downloaded file from the downloads.")
    try:
        st.write("This is where you can see your dataset.")
        st.write(df)
    except Exception as e:
        print(e)
        st.write("Please upload file to the application.") 
        
    predict_select = st.sidebar.selectbox(
        label="Select the Prediction type",
        options=[' ', 'Cases', 'Recovered'])

    if predict_select == "Cases":
        eda = ['Graphs', 'Trend', 'Predicted']
        confirm = st.sidebar.selectbox("select",eda) 
        st.header((confirm))
        
        try:
            df.drop(['Date','Total Confirmed','Daily Recovered','Total Recovered','Daily Deceased','Total Deceased'], axis=1, inplace=True)
            df.columns = ['ds','y']
            
                 ##modeling
            m  = Prophet(
                interval_width=0.95,
                changepoint_prior_scale=0.4,
                growth='linear',
                changepoint_range=0.9,
                daily_seasonality=False,
                weekly_seasonality=True,
                yearly_seasonality=True,
                seasonality_mode='multiplicative'
            )
                    
            m.fit(df)

            future= m.make_future_dataframe(
                periods=365,
                freq='d',
                include_history=True
            )

                 # Prediction 
                       
            forecast = m.predict(future)
        except Exception as e:
            print(e)  

        
                
        if confirm == "Graphs":
            try:
                st.write("The graph helps to unterstand our prediction. The black dot epresents the actual value.The blue line represents the predicted value and the shade over the blue line represents the lowe and upper limit of the predicted value.")
                fig = plot_plotly(m, forecast,xlabel='Date',ylabel='Recovered Cases')  
                st.plotly_chart(fig)
            except Exception as e:
                print(e)
                
        if confirm == "Trend":
            try:
                st.write("Trend is a pattern in data that shows the movement of a series to relatively higher or lower values over a long period of time. In other words, a trend is observed when there is an increasing or decreasing slope in the time series. Trend usually happens for some time and then disappears, it does not repeat. For example, some new song comes, it goes trending for a while, and then disappears. There is fairly any chance that it would be trending again.")       
                trend = m.plot(forecast)
                a = add_changepoints_to_plot(trend.gca(), m, forecast)
                st.write(trend)
                st.write("The trend we saw in this graph is stationary trend which means there is no pattern.In this graph x axis has ds which means date and y axis  represents the daily confirmed cases.")
            except Exception as e:
                print(e)
         
        if confirm == "Predicted": 
            try:
                st.write("You can see the upcoming week recovered case prediction.In this table ds means the date,yhat represents our predicted number of cases , yhat_lower and yhat_upper represents our lower and upper limit of the predicted cases.")
                final = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(8)
                st.write(final)
            except Exception as e:
                print(e)
                
    elif predict_select == "Recovered":
        eda = ['Graphs', 'Trend', 'Predicted']
        confirm = st.sidebar.selectbox("select",eda)
        st.header((confirm))
        
        try:
            df.drop(['Date','Daily Confirmed','Total Confirmed','Total Recovered','Daily Deceased','Total Deceased'], axis=1, inplace=True)
            df.columns = ['ds','y']
            
                  ##modeling
            model = Prophet(
                interval_width=0.95,
                changepoint_prior_scale=0.4,
                growth='linear',
                changepoint_range=0.9,
                daily_seasonality=False,
                weekly_seasonality=True,
                yearly_seasonality=True,
                seasonality_mode='multiplicative'
            )
                    
            model.fit(df)

            future_pd = model.make_future_dataframe(
                periods=7,
                freq='d',
                include_history=True
            )

                 # Prediction 
                       
            forecast_pd = model.predict(future_pd)
           
        except Exception as e:
            print(e)
           
        
                
        if confirm == "Graphs":
            try:
                st.write("The graph helps to unterstand our prediction. The black dot epresents the actual value.The blue line represents the predicted value and the shade over the blue line represents the lowe and upper limit of the predicted value.")
                fig = plot_plotly(model, forecast_pd,xlabel='Date',ylabel='Recovered Cases')  
                st.plotly_chart(fig)
            except Exception as e:
                print(e)

        if confirm == "Trend":
            try:
                st.write("Trend is a pattern in data that shows the movement of a series to relatively higher or lower values over a long period of time. In other words, a trend is observed when there is an increasing or decreasing slope in the time series. Trend usually happens for some time and then disappears, it does not repeat. For example, some new song comes, it goes trending for a while, and then disappears. There is fairly any chance that it would be trending again.")    
                trend = model.plot(forecast_pd)
                a = add_changepoints_to_plot(trend.gca(), model, forecast_pd)
                st.write(trend)
                st.write("In this graph x axis has ds which means date and y axis  represents the daily recovered ceses.")
            except Exception as e:
                print(e)

        if confirm == "Predicted": 
            try:
                st.write("You can see the upcoming week recovered case prediction.In this table ds means the date,yhat represents our predicted number of cases , yhat_lower and yhat_upper represents our lower and upper limit of the predicted cases.")
                final = forecast_pd[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(8)
                st.write(final)
            except Exception as e:
                print(e)
