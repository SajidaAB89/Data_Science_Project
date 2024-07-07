# Titanic Survival Prediction Model

## Overview

The Titanic Survival Prediction Model aims to predict whether a passenger survived the Titanic disaster based on various features such as passenger class, gender, age, fare, and embarkation point. The model is built using a RandomForestClassifier and is trained on the Titanic dataset.

## Table of Contents

- [Load the dataset](#loadthedataset)
- [Installation](#installation)
- [Model Training](#model-training)
- [Model Deployment](#model-deployment)
- [License](#license)
  


### Training the Model

The training script processes the Titanic dataset, trains a RandomForestClassifier, and saves the trained model using joblib. The model can then be used to make predictions on new data.


### Predicting Survival
To use the pre-trained model for predicting survival, load the model and pass the input features:
1. pclass 
2. sex
3. age 
4. fare 
5. embarked

### Streamlit App

The repository also includes a Streamlit app that provides a user-friendly interface for predicting passenger survival. Users can input the relevant features through the app, and the model will output the prediction of whether the passenger survived or not.

### License
This project is licensed under the Apache License 2.0. See the LICENSE file for details.
