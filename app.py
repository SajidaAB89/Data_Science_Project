#Loading Modules

import joblib
import pandas as pd
import streamlit as st

# Load the dataset
iris_df = pd.read_csv("IRIS.csv")


# Load the Models
knn_model = joblib.load("Persistence/knn_model.sav")
scalar = joblib.load("Persistence/scaler_features.sav")
encoder = joblib.load("Persistence/label_encoder.sav")


st.sidebar.header("Input Parameters")
sl = st.sidebar.slider("Select Sepal Length", 0.0, 10.0, 5.0)
sw = st.sidebar.slider("Select Sepal Width", 0.0, 10.0, 5.0)
pl = st.sidebar.slider("Select Petal Length", 0.0, 10.0, 5.0)
pw = st.sidebar.slider("Select Petal Width", 0.0, 10.0, 5.0)

# new_data = [[2.5, 4.7, 5.2, 8.2]]

new_data = [[sl, sw, pl, pw]]
new_scaled_data = scalar.transform(new_data)

prediction = knn_model.predict(new_scaled_data)  # 0, 1, 2
encoded_prediction = encoder.inverse_transform(prediction)


    

st.write("""
         # Iris Flower Classification  
         This app predicts the **Iris Flower** type!
         """)

st.write(iris_df)

st.write("""
         ## Prediction 
         The predicted flower is:
         """)

st.write(encoded_prediction[0])
