# US Bank – Online Banking & Finance Tools Application

A secure and user-friendly web application built using Django that offers a suite of financial tools, account management, and a loan predictor for assessing borrowing capacity. Designed for authenticated users to manage their finances in one place.

---

## 🔧 Features

- 📟 **User Registration & Authentication**
- 🏦 **Bank Account Management**
- 📊 **Financial Tools Suite**
  - EMI Calculator
  - SIP Tool
  - Fixed Deposit (FD) Calculator
  - Recurring Deposit (RD) Calculator
  - Retirement Corpus Estimator
  - Home Loan Calculator
  - Credit Card Interest Calculator
  - Taxable Income Calculator
  - Budget Planner
  - Net Worth Calculator
- 🤖 **Loan Predictor**
  - Predicts potential loan eligibility using form inputs and machine learning
- 💡 Clean, aesthetic Bootstrap 5-based responsive design

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/ramji-ust/finance_project.git
cd finance_project
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Activate virtual environment:
# On Windows
venv\Scripts\activate

# On Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

---

## 🔐 Accessing the App

- Visit: `http://127.0.0.1:8000/`
- Register a new account or log in with existing credentials
- Upon login, you will be directed to the **Dashboard** with full tool access

---

## 📁 Project Structure

```
finance_project/
├── banking_webapp/ # Main Django app (views, models, urls, forms)
│ ├── templates/
│ │ ├── auth/ # login.html, register.html
│ │ └── banking_webapp/ # dashboard, calculator templates
│ ├── tests/ # Unit tests for Django app components
│ │ ├── test_views.py
│ │ ├── test_urls.py
│ │ ├── test_models.py
│ │ └── test_forms.py
│ └── ...
├── finance_tools/ # Custom Python module with all financial tools
│ └── finance_tools.py
├── ml_model/ # ML model for loan prediction
│ ├── loan_model.pkl
│ └── loan_estimator.ipynb
├── templates/ # base.html
├── finance_project/ # Django settings and configuration
├── db.sqlite3 # SQLite database
├── manage.py # Django project runner
└── README.md

```

---

## 🤝 Contribution

Pull requests are welcome. For significant changes, please open an issue first to discuss what you'd like to change.

---

## 📜 License

This project is licensed under the MIT License.

