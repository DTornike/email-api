# Project Setup Instructions

## Introduction
This guide will help you set up and run the Django project locally on your machine. Follow the steps below to install the necessary dependencies, configure the environment, and get the server up and running.

## Prerequisites
- **Python 3.8+**
- **pip** (Python package installer)
- **PostgreSQL**
- **Git**

## Installation Steps

### 1. Clone the Repository
Clone the GitHub repository to your local machine using the command below:

```bash
git clone <repository-url>
cd <repository-folder>
```

Replace `<repository-url>` with the actual URL of the GitHub repository and `<repository-folder>` with the folder name of your choice.

### 2. Set Up Virtual Environment
Create and activate a virtual environment to keep the project dependencies isolated:

```bash
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

### 3. Install Dependencies
Install the required packages listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add the required environment variables. Here is an example of the variables you might need to set:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Update the values as per your configuration and secret key requirements.

### 5. Set Up the Database
Run the following commands to set up the database:

install postgresql and update credentials in `email_api/settings.py`

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Optional)
To access the Django admin interface, you can create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your superuser credentials.

### 7. Run the Server
Start the development server:

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`. You can now access the application in your browser.

## License
This project is licensed under the MIT License.

