# Loan Rejection Approval Status Regression

This project is a machine learning application designed to predict the rejection or approval status of a loan application. It uses a regression model trained on historical data to make predictions based on user input. The web application is built using Flask and is designed to take various input features and provide a prediction on the loan status.

## Features

- Predict loan approval status based on multiple input features.
- User-friendly web interface for inputting features and displaying predictions.
- Utilizes Flask for the web application framework.
- Includes a pre-trained machine learning model for making predictions.

## Installation

### Prerequisites

Ensure you have the following installed on your local development environment:

- Python 3.x
- Flask
- joblib

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/ahiru60/Loan_Rejection_Approval_Status_Regression.git
    cd Loan_Rejection_Approval_Status_Regression/Loan Eligibility Regressor
    ```

2. Set up a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure the model file `Loan_Eligibility_Regressor.pkl` is in the project directory.

5. Run the Flask application:

    ```bash
    python app.py
    ```

6. Open a web browser and navigate to `http://127.0.0.1:5000` to use the application.

## Usage

### Web Interface

1. Navigate to the home page.
2. Enter the required features for prediction:
    - Credit History
    - Married
    - Property Area
    - Loan Amount
    - Gender
    - Coapplicant Income
    - Self Employed
    - Dependents
    - Loan Amount Term
    - Education
3. Click the "Predict" button to see the prediction result.

### Model

The model used in this project is a pre-trained regression model stored in `Loan_Eligibility_Regressor.pkl`. The Flask application loads this model to make predictions based on user input.

## File Structure

- `app.py`: Main Flask application file.
- `model.py`: Contains the machine learning model.
- `templates/index.html`: HTML template for the web interface.
- `requirements.txt`: Python dependencies.

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact the project maintainer at [adhirunath@gmail.com].

