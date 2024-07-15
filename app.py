import streamlit as st
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
locations=''
data = pd.read_csv('cleaned_data.csv')
pipe = pickle.load(open('LinearRegression.pkl','rb'))
location = sorted(data['location'].unique())
st.write("""
         ## Welcome To Predict Bangalore House Price
         """)

locations=st.selectbox('**Eneter the location**',location)

sqft=st.slider('**Enter Total Number Of Squarefeet**', max_value=30400, min_value=300)

bath = st.slider('**Enter Number of Bathroom**', max_value=16, min_value=1)

BHK = st.slider('**Enter Number Of BHK**',max_value=20, min_value=1)
pred=0

input_data = pd.DataFrame([[locations,sqft,bath,BHK]],columns=['location','total_sqft','bath','bhk'])
pred = pipe.predict(input_data)[0]*100000

st.write("### Price: ",pred)
