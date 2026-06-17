# Business Dashboard

A full-stack Business Dashboard built using FastAPI, MySQL, HTML, Bootstrap and Chart.js.

## Features

* Dashboard analytics with summary cards
* Total Businesses, Total Cities and Total Categories count
* Businesses by Category bar chart
* Businesses by City pie chart
* Add new business records
* Search businesses by city and category
* REST API integration using FastAPI
* MySQL database connectivity

## Tech Stack

### Backend

* Python
* FastAPI
* MySQL

### Frontend

* HTML
* Bootstrap 5
* JavaScript
* Chart.js

## Project Structure

business-dashboard/

├── backend/

├── frontend/

├── scripts/

├── business_data.csv

└── README.md

## Setup Instructions

### 1. Clone Repository

git clone https://github.com/guptashambhavi-930/business-dashboard.git

### 2. Install Dependencies

pip install fastapi uvicorn mysql-connector-python pandas

### 3. Start Backend

cd backend

python -m uvicorn main:app --reload

### 4. Run Frontend

Open index.html using Live Server in VS Code.

## API Endpoints

* GET /businesses
* GET /total-count
* GET /city-count
* GET /category-count
* GET /filter
* POST /add-business

## Challenges Faced

* Connecting FastAPI with MySQL database
* Integrating frontend with backend APIs
* Creating interactive charts using Chart.js
* Managing and visualizing business data efficiently

## Author

Shambhavi Gupta
BCA (DS & AI)
