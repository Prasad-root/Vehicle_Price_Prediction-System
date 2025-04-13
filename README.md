# Vehicle Price Prediction Using Machine Learning

This project is a machine learning-based vehicle price prediction system that utilizes data scraped from **[riyasewana.lk](https://riyasewana.lk)** and **[ikman.lk](https://ikman.lk)**. The goal is to predict the market value of used vehicles in Sri Lanka based on features like **brand**, **model**, **mileage**, and **other specifications**.

## 🚗 Project Overview

Many buyers and sellers struggle to determine the accurate value of a used vehicle. This project aims to solve that problem using machine learning techniques. The model is trained on real-world data scraped from popular Sri Lankan vehicle listing sites and can predict a fair price for a used vehicle based on its features.

## 🔍 Features

- Web scraping from **riyasewana.lk** and **ikman.lk**
- Data cleaning and preprocessing
- Feature engineering
- Model training and evaluation
- Price prediction using regression algorithms
- Custom dataset creation from live listings

## 🛠️ Tech Stack

- Python
- BeautifulSoup (for web scraping)
- Pandas / NumPy (for data processing)
- Scikit-learn / XGBoost (for ML modeling)
- Matplotlib / Seaborn (for visualization)
- Jupyter Lab

## 📊 Dataset

The dataset was created by scraping publicly available data from:

- [riyasewana.lk](https://riyasewana.lk)
- [ikman.lk](https://ikman.lk)

It has been cleaned and organized into a custom dataset, now available on Kaggle:

📥 **[Download the Dataset on Kaggle](https://www.kaggle.com/datasets/prasadnirmal/srilankan-second-vehiclecar-price-dataset)**

### Dataset Features:

- `Brand`
- `Model`
- `Year`
- `Mileage`
- `Transmission`
- `Fuel Type`
- `Engine Capacity`
- `Condition`
- `Location`
- `Features` (optional extras like Airbags, ABS, etc.)
- `Price` (target variable)

## 🧠 ML Models Used

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor (best performance)
- SVM
  
Model evaluation metrics:

- MSE (Mean Squared Error)
- MAE (Mean Absolute Error)
