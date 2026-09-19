# Birthday Tracker

Birthday Tracker is a web application that allows users to store and manage birthdays in one place. I built this project while learning web development through CS50.

## Features

- Add a person's name and birthday
- View saved birthdays
- Store birthday information using SQLite
- Simple web interface for managing birthday data
- Persistent data storage

## Technologies

- Python
- Flask
- SQLite
- HTML
- CSS

## How It Works

Users can enter a person's name, birth month, and birth day through the web interface. The information is stored in a SQLite database and displayed on the application's main page.

The Flask backend handles requests and communicates with the database, while HTML and CSS are used to create the user interface.

## Project Structure

    birthday-tracker/
    ├── static/
    │   └── styles.css
    ├── templates/
    │   └── index.html
    ├── app.py
    └── birthdays.db

## About

I built this project while learning web development with CS50. It helped me practice connecting a Flask application to a SQL database and using backend data to dynamically generate a web page.
