# Firewall Manager

## Overview

A Flask application for managing firewalls and policies.

## Features

- Add, view, and remove firewalls
- Add, view, and delete filtering policies to a firewall
- Add, view, and remove firewall rules to a filtering policy

## Requirements

- Python 
- Flask
- SQLAlchemy
  
## Installation

1. Clone the repository

   ```bash
   git clone https://github.com/rahmedn/JouerFlux_app.git
   cd your_project_directory
2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   venv\\Scripts\\activate

3. Install dependencies

   ```bash
   pip install -r requirements.txt

  4. upgrade your database (you need to add "migrations" directory to your projet
     you can modify your databe in config.py
     
    ```bash
      flask db init
      flask db migrate -m "Initial migration"
     flask db upgrade
     
  5. Generate test data to test your application

    ```bash
      python generate_fake_data.py

6. Run your application 
   ```bash
     python run.py
   
7. Access the API at http://127.0.0.1:5000/apidocs in your browser and enjoy it ;) 

