# IDOR Ticket Challenge

A beginner-friendly web exploitation challenge that demonstrates an **Insecure Direct Object Reference (IDOR)** vulnerability.

## Challenge Scenario

A ticket viewing system allows users to access ticket information using an ID parameter.

Example:

```bash
/ticket?id=1
```

The application fails to enforce proper authorization checks, allowing attackers to enumerate ticket IDs and access restricted data.

One hidden ticket contains the flag.

---

## Project Files

- `app.py` → Vulnerable Flask application

---

## Requirements

Install Flask:

```bash
pip install flask
```

---

## Setup Instructions

Run the application:

```bash
python app.py
```

---

## Access Challenge

Open browser:

```bash
http://127.0.0.1:5000
```

Try accessing:

```bash
/ticket?id=1
```

---

## Learning Objectives

- Understand IDOR vulnerabilities
- Broken access control
- Parameter manipulation
- Enumeration attacks
- Web exploitation basics

---

## Warning

This challenge is intentionally vulnerable and created for local educational testing only.
Do not deploy this application in production environments.
