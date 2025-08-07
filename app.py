# app.py

import streamlit as st
import joblib 
import numpy as np

# Set up page
st.set_page_config(page_title='Sales Prediction', page_icon='📈')

# Load the model
model = joblib.load('model.pkl')

st.title('📊 Sales Prediction App')
st.write('This app predicts sales revenue based on your input features.')

# Mappings for categorical features
Product_Category_map = {'Electronics': 0, 'Clothing': 1, 'Grocery': 2, 'Furniture': 3}
Store_Location_map = {'Urban': 0, 'Suburban': 1, 'Rural': 2}

# Input UI
selected_product_category = st.selectbox('Product Category', list(Product_Category_map.keys()))
selected_store_location = st.selectbox('Store Location', list(Store_Location_map.keys()))

STORE_ID = st.number_input('Store ID', min_value=0, max_value=100, step=1)
PRODUCT_ID = st.number_input('Product ID', min_value=1000, max_value=1100, step=1)
UNITS_SOLD = st.number_input('Units Sold', min_value=0, step=1)
UNIT_PRICE = st.number_input('Unit Price', min_value=0.0, step=10.0)
DISCOUNT = st.number_input('Discount', min_value=0.0, max_value=0.3, step=0.01)
ADVERTISING_EXPENSE = st.number_input('Advertising Expense', min_value=0.0, step=100.0)
HOLIDAY_SEASON = st.selectbox('Holiday Season', ['Yes', 'No'])
HOLIDAY_SEASON = 1 if HOLIDAY_SEASON == 'Yes' else 0

# Map categories to numeric
PRODUCT_CATEGORY = Product_Category_map[selected_product_category]
STORE_LOCATION = Store_Location_map[selected_store_location]

# Predict
if st.button("Predict Sales Revenue"):
    input_data = np.array([[STORE_ID, PRODUCT_ID, PRODUCT_CATEGORY, STORE_LOCATION,
                            UNITS_SOLD, UNIT_PRICE, DISCOUNT,
                            ADVERTISING_EXPENSE, HOLIDAY_SEASON]])
    
    prediction = model.predict(input_data)
    prediction_value = float(prediction.flatten()[0]) # Convert to float for display
    st.success(f"💰 Predicted Sales Revenue: ₹{prediction_value:,.2f}") # Display prediction with ₹ symbol and two decimal places
