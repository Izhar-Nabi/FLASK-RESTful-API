# Flask CRUD RESTful API with MySQL
- This project demonstrates a simple CRUD (Create, Read, Update, Delete) application using Flask as the web framework and MySQL as the database. The application exposes a RESTful API for managing a collection of items.
## Table of Contents
- Features
- Installation
- Configuration
- Usage
- API Endpoints
# License
# Features
# Create new items
# Read existing items
# Update existing items
# Delete items
# RESTful API design
# Installation
# Prerequisites
# Python 3.x
# MySQL
# Steps
# Clone the repository:
- git clone https://github.com/yourusername/flask-crud-restful-api.git
- cd flask-crud-restful-api
# Create and activate a virtual environment:
- python -m venv venv
- source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
# Install the required packages:
# pip install -r requirements.txt
# Set up the MySQL database:

# Create a new MySQL database.

- Update the database configuration in config.py:

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/dbname'
# Initialize the database:
- flask db init
- flask db migrate
- flask db upgrade

# Configuration
- Update the config.py file with your database credentials and other configuration settings as needed.

# Usage
- Run the Flask application:

- flask run
- Access the API at http://localhost:5000.

# API Endpoints
- Create an Item

- POST /items
- Request Body: { "name": "item name", "description": "item description" }
- Response: 201 Created
- Read All Items

# GET /items
- Response: 200 OK with JSON array of items
- Read a Single Item

# GET /items/<id>
- Response: 200 OK with item JSON
- Update an Item

# PUT /items/<id>
- Request Body: { "name": "updated name", "description": "updated description" }
- Response: 200 OK
- Delete an Item

# DELETE /items/<id>
- Response: 204 No Content
# License
- This project is licensed under the MIT License. See the LICENSE file for details.
