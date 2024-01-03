import streamlit as st
import pandas as pd
import zipfile
import io

# Assuming your data is stored in the 'filtered_data' DataFrame
# If not, replace 'filtered_data' with your DataFrame name
ZIP_URL = 'DIST_Franchise-Orders-2022-23.zip'

# Download and extract the ZIP file
zip_file = st.download_button('Download ZIP File', ZIP_URL)
if zip_file is not None:
    with zipfile.ZipFile(io.BytesIO(zip_file)) as z:
        with z.open(z.namelist()[0]) as f:
            filtered_data = pd.read_csv(f)

# Create a dropdown widget for selecting a District
district_dropdown = st.selectbox('Select District:', filtered_data['DISTRICT'].unique())

# Function to update the Shop-Code options based on the selected District
def update_shop_code_options(selected_district):
    shop_code_options = filtered_data[filtered_data['DISTRICT'] == selected_district]['Shop-Code'].unique()
    return ['All'] + list(shop_code_options)

# Create a variable to hold the Shop-Code options
shop_code_options = update_shop_code_options(district_dropdown)

# Create a dropdown widget for selecting a Shop-Code
shop_code_dropdown = st.selectbox('Select Shop-Code:', shop_code_options)

# Option to update Shop-Code options based on selected District
if st.button('Update Shop-Code Options'):
    # Update the variable that holds the options
    shop_code_options = update_shop_code_options(district_dropdown)

# Display the Medicine Names and Quantities based on the selected Shop-Code
if shop_code_dropdown != 'All':
    selected_data = filtered_data[(filtered_data['DISTRICT'] == district_dropdown) & (filtered_data['Shop-Code'] == shop_code_dropdown)]
else:
    selected_data = filtered_data[filtered_data['DISTRICT'] == district_dropdown]

# Sort the data by Qty in descending order
selected_data = selected_data.sort_values(by='Qty', ascending=False)

# Display the data
st.table(selected_data[['Medicine Name', 'Qty']])
