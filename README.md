# Weather Temperature Prediction

A machine learning project that predicts the next day's maximum temperature using historical daily weather data from major Indian cities.

## Project Overview

This project uses historical weather data from 2000 to 2024 to train a machine learning model for next-day maximum temperature prediction.

The project includes data preprocessing, feature engineering, model training, evaluation, and a prediction script for using the trained model.

## Dataset

The dataset contains daily weather observations for 10 major Indian cities:

- Delhi
- Mumbai
- Kolkata
- Chennai
- Bangalore
- Hyderabad
- Ahmedabad
- Pune
- Jaipur
- Lucknow

### Dataset Details

- Period: 2000-01-01 to 2024-12-31
- Total records: ~91,320
- Target: Next-day maximum temperature
- Data frequency: Daily

## Machine Learning Model

The project uses a **Random Forest Regressor**.

### Features

The model uses weather and historical temperature features including:

- Maximum temperature
- Minimum temperature
- Apparent maximum temperature
- Apparent minimum temperature
- Precipitation
- Weather code
- Maximum wind speed
- Maximum wind gusts
- Dominant wind direction
- Month
- Temperature lag features
- Rolling temperature features

## Model Performance

The Random Forest model achieved approximately:

| Metric | Score |
|---|---:|
| MAE | 0.924°C |
| RMSE | 1.276°C |
| R² Score | 0.929 |

The model's R² score of approximately 0.93 indicates that it explains a large portion of the variation in next-day maximum temperature.

## Project Structure

```text
weather-temperature-prediction/
│
├── data/
│   └── india_2000_2024_daily_weather.csv
│
├── models/
│   └── weather_temperature_model.pkl
│
├── notebooks/
│   └── weather_temperature_prediction.ipynb
│
├── src/
│   └── predict.py
│
├── .gitignore
├── README.md
└── requirements.txt