# Flask Task Manager App

A simple **Flask-based Task Manager Web Application** that allows users to create, view, update, and delete tasks. This project demonstrates basic **Flask + SQLAlchemy + SQLite** integration with a simple HTML frontend.

---

## 🚀 Features

* Add new tasks
* View tasks in a table
* Update task status
* Delete tasks
* SQLite database integration
* Clean Flask project structure

---

## 🛠️ Tech Stack

* Python
* Flask
* SQLAlchemy
* SQLite
* HTML / CSS

---

## 📁 Project Structure

```
app/
│
├── __init__.py
├── models.py
├── routes/
│   ├── __init__.py
│   └── auth.py
|   └──tasks.py
├── static/
│   |── css/ 
|   |   └──style.css
|   |──js/
|      └──script.js
├── templates/
│   ├── base.html
│   └── login.html
|   └──register.html
|   └──tasks.html
|
├──run.py
|── requirements.txt
└── README.md
```

---

## ⚙️ Installation


### 1. Create virtual environment

```
python -m venv env
```

Activate environment:

Windows:

```
env\Scripts\activate
```

Mac/Linux:

```
source env/bin/activate
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Run the application

```
python app.py
```

---

## 🌐 Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🗄️ Database

The project uses **SQLite** database.

If database tables are missing, run:

```
python
```

Then:

```python
from app import db
db.create_all()
exit()
```

---



---

## 🎯 Learning Objectives

This project demonstrates:

* Flask routing
* HTML templates with Jinja2
* SQLAlchemy ORM
* CRUD operations
* SQLite database integration

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the project and submit pull requests.

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/Saiteja-Teja
