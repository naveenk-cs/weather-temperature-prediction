# 🌦️ Weather Temperature Prediction for Indian Cities

A machine learning project that predicts the next day's maximum temperature for major Indian cities using historical daily weather data from 2000 to 2024.

The project uses feature engineering and a Random Forest Regression model to learn relationships between historical temperature, weather conditions, wind, precipitation, and time-based features.

## 🎯 Problem Statement

Weather conditions change over time and accurate temperature prediction can be useful for planning, agriculture, transportation, energy management, and other applications.

This project explores how machine learning can use historical weather observations to predict the next day's maximum temperature.

## 🚀 Project Objective

The main objective is to build a machine learning model that can:

- Predict the next day's maximum temperature
- Learn patterns from historical weather data
- Use lag and rolling temperature features
- Compare model performance using standard regression metrics
- Provide a reusable prediction script

## 📊 Dataset

The dataset contains daily weather observations from:

**January 1, 2000 to December 31, 2024**

### Cities

The project includes 10 major Indian cities:

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

### Main Features

- `temperature_2m_max`
- `temperature_2m_min`
- `apparent_temperature_max`
- `apparent_temperature_min`
- `precipitation_sum`
- `rain_sum`
- `weather_code`
- `wind_speed_10m_max`
- `wind_gusts_10m_max`
- `wind_direction_10m_dominant`

Additional engineered features include:

- Month
- Temperature lag 1 day
- Temperature lag 2 days
- Temperature lag 3 days
- Temperature lag 7 days
- 3-day rolling temperature
- 7-day rolling temperature

## 🧠 Machine Learning Approach

The project follows this workflow:

```text
Historical Weather Data
          ↓
Data Cleaning
          ↓
Feature Engineering
          ↓
Lag & Rolling Features
          ↓
Train/Test Split
          ↓
Model Training
          ↓
Model Evaluation
          ↓
Next-Day Temperature Prediction