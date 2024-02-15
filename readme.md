# Django Project Name

Welcome to the jwt-auth-wolfpack project! This project is built using Django, a high-level Python web framework. 

## Installation

To run this project locally on a Windows environment, follow these steps:

### 1. Clone the Repository

Clone this repository to your local machine. You can use Git Bash or any Git GUI tool for this purpose. Open Git Bash and run the following command:

```sh
git clone https://github.com/fkhan999/jwt-auth-wolfpack.git
```

### 2. Navigate to the Project Directory
Open Command Prompt (cmd) and navigate into the project directory
```sh
cd django-project-name
```
### 3. Set Up a Virtual Environment
It's best practice to use a virtual environment to isolate project dependencies. You can create and activate a virtual environment using the following commands:

# Create virtual environment
```sh
python -m venv env

```


# Activate virtual environment
```sh
source \env\Scripts\activate

```
### 4. Install Dependencies
Install the project dependencies listed in the requirements.txt file:

```sh
pip install -r requirements.txt
```
### 5. Set Up Database
Run following comnmond to setup db
```sh
python manage.py makemigrations
python manage.py migrate
```
### 6. Run the Development Server
Start the Django development server:
```sh
python manage.py runserver
```
### 7. Access the Application
Once the development server is running, you can access the api in testing tool like postman, thunderclient etc.
at http://localhost:8000/.


