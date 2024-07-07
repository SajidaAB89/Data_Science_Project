# # Loading Modules

# import joblib
# import pandas as pd
# import streamlit as st

# # Load the dataset
# data = pd.read_csv("Titanic.csv")


# # Load the Models
# le = joblib.load("Titanic/le.sav")
# model2 = joblib.load("Titanic/model2.sav")
# tuning = joblib.load("Titanic/tuning.sav")


# st.sidebar.header("Input Parameters")

# pclass = st.sidebar.number_input("Enter passenger's class:" , 0.0, 10.0, 5.0)
# sex = st.sidebar.number_input("Enter the Sex: ", 0.0, 10.0, 5.0)
# age = st.sidebar.number_input("Enter the Age: ", 0.0, 10.0, 5.0)
# fare = st.sidebar.number_input("Enter the Fare: ", 0.0, 10.0, 5.0)
# embarked = st.sidebar.number_input("Enter if passenger embarked: ", 0.0, 10.0, 5.0)

# # new_data = [[2.5, 4.7, 5.2, 8.2]]

# new_data = [[pclass, sex, age, fare, embarked]]
# new_scaled_data = le.transform(new_data)

# prediction = model2.predict(new_scaled_data)  # 0, 1, 2
# encoded_prediction = tuning.inverse_transform(prediction)


# st.write("""
#          # Titanic SURVIVAL PREDICTION
#          This app predicts if the passenger on **Titanic** survived or not!
#          """)

# st.write(data)

# st.write("""
#          ## Prediction 
#          The passenger:
#          """)

# st.write(encoded_prediction[0])
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model

le = joblib.load("Titanic/le.sav")
model2 = joblib.load("Titanic/model2.sav")
tuning = joblib.load("Titanic/tuning.sav")


st.title("Titanic Survival Prediction 🌊🚢")

# Create input fields for user to enter details
pclass = st.selectbox("Pclass", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 100, 30)
fare = st.slider("Fare", 0, 500, 50)
embarked = st.selectbox("Embarked", ["C", "Q", "S"])

# Encode the inputs to match the model
sex = 1 if sex == "male" else 0
embarked = {"C": 1, "Q": 2, "S": 0}[embarked]

# Create input data for the model
input_data = np.array([[pclass, sex, age, fare, embarked]])

# Make prediction
if st.button("Predict"):
    prediction = tuning.predict(input_data)
    if prediction[0] == 1:
        st.success("Survived")
    else:
        st.error("Not Survived")