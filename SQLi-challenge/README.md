# SQL Injection CTF Challenge

A beginner-friendly web exploitation challenge built with Flask and SQLite that demonstrates SQL Injection vulnerabilities in authentication systems.

## Challenge Scenario

A login portal contains an insecure SQL query implementation. Your objective is to analyze the vulnerability and bypass authentication to retrieve the hidden flag.

---

## Project Files

- `app.py` → Vulnerable Flask login application
- `setup_db.py` → Database initialization script
- `database.db` → Generated SQLite database

---

## Requirements

Install dependencies:

```bash
pip install flask
```

---

## Setup Instructions

### 1. Create database

```bash
python setup_db.py
```

This creates:

- SQLite database
- users table
- sample credentials

---

### 2. Run application

```bash
python app.py
```

---

### 3. Access challenge

Open browser:

```bash
http://127.0.0.1:5000
```

---

## Learning Objectives

- Understand SQL Injection
- Authentication bypass techniques
- Insecure query handling
- Web exploitation fundamentals

---

## Disclaimer

This project is created for educational purposes and local security training only.
