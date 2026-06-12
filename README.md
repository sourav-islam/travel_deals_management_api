# ✈️ Travel Deal Management System (Flask REST API)

A modular Flask-based REST API for managing travel deals.  
This project follows a **layered architecture (Routes → Services → Database)** with proper validation, error handling, and environment-based configuration.

---

## 🚀 Features

- Create travel deals
- Retrieve all travel deals
- Retrieve single deal by ID
- Input validation with reusable logic
- Clean layered architecture
- Centralized business logic (Service layer)
- Proper HTTP status codes
- JSON-based API responses
- SQLite database integration
- Environment variable configuration (`.env`)
- Global error handling

---

## 🏗️ Project Architecture

```text
Client (Postman / Frontend)
        ↓
Routes Layer (HTTP handling)
        ↓
Service Layer (Business logic)
        ↓
Database Layer (SQLAlchemy ORM)
        ↓
SQLite Database
```
```
project/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
│
├── routes/
│   ├── __init__.py
│   └── deal_routes.py
│
├── services/
│   ├── __init__.py
│   └── deal_service.py
│
├── utils/
│   ├── __init__.py
│   └── validator.py
│
├── database/
│   ├── __init__.py
│   ├── models.py
│   └── deals.db
```
## 🛠️ Tech Stack

* **Python 3.x**
* **Flask**
* **Flask-SQLAlchemy**
* **SQLite**
* **python-dotenv**

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory:

```env
PORT=5000
DEBUG=True
DATABASE_URL=sqlite:///deals.db
```
## 📦 Installation
1. Clone Repository
```
git clone <https://github.com/sourav-islam/travel_deals_management_api.git>
cd travel_deals_management_api
```
2. Create Virtual Environment
```
python -m venv .venv
```
3. Activate Virtual Environment
Linux / macOS

```
source .venv/bin/activate
```
Windows
```
.venv\Scripts\activate
```
4. Install Dependencies
```
pip install -r requirements.txt
pip freeze > requirements.txt
```
▶️ Run Application

```
python app.py
```
## 🚀 Base URL
Server will start at: http://127.0.0.1:5000

## 🧳 Travel Deal APIs

GET    /deals/<id>  
POST   /deals  
PUT    /deals/<id>  