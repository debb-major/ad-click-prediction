# Ad Click Prediction Web App

This is a machine learning-powered web application that predicts whether a user will click on an advertisement based on their personal and browsing data. Built using Flask and deployed on Render, the app allows users to interactively input data and receive real-time predictions.

## Live Demo
[View App on Render](https://ad-click-predictor.onrender.com/)

## Features

- Predicts ad click likelihood using three trained ML models:
  - Random Forest
  - XGBoost
  - Logistic Regression
- User input form with dropdowns and grouped input ranges (age, internet usage, time on site)
- Model selection by user
- Clean UI with real-time feedback
- Handles text input via TF-IDF
- Pipeline-powered preprocessing and inference

## Tech Stack

- Python
- Flask
- scikit-learn
- XGBoost
- pandas, NumPy
- TfidfVectorizer
- HTML + CSS (Jinja templates)

## Project Structure

```bash
ad-click-app/
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── Procfile # For Render deployment
├── templates/
│ └── index.html # Web interface
├── models/
│ └── rf_tuned_model.pkl
│ └── xgb_tuned_model.pkl
│ └── lr_tuned_model.pkl
└── README.md
```

## Model Training Overview

- Preprocessed data by encoding categorical features and binning continuous ones
- Applied TF-IDF vectorization to ad headline
- Trained and fine-tuned models using GridSearchCV
- Evaluated using Accuracy, Precision, Recall, F1, and ROC-AUC

## How to Run Locally


### Create virtual environment (optional)
```bash
python -m venv venv
source venv/bin/activate    # on Windows: venv\Scripts\activate
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Run app
```bash
python app.py
```

## Deployment (Render)

1. Create a free Render account

2. Connect your GitHub repo

3. Add ```requirements.txt``` and ```Procfile``` to root directory

4. Use ```gunicorn app:app``` as the start command

5. Deploy

## Sample Output

Predictions returned as either ```likely Clicked``` or ```likely Not Clicked``` with result displayed on the app interface after user input.

## Author

### Deborah Olatona
Aspiring ML Engineer | Biochemistry BSc | https://medium.com/@devdebb
