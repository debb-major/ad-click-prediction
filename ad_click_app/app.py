from flask import Flask, render_template, request, redirect, url_for, session, flash
from dotenv import load_dotenv
import os
import pandas as pd
import joblib


# Load environment variables
load_dotenv()

# Load models
lr_model = joblib.load("models/lr_tuned_model.pkl")
rf_model = joblib.load("models/rf_tuned_model.pkl")
xgb_model = joblib.load("models/xgb_tuned_model.pkl")


# Setup Flask
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Required to use session
# This stores the prediction result temporarily so we can:
# Redirect the user
# Show the result once on '/result'
# And not show it again on refresh
# To do this safely, Flask requires a secret key.
# If 'app.secret_key' isn't set up, Flask will raise an error when 'session' is to be used.



# Home route
@app.route('/')
def home():
    return render_template('index.html', prediction=None)

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        model_choice = request.form['model_choice']  # Select model choice

        data = {
            'ad_topic_line': request.form['ad_topic_line'],
            'gender': request.form['gender'],
            'time_of_day': request.form['time_of_day'],
            'device_type': request.form['device_type'],
            'browsing_history': request.form['browsing_history'],
            'ad_position': request.form['ad_position'],
            'age_group': request.form['age_group'],
            'site_time_group': request.form['site_time_group'],
            'internet_usage_group': request.form['internet_usage_group'],
        }

        input_df = pd.DataFrame([data])

        # Load the appropriate model
        if model_choice == 'rf':
            model = rf_model
        elif model_choice == 'xgb':
            model = xgb_model
        elif model_choice == 'lr':
            model = lr_model
        else:
            flash("Invalid model selected.")
            return render_template('index.html', form_data=data, model_choice=model_choice)  # pass model_choice

        prediction = model.predict(input_df)[0]

        # Store for result page
        session['prediction'] = int(prediction)
        session['form_data'] = data
        session['model_name'] = model_choice  # store model_choice in session

        return redirect(url_for('result'))

# Handle missing fields
    except KeyError:
        flash("Please fill out all fields before submitting.")
        return render_template('index.html', form_data=request.form, model_choice=request.form.get('model_choice'))

    except Exception as e:
        flash(f"An error occurred: {str(e)}")
        return render_template('index.html', form_data=request.form, model_choice=request.form.get('model_choice')) 


@app.route('/result')
def result():
    prediction = session.pop('prediction', None)
    form_data = session.pop('form_data', None)
    model_choice = session.pop('model_name', None)  # retrieve model_choice from session

    return render_template('index.html', prediction=prediction, form_data=form_data, model_choice=model_choice)  # pass model_choice


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)