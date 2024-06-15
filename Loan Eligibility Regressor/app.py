
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('Loan_Eligibility_Regressor.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    dependents_0 = 0.0
    dependents_1 = 0.0
    dependents_2 = 0.0
    dependents_3P = 0.0

    if request.form['Dependents'] == 0:
        dependents_3P = 1.0
    elif request.form['Dependents'] == 1:
        dependents_2 = 1.0
    elif request.form['Dependents'] == 2:
        dependents_1 = 1.0
    elif request.form['Dependents'] == 3:
        dependents_0 = 1.0

    Property_Area_Rural = 0.0
    Property_Area_Semiurban = 0.0
    Property_Area_Urban = 0.0

    if request.form['Property_Area'] == 0:
        Property_Area_Rural = 1.0
    elif request.form['Property_Area'] == 1:
        Property_Area_Semiurban = 1.0
    elif request.form['Property_Area'] == 2:
        Property_Area_Urban = 1.0

    # Get input data from the form
    features = [
        float(request.form['Gender']),
        float(request.form['Married']),
        float(request.form['Education']),
        float(request.form['Self_Employed']),
        float(request.form['CoapplicantIncome']),
        float(request.form['LoanAmount']),
        float(request.form['Loan_Amount_Term']),
        float(request.form['Credit_History']),
        dependents_0,
        dependents_1,
        dependents_2,
        dependents_3P,
        Property_Area_Rural,
        Property_Area_Semiurban,
        Property_Area_Urban,
        0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

    prediction = model.predict([features])

    if prediction == 0.0:
        return render_template('result.html', prediction="Rejected")
    if prediction == 1.0:
        return render_template('result.html', prediction="Approved")

if __name__ == '__main__':
    app.run(debug=True)
