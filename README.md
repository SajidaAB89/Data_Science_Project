Introducing My Movie Rating Prediction Model

I'm excited to share the completion of my latest project—a Movie Rating Prediction Model. Developed during my internship at Rover Codes, this model leverages machine learning to predict movie ratings based on various features such as genre, director, cast, and more. Here's a brief overview of the process:

Data Analysis & Preprocessing
Dataset: IMDb Movies India.
Preprocessing: Handled missing values, converted relevant columns to numeric types, and performed target encoding for categorical features.
Exploratory Analysis: Visualized top genres, directors, and actors, and analyzed the distribution of ratings, years, duration, and votes.
Feature Engineering
Target Encoding: Encoded features like Genre, Director, and Actors based on their average ratings.
Mutual Information Gain: Assessed feature importance to select the most significant predictors.
Model Training
Model: Linear Regression.
Training & Testing: Split the data into training and testing sets (70/30).
Performance Evaluation: Achieved a promising R-squared score and analyzed residual errors.
Deployment
Saving the Model: Exported the trained model using joblib.
Streamlit App: Deployed an interactive web application where users can input movie features to get predicted ratings.
