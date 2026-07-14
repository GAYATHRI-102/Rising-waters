# 🌊 Rising Waters – AI-Based Flood Prediction System

## Overview

Rising Waters is a machine learning application that predicts the likelihood of flooding based on rainfall and weather-related parameters. The objective of the project is to demonstrate how machine learning can assist in identifying flood-prone conditions and support early decision-making.

The project combines data preprocessing, model training, and a Flask-based web application to provide users with instant flood risk predictions.

---

## Problem Description

Floods are one of the most common natural disasters and can lead to significant damage to lives, agriculture, transportation, and infrastructure. Predicting flood risk using historical environmental data can help improve preparedness and reduce potential losses.

This project applies supervised machine learning techniques to classify whether a given set of weather conditions indicates a flood risk.

---

## Project Goals

- Build a machine learning model for flood prediction.
- Analyze historical rainfall and weather data.
- Clean and preprocess the dataset.
- Compare different classification algorithms.
- Deploy the selected model using Flask.
- Provide an easy-to-use web interface for predictions.

---

## Dataset Information

The model is trained using historical weather and rainfall records.

### Input Features

- Temperature
- Humidity
- Cloud Cover
- Annual Rainfall
- January–February Rainfall
- March–May Rainfall
- June–September Rainfall
- October–December Rainfall
- Average Rainfall
- Subdivision Rainfall

### Output

| Value | Prediction |
|-------|------------|
| 0 | No Flood |
| 1 | Flood |

---

## Technology Stack

### Programming Language

- Python 3

### Machine Learning

- Scikit-learn
- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Web Framework

- Flask

### Frontend

- HTML
- CSS
- Bootstrap

### Development Environment

- Jupyter Notebook
- Visual Studio Code

---

## Project Pipeline

The complete workflow includes:

1. Importing the dataset
2. Data cleaning
3. Exploratory Data Analysis (EDA)
4. Feature engineering
5. Data preprocessing
6. Splitting training and testing data
7. Feature scaling
8. Model training
9. Performance evaluation
10. Saving the trained model
11. Flask application development
12. Prediction through the web interface

---

## Exploratory Data Analysis

EDA was carried out to better understand the dataset before training.

The analysis included:

- Dataset information
- Statistical summary
- Missing value inspection
- Correlation analysis
- Feature distributions
- Outlier identification
- Visualizations using graphs and charts

---

## Data Preprocessing

The following preprocessing techniques were applied:

- Missing value treatment
- Handling outliers
- Feature selection
- Train-test split
- Standardization using StandardScaler

---

## Machine Learning Models Evaluated

Several classification models were tested, including:

- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- Gradient Boosting Classifier

After evaluation, the model with the best overall performance was selected for deployment.

---

## Model Evaluation

Model performance was measured using standard classification metrics such as:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

These metrics helped compare different algorithms and identify the most suitable model.

---

## Web Application Features

The Flask application allows users to:

- Enter weather and rainfall information
- Generate flood predictions instantly
- Display flood risk status
- Show appropriate recommendations based on the prediction
- Access the application through a simple and responsive interface

---

## Project Directory

```
Rising-Waters/
│
├── Application/
│   ├── app.py
│   ├── floods.save
│   ├── transform.save
│   ├── templates/
│   │   ├── home.html
│   │   ├── index.html
│   │   ├── chance.html
│   │   └── no_chance.html
│   ├── static/
│   └── requirements.txt
│
├── Data/
├── EDA.ipynb
├── Flood_Prediction.ipynb
├── README.md
└── ER_Diagram.drawio
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project folder:

```bash
cd Rising-Waters
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000/
```

---

## Application Pages

- Home Page
- Prediction Form
- Flood Prediction Result
- No Flood Prediction Result

Screenshots can be added to this section after deployment.


## Possible Improvements

Future versions of the project may include:

- Live weather API integration
- Interactive flood maps
- SMS and email notifications
- Mobile application support
- Real-time rainfall monitoring
- Advanced deep learning models


## Learning Outcomes

This project provided practical experience in:

- Data preprocessing
- Exploratory Data Analysis
- Classification algorithms
- Model evaluation
- Flask web development
- Machine learning model deployment
