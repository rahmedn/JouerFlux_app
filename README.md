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

## Running in Docker (Optional)

To run the application in a Docker container, follow these steps:

1. Build the Docker image from the Dockerfile:

   ```bash
   docker build -t firewall-manager .

2. Run the Docker container
   
   ```bash
   docker run -p 5000:5000 firewall-manager
   
4. Database Migration
   
- Enter the Docker container shell
   ```bash
   docker exec -it <container_id> /bin/bash

- Inside the Docker container, initialize the database migrations
  ```bash
   flask db init

- Generate a migration script
  ```bash
  flask db migrate -m "Initial migration"

 - Apply the migration to the database
    ```bash
    flask db upgrade

- Generate test data
  ```bash
  python generate_fake_data.py
5. Access the API at http://localhost:5000/apidocs in your browser.
