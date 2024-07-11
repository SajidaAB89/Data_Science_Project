# Movie Rating Prediction Model

## Overview
This project is a Movie Rating Prediction Model developed during my internship at Rover Codes. The model predicts movie ratings based on various features such as genre, director, cast, and more. The project includes data analysis, preprocessing, feature engineering, model training, and deployment using a Streamlit web application.

## Features
- Data Preprocessing: Handling missing values, converting columns to numeric types, and target encoding.
- Exploratory Data Analysis: Visualizing top genres, directors, actors, and distributions of ratings, years, duration, and votes.
- Feature Engineering: Assessing feature importance using Mutual Information Gain.
- Model Training: Using Linear Regression to train the model on the dataset.
- Model Evaluation: Evaluating model performance using R-squared score and residual analysis.
- Deployment: Deploying the model using Streamlit for interactive predictions.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/movie-rating-prediction.git
    ```

2. Navigate to the project directory:
    ```bash
    cd movie-rating-prediction
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Dataset
The dataset used for this project is IMDb Movies India, which contains information about movies including genres, directors, actors, duration, year, votes, and ratings.

## Usage

1. **Data Preprocessing**:
    - Handle missing values and convert relevant columns to numeric types.
    - Target encode categorical features like Genre, Director, and Actors.

2. **Exploratory Data Analysis**:
    - Visualize the top genres, directors, and actors.
    - Analyze the distribution of ratings, years, duration, and votes.

3. **Feature Engineering**:
    - Assess feature importance using Mutual Information Gain.

4. **Model Training**:
    - Split the data into training and testing sets (70/30).
    - Train the Linear Regression model on the dataset.

5. **Model Evaluation**:
    - Evaluate the model performance using the R-squared score and residual analysis.

6. **Deployment**:
    - Save the trained model using `joblib`.
    - Deploy the model using Streamlit for interactive predictions.

## Streamlit App

1. Save the trained model:
    ```python
    import joblib
    joblib.dump(model, 'movie_rating_model.sav')
    ```

2. Create a `streamlit_app.py` file:
    ```python
    import streamlit as st
    import joblib
    import pandas as pd

    # Load the trained model
    model = joblib.load('movie_rating_model.sav')

    st.title("Movie Rating Prediction")

    genre = st.text_input("Genre")
    director = st.text_input("Director")
    actor1 = st.text_input("Actor 1")
    actor2 = st.text_input("Actor 2")
    actor3 = st.text_input("Actor 3")
    year = st.number_input("Year", min_value=1900, max_value=2024, step=1)
    votes = st.number_input("Votes", min_value=0, step=1)

    if st.button("Predict Rating"):
        input_data = pd.DataFrame({
            'Genre': [genre],
            'Director': [director],
            'Actor 1': [actor1],
            'Actor 2': [actor2],
            'Actor 3': [actor3],
            'Year': [year],
            'Votes': [votes]
        })
        rating = model.predict(input_data)
        st.write(f"Predicted Rating: {rating[0]}")

    ```

3. Run the Streamlit app:
    ```bash
    streamlit run streamlit_app.py
    ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Thanks to Rover Codes for the internship opportunity.
- Thanks to IMDb for providing the dataset.
