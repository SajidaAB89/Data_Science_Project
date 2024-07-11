import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("prediction_model/movie_rating_model.sav")
mse = joblib.load("prediction_model/mean_squared_error.sav")
score = joblib.load("prediction_model/r_square_value.sav")

# Load the dataset for target encoding
data = pd.read_csv("IMDb Movies India.csv", encoding="latin")

# Preprocess the dataset for target encoding
data["Duration"] = data["Duration"].str.replace(" min", "").astype(float)
data["Year"] = data["Year"].str.strip("()").astype(float)
data["Votes"] = (
    data["Votes"]
    .str.replace(",", "")
    .str.replace("$5.16M", "516", regex=False)
    .astype(float)
)
data["Duration"].fillna(data["Duration"].median(), inplace=True)
data["Rating"].fillna(data["Rating"].mean(), inplace=True)
data["Votes"].fillna(data["Votes"].median(), inplace=True)
data.dropna(
    subset=[
        "Name",
        "Year",
        "Genre",
        "Director",
        "Actor 1",
        "Actor 2",
        "Actor 3",
    ],
    inplace=True,
)
data["Genre"] = data["Genre"].str.split(",").explode("Genre").reset_index(drop=True)

# Define the input fields for the Streamlit app
st.title("Movie Rating Prediction 🎬🍿")

st.write("Please input the following details to predict the movie rating:")

name = st.text_input("Movie Name:")
year = st.number_input("Year", min_value=1900, max_value=2100, step=1)
genre = st.text_input("Genre:")
votes = st.number_input("Votes", min_value=0, step=1)
director = st.text_input("Director")
actor1 = st.text_input("Actor 1")
actor2 = st.text_input("Actor 2")
actor3 = st.text_input("Actor 3")


# Process the inputs and make a prediction
if st.button("Predict Rating"):
    # Create a DataFrame for the inputs
    input_data = pd.DataFrame(
        {
            "Name": [name],
            "Year": [year],
            "Genre": [genre],
            "Votes": [votes],
            "Director": [director],
            "Actor 1": [actor1],
            "Actor 2": [actor2],
            "Actor 3": [actor3],
        }
    )

    # Perform target encoding for the inputs

    input_data["Name"] = input_data["Name"].map(data.groupby("Name")["Rating"].mean())
    input_data["Genre"] = input_data["Genre"].map(
        data.groupby("Genre")["Rating"].mean()
    )
    input_data["Director"] = input_data["Director"].map(
        data.groupby("Director")["Rating"].mean()
    )
    input_data["Actor 1"] = input_data["Actor 1"].map(
        data.groupby("Actor 1")["Rating"].mean()
    )
    input_data["Actor 2"] = input_data["Actor 2"].map(
        data.groupby("Actor 2")["Rating"].mean()
    )
    input_data["Actor 3"] = input_data["Actor 3"].map(
        data.groupby("Actor 3")["Rating"].mean()
    )

    # Handle any NaN values that result from the mapping
    input_data.fillna(0, inplace=True)

    # Make a prediction
    prediction = model.predict(input_data)

    # Display the prediction
    st.write(f"The predicted movie rating is: {prediction[0]:.2f}")
