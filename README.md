BigMart Sales Prediction using Machine Learning

📌 Project Overview

The BigMart Sales Prediction project is an end-to-end Machine Learning application designed to predict the sales of products in BigMart outlets based on product and outlet characteristics. This project demonstrates the complete machine learning workflow, including data preprocessing, exploratory data analysis (EDA), feature engineering, model training, model evaluation, and deployment using Streamlit.

The objective is to help retailers estimate future product sales, enabling better inventory management and business decision-making.


---

🎯 Objectives

Perform data preprocessing and cleaning.

Analyze the dataset using visualizations.

Train and compare multiple machine learning models.

Predict product sales accurately.

Develop an interactive web application using Streamlit.

Deploy a user-friendly prediction system.



---

📂 Dataset

Dataset Name: BigMart Sales Prediction Dataset

Source: Kaggle

The dataset contains information about various products sold in BigMart outlets.

Features

Item Identifier

Item Weight

Item Fat Content

Item Visibility

Item Type

Item MRP

Outlet Identifier

Outlet Establishment Year

Outlet Size

Outlet Location Type

Outlet Type


Target Variable

Item_Outlet_Sales



---

🛠 Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Streamlit

Pickle

VS Code

Git & GitHub



---

📊 Exploratory Data Analysis

The project includes comprehensive data visualization techniques to understand the dataset.

Visualizations include:

Missing Value Heatmap

Sales Distribution

Item Type Analysis

Outlet Type Distribution

Outlet Size Analysis

Correlation Heatmap

Sales by Outlet Type

Sales by Item Type

Sales by Outlet Location

Feature Relationship Analysis



---

🤖 Machine Learning Models

The following regression algorithms are implemented and compared:

Linear Regression

Decision Tree Regressor

Random Forest Regressor


Evaluation Metrics:

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

Root Mean Squared Error (RMSE)

R² Score


The best-performing model is saved using Pickle and integrated into the Streamlit application.


---

🌐 Streamlit Application Features

The application provides a clean and interactive user interface.

Home Page

Project overview

Introduction

Objectives


Dashboard

Dataset preview

Dataset statistics

Interactive visualizations


Sales Prediction

Users can enter product and outlet details to predict the expected sales instantly.

About Page

Contains project information, technologies used, machine learning workflow, and developer details.


---

📁 Project Structure

BigMart-Sales-Prediction/

│── dataset/
│   ├── Train.csv
│   └── Test.csv
│
│── models/
│   └── model.pkl
│
│── app.py
│── train_model.py
│── requirements.txt
│── README.md
│── .gitignore


---

⚙ Installation

Clone the repository:

git clone https://github.com/yourusername/BigMart-Sales-Prediction.git

Navigate to the project folder:

cd BigMart-Sales-Prediction

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py


---

📈 Results

Successfully cleaned and preprocessed the BigMart dataset.

Performed detailed exploratory data analysis.

Compared multiple machine learning algorithms.

Achieved accurate sales prediction using the best-performing model.

Developed an interactive Streamlit web application for real-time predictions.



---

🚀 Future Enhancements

Hyperparameter tuning for improved model accuracy.

Integration with a SQL database.

Deployment on Streamlit Community Cloud or Render.

Advanced business analytics dashboard.

Sales forecasting for multiple years.

User authentication and prediction history.



---

📚 Learning Outcomes

Through this project, the following skills were developed:

Data Cleaning and Preprocessing

Exploratory Data Analysis

Feature Engineering

Machine Learning Model Development

Model Evaluation

Model Deployment using Streamlit

Data Visualization

Git and GitHub Version Control

Professional Project Development



---

👩‍💻 Author

Niharika Medipally

B.Tech – Artificial Intelligence and Machine Learning (AIML)

This project was developed as part of a Machine Learning portfolio to demonstrate practical knowledge in data analysis, predictive modeling, and web application development.


---

📜 License

This project is intended for educational and portfolio purposes. The BigMart dataset is used solely for academic learning and demonstration.
