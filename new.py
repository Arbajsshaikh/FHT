import streamlit as st
import pandas as pd
import zipfile
import io

# Assuming your data is stored in the 'filtered_data' DataFrame
# If not, replace 'filtered_data' with your DataFrame name
URL='DIST_Franchise-Orders-2022-23.zip'
# For example, you can load data from a CSV file using pd.read_csv('your_data.csv')
filtered_data = pd.read_csv(URL)

# Display the Medicine Names and Quantities based on the selected Shop-Code
if shop_code_dropdown != 'All':
    selected_data = filtered_data[(filtered_data['DISTRICT'] == district_dropdown) & (filtered_data['Shop-Code'] == shop_code_dropdown)]
else:
    selected_data = filtered_data[filtered_data['DISTRICT'] == district_dropdown]

# Sort the data by Qty in descending order
selected_data = selected_data.sort_values(by='Qty', ascending=False)

# Display the data
st.table(selected_data[['Medicine Name', 'Qty']])
