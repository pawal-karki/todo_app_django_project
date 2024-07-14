# Django To-Do App

This is a simple To-Do application built with Django.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have Python 3.7+ installed.
- You have Django 3.0+ installed.
- You have pip (Python package installer) installed.
- You have a virtual environment tool like `virtualenv` or `venv` installed.

## Installation

1. Clone the repository:

    ```sh
    git clone **https://github.com/pawal-karki/todo_app_django_project**
    cd django-todo-app
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate #for mac/Linux
    # On Windows use `venv\Scripts\activate`
    
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply the database migrations:**

    ```sh
    python manage.py migrate
    ```

5. Create a superuser (optional but recommended for admin access):

    ```sh
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```sh
    python manage.py runserver
    ```
