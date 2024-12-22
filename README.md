# Django Login Application

This is a simple Django web application demonstrating a basic login system. It includes two screens:
1. A login page where users can input a username and password.
2. A welcome page that greets the user with their username after form submission.

---

## Features
- **Login Form**: A form with fields for username and password.
- **Welcome Page**: Displays a personalized greeting message using the entered username.
- **CSRF Protection**: Implements Django's built-in protection against cross-site request forgery.

---

## Technology Stack
- **Backend**: Django 
- **Frontend**: HTML5, CSS3
- **Language**: Python 

---

## Prerequisites
Before running this application, make sure you have the following installed:
- Python
- Django (install using `pip install django`)

---

## Setup Instructions

1. Clone this repository:
   ```cmd
   git clone https://github.com/yourusername/django-login-app.git
   cd django-login-app
   ```
2. Create and activate a virtual environment:
   ```cmd
   python -m venv env
   env\Scripts\activate
   ```
3. Install dependencies:
   ```cmd
   pip install django
   ```
4. Run database migrations:
   ```cmd
   python manage.py migrate
   ```
5. Start the development server:
   ```cmd
   python manage.py runserver
   ```
6. Open the application in your browser:
   ```cmd
   http://127.0.0.1:8000/
   ```

