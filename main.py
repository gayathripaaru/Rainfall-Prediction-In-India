# loading in packages in this streamlit python file
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
rainfallPrediction = pd.read_csv("rainfall.csv")
st.title("Rainfall Prediction in India")
st.write("Rainfall prediction is important as heavy rainfall can lead to many disasters.The prediction helps people to take preventive measures. Now climate change is the biggest issue all over the world. Peoples are working on to detect the patterns in climate change as it affects the economy in production to infrastructure. So, making prediction of rainfall is a challenging task with a good accuracy rate. Making prediction on rainfall cannot be done by the traditional way, so scientist is using machine learning and deep learning to find out the pattern for rainfall prediction.Here we are showing the data visualization of Rainfall in India")
st.header("Data Visualization of Rainfall in India")
st.header("Rainfall in India Dataset")


# Annual rainfall is: high if  it is greater than or equal to 3418mm
# Annual rainfall is: low if  it is less than or equal to 292mm
valueIfTrue = "Heavy Rainfall"
valueIfFalse = "Low Rainfall"
rainfallPrediction['Amount of annual Rainfall'] = np.where((rainfallPrediction .ANNUAL >= 3000), valueIfTrue, valueIfFalse)


# Rainfall during the month of January
valueIfTrue = "Heavy Rainfall"
valueIfFalse = "Low Rainfall"
rainfallPrediction['Rainfall During the month of January'] = np.where((rainfallPrediction .JAN >= 3500), valueIfTrue, valueIfFalse)

# Rainfall during the month of June
valueIfTrue = "Heavy rainfall"
valueIfFalse = "Low rainfall"
rainfallPrediction['Amount of rainfall in the month of June'] = np.where((rainfallPrediction.JUN >=2500), valueIfTrue, valueIfFalse)

# Rainfall during the month of December
valueIfTrue = "Heavy rainfall"
valueIfFalse = "Low rainfall"
rainfallPrediction['Amount of Rainfall in the month of december'] = np.where((rainfallPrediction.DEC==3800), valueIfTrue, valueIfFalse)


# Rainfall during the month of JF
valueIfTrue = "Heavy rainfall"
valueIfFalse = "Low rainfall"
rainfallPrediction['Amount of Rainfall in the month of January and February'] = np.where((rainfallPrediction.JF>=3800), valueIfTrue, valueIfFalse)

# Rainfall during the month of MAM
valueIfTrue = "Heavy rainfall"
valueIfFalse = "Low rainfall"
rainfallPrediction['Amount of Rainfall in the month of March,April and May'] = np.where((rainfallPrediction.MAM>=3400), valueIfTrue, valueIfFalse)

# Rainfall during the month of JJAS
valueIfTrue = "Heavy rainfall"
valueIfFalse = "Low rainfall"
rainfallPrediction['Amount of Rainfall in the month of June,July,August,September'] = np.where((rainfallPrediction.JJAS>=1400), valueIfTrue, valueIfFalse)

# Rainfall during the month of OND
valueIfTrue = "Heavy rainfall"
valueIfFalse = "Low rainfall"
rainfallPrediction['Amount of Rainfall in the month of October,November,December'] = np.where((rainfallPrediction.OND==2500), valueIfTrue, valueIfFalse)

# co1 = 'Heavy Rainfall'
# co2 = 'Average Rainfall'
# co3 = 'Low Rainfall'
# co4 = 'Poor Rainfall'
# co5 = 'Very poor Rainfall'

# rainfallPrediction.loc[(rainfallPrediction['ANNUAL'] == 3400, 'Amount of Annual Rainfall')] = co1
# rainfallPrediction.loc[(rainfallPrediction['ANNUAL'] == 2500, 'Amount of  Annual Rainfall')] = co2
# rainfallPrediction.loc[(rainfallPrediction['ANNUAL'] == 1500, 'Amount of Annual Rainfall')] = co3
# rainfallPrediction.loc[(rainfallPrediction['ANNUAL'] == 1000, 'Amount of Annual Rainfall')] = co4
# rainfallPrediction.loc[(rainfallPrediction['ANNUAL'] == 500, 'Amount of Annual Rainfall')] = co5

# v1 = 'Excellent'
# v2 = 'Good '
# v3 = 'Average '
# v4 = 'Poor'
# v5 = 'Terrible '


# rainfallPrediction.loc[(rainfallPrediction['JF'] == 3400, 'Rainfall in the month of January and February')] = v1
# rainfallPrediction.loc[(rainfallPrediction['JF'] == 2500, 'Rainfall in the month of January and February')] = v2
# rainfallPrediction.loc[(rainfallPrediction['JF'] == 1500, 'Rainfall in the month of January and February')] = v3
# rainfallPrediction.loc[(rainfallPrediction['JF'] == 1000, 'Rainfall in the month of January and February')] = v4
# rainfallPrediction.loc[(rainfallPrediction['JF'] == 500, 'Rainfall in the month of January and February')] = v5

# c1 = 'High'
# c2 = 'Average'
# c3 = 'Low'
# rainfallPrediction.loc[(rainfallPrediction['JJAS'] <= 500, 'Jun,Jul,Aug,Sep')] = c3
# rainfallPrediction.loc[(((rainfallPrediction['JJAS'] > 1000) & (rainfallPrediction['JJAS'] <= 500)), 'Jun,Jul,Aug,Sep')] = c2
# rainfallPrediction.loc[(rainfallPrediction['JJAS'] >1500, 'Jun,Jul,Aug,Sep')] = c1

st.dataframe(rainfallPrediction)
# Select columns to display
if st.checkbox("Show dataset with selected columns"):
        # get the list of columns
        columns = rainfallPrediction.columns.tolist()
        st.write("#### Select the columns to display:")
        selected_cols = st.multiselect("", columns)
        if len(selected_cols) > 0:
            selected_df = rainfallPrediction[selected_cols]
            st.dataframe(selected_df)


# selecting all of the columns that have data types of ints or floats
numericHouseColumnsTuple = tuple(rainfallPrediction.select_dtypes(["int", "float"]).columns) 
HouseColumnsTuple = tuple(rainfallPrediction.columns)
unknownvariable1 = st.selectbox(
     'What do You Want The X-Axis of This Graph To Show?',
        numericHouseColumnsTuple)

unknownvariable2 = st.selectbox(
     'What do You Want The Y-Axis of This Graph To Show?',
           numericHouseColumnsTuple)

colorVariable1 = st.selectbox(
     'what would you like the graph to be colored based on?',
      ("SUBDIVISION", "YEAR", "JAN", "FEB", "MAR",
       "APR", "MAY", "JUN", "JUL", "AUG",
       "SEP", "OCT", "NOV", "DEC", "ANNUAL",
       "JF","MAM","JJAS","OND"))


titleMessage = "Scatterplot of " + unknownvariable2+" as compared to "+unknownvariable1
rainfallfig1 = px.scatter(rainfallPrediction, x=unknownvariable1, y=unknownvariable2, color = colorVariable1,
                           title = titleMessage)
st.plotly_chart(rainfallfig1)
txt = st.text_area('Analysis of the above Scatterplot Chart', '''This scatterplot for rainfall prediction shows the rainfall amount based on the x and y 
co-ordinates. you can change the x and y choices using the drop down menu. the options range anywhere from subdivisions, year, to month and more! Just like you can change the x and y axis, you can also change the coloring factor.  ''')


# choice = st.radio("Pick a View Type", ['Terrible View', 'Poor View', 'Average View', 'Good View', 'Excellent View'])
# if choice == 'Terrible View':
#     houseviewDF = rainfallPrediction[rainfallPrediction["Amount of annual Rainfall"] == "Terrible View"]
# elif choice == 'Poor View':
#     houseviewDF = rainfallPrediction[rainfallPrediction["Amount of annual Rainfall"] == "Poor View"]
# elif choice == 'Average View':
#     houseviewDF =rainfallPrediction[rainfallPrediction["Amount of annual Rainfall"] == "Average View"]
# elif choice == 'Good View':
#     houseviewDF = rainfallPrediction[rainfallPrediction["Amount of annual Rainfall"] == "Good View"]
# else: # choice == 'Excellent View':
#     houseviewDF = rainfallPrediction[rainfallPrediction["Amount of annual Rainfall"] == "Excellent View"]
    
# titleBoxPlot = "Boxplot of the rainfall for Various Conditions (1 to 5 Stars) with a " + choice + ":"
# housePricefig2 = px.box(houseviewDF, x="ANNUAL", y="YEAR", 
#                            title = titleBoxPlot)
# st.plotly_chart(housePricefig2)


categoryForBarChart1 = st.radio("Which feature do you want to learn more about in the bar chart?",  ('SUBDIVISION','JAN', 'FEB',  'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV','DEC','ANNUAL','JF', 'MAM', 'JJAS','OND'))
categoryForBarChart2 = st.radio("What other feature do you want to be shown in the bar chart?", numericHouseColumnsTuple)
titleMessage3 = "Bar Graph of " + categoryForBarChart1 +" as compared to "+ categoryForBarChart2

rainfallfig3 = px.bar(rainfallPrediction, x = categoryForBarChart2, y = categoryForBarChart1, title = titleMessage3)
st.plotly_chart(rainfallfig3)

select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
if not st.sidebar.checkbox("Hide", True, key='1'):
     if select == 'Pie chart':
        st.title("First five years rainfall in the month of June")
fig = px.pie(rainfallPrediction, values=rainfallPrediction['JUN'][:5], names=rainfallPrediction['YEAR'][:5], title='Amount of Rainfall in June')
st.plotly_chart(fig)
if select=='Bar plot':
        st.title("First five subdivisions")
        fig = go.Figure(data=[
        go.Bar(name='JF', x=rainfallPrediction['SUBDIVISION'][:500], y=rainfallPrediction['JF'][:500]),
        go.Bar(name='MAM', x=rainfallPrediction['SUBDIVISION'][:500], y=rainfallPrediction['MAM'][:500]),
        go.Bar(name='JJAS', x=rainfallPrediction['SUBDIVISION'][:500], y=rainfallPrediction['JJAS'][:500]),
        go.Bar(name='OND', x=rainfallPrediction['SUBDIVISION'][:500], y=rainfallPrediction['OND'][:500])])
        st.plotly_chart(fig)
st.write("The End of the Visualization of Rainfall Prediction in India")
