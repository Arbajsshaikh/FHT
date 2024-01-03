import streamlit as st
import pandas as pd
import zipfile


# Specify the path to the ZIP file
zip_file_path = 'DIST_Franchise-Orders-2022-23.zip'

# Open the ZIP file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extract the contents (assuming there is only one CSV file in the ZIP)
    csv_file_name = zip_ref.namelist()[0]
    with zip_ref.open(csv_file_name) as file:
        # Read the CSV file into a DataFrame
        filtered_data = pd.read_csv(file)
# Assuming your data is stored in the 'filtered_data' DataFrame
# If not, replace 'filtered_data' with your DataFrame name
# URL='DIST_Franchise-Orders-2022-23.csv'
# For example, you can load data from a CSV file using pd.read_csv('your_data.csv')
# filtered_data = pd.read_csv(URL)

# Create a dropdown widget for selecting a District
district_dropdown = st.selectbox('Select District:', filtered_data['DISTRICT'].unique())

# Create a function to update the Shop-Code options based on the selected District
def update_shop_code_options(selected_district):
    shop_code_options = filtered_data[filtered_data['DISTRICT'] == selected_district]['Shop-Code'].unique()
    return ['All'] + list(shop_code_options)

# Create a dropdown widget for selecting a Shop-Code
shop_code_dropdown = st.selectbox('Select Shop-Code:', update_shop_code_options(district_dropdown))

# Option to update Shop-Code options based on selected District
if st.button('Update Shop-Code Options'):
    shop_code_dropdown.options = update_shop_code_options(district_dropdown)

# Display the Medicine Names and Quantities based on the selected Shop-Code
if shop_code_dropdown != 'All':
    selected_data = filtered_data[(filtered_data['DISTRICT'] == district_dropdown) & (filtered_data['Shop-Code'] == shop_code_dropdown)]
else:
    selected_data = filtered_data[filtered_data['DISTRICT'] == district_dropdown]

# Sort the data by Qty in descending order
selected_data = selected_data.sort_values(by='Qty', ascending=False)

# Display the data
st.table(selected_data[['Medicine Name', 'Qty']])
