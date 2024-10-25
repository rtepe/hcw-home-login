# Healthcare Worker At Home - Login Page Design

A simple login and signup page for **Healthcare Worker At Home**, built using Flask. This project provides a clean and user-friendly interface for healthcare workers to log in or sign up.

## Features

- **Login**: Allows users to log in with predefined credentials.
- **Signup**: Supports new user registration and provides feedback if the email already exists.
- **JSON/Form Support**: Handles both JSON payloads (for API/AJAX) and traditional form data.
- **Dashboard**: Placeholder dashboard view for successful login.

## Project Structure

```
.
├── app.py                  # Main Flask application file
├── templates/
│   └── login.html          # HTML template for login/signup forms
└── README.md               # Project documentation
```

## Prerequisites

- Python 3.x
- Flask

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd healthcareworker-at-home-login
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install flask
   ```

## Usage

### Running the Application

1. **Start the Flask server**:
   ```bash
   flask run
   ```

2. **Access the app**:
   Open `http://127.0.0.1:5050/` in your web browser to view the login and signup forms.

### Login

- Use the **login form** on the homepage.
- **Predefined credentials**:
  - **Email**: `admin@admin.com`
  - **Password**: `password`
- Successful login redirects to the dashboard page.

### Signup

- Use the **signup form** on the homepage.
- If the email does not already exist, registration will be successful, allowing you to log in.

## Customization

- **Authentication Logic**: The current setup uses hardcoded credentials for login. For production use, integrate a database for real user management.
- **Styling**: Customize `login.html` with additional styling to align with branding or design requirements.


---

This README gives an overview of the setup, configuration, and usage tailored to the **Healthcare Worker At Home** login design. Let me know if further adjustments are needed!