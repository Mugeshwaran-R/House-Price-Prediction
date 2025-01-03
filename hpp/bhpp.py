import streamlit as st
import pickle
import numpy as np
import sklearn

# Load the model
with open('hpp/banglore_home_prices_model.pickle', 'rb') as f:
    model = pickle.load(f)

with open('hpp/X_table.pickle', 'rb') as f:
    X = pickle.load(f)

def predict_price(location,sqft,bath,bhk):    
    loc_index = np.where(X.columns==location)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return model.predict([x])[0]

# To get locations to display in the dropdown
exclude_columns = ['total_sqft', 'bath', 'bhk']
columns = [col for col in X.columns if col not in exclude_columns]
print(columns)

# UI
st.title('Banglore Home Price Prediction')

sqft = st.text_input('Area in sqft', 1000)
bhk = st.selectbox('BHK', [1,2,3,4,5],index = None)
bath = st.selectbox('Bath', [1,2,3,4,5], index = None)
location = st.selectbox('Location', columns, index = None)

if st.button('Predict'):
    if location == ' ' or sqft == None or bath == None or bhk == None or location == None:
        st.error('Please fill all the fields')
    else:
        result = predict_price(location,sqft,bath,bhk)
        st.success('The estimated price is Rs. {} lakhs'.format(round(result,2)))

