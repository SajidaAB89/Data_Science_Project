# Iris Flower Classification Prediction Model

This repository contains a Streamlit application that predicts the species of Iris flowers based on their sepal and petal measurements. The Iris flower dataset consists of three species: setosa, versicolor, and virginica, which can be distinguished based on their measurements. The objective is to train a machine learning model that can accurately classify the Iris flowers into their respective species.

## Dataset

The Iris dataset contains 150 samples of iris flowers categorized into three species:
- **Setosa**
- **Versicolor**
- **Virginica**

Each sample contains four features:
- **Sepal length** (cm)
- **Sepal width** (cm)
- **Petal length** (cm)
- **Petal width** (cm)

## Objective

The goal is to develop a machine learning model that can classify iris flowers into different species based on their sepal and petal measurements. This dataset is widely used for introductory classification tasks.

## Streamlit Application

The application uses a K-Nearest Neighbors (KNN) model to predict the species of an Iris flower based on user-provided sepal and petal measurements.

### Loading Modules

- **joblib**: For loading the pre-trained model and scaler.
- **pandas**: For loading the dataset.
- **streamlit**: For creating the web application.

### Steps Performed in the Application

1. **Load the Dataset**:
   The Iris dataset is loaded from a CSV file.

2. **Load the Models**:
   The pre-trained KNN model, feature scaler, and label encoder are loaded using `joblib`.

3. **User Input**:
   The user provides input for sepal length, sepal width, petal length, and petal width using Streamlit sliders.

4. **Data Transformation**:
   The user input is scaled using the loaded scaler.

5. **Prediction**:
   The KNN model predicts the species of the Iris flower based on the scaled user input. The prediction is then decoded using the label encoder to get the species name.

6. **Display**:
   The dataset and prediction results are displayed in the Streamlit app.

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

### Explanation
- **Dataset**: Brief description of the dataset and its features.
- **Objective**: The goal of the project.
- **Streamlit Application**: High-level overview of the steps performed in the Streamlit app.
- **How to Run the Application**: Instructions to set up and run the Streamlit application.
- **Example**: Example of user input and the resulting prediction.
- **File Structure**: Overview of the repository's file structure.
- **Contributing**: Guidelines for contributing to the project.
- **License**: Licensing information.

