# File Upload Bypass Challenge

A beginner-friendly web exploitation challenge that demonstrates insecure file upload validation and unsafe server-side file execution.

## Challenge Scenario

A web application allows users to upload avatar files.

The application claims to block dangerous files, but its validation logic contains a weakness that allows bypassing file restrictions using crafted filenames.

If the uploaded file is later executed by the server, the hidden flag can be retrieved.

---

## Project Files

- `app.py` → Main vulnerable Flask application
- `uploads/` → Stores uploaded files

---

## Requirements

Install Flask:

```bash
pip install flask
```

---

## Setup Instructions

### Run the application

```bash
python app.py
```

---

## Access Challenge

Open browser:

```bash
http://127.0.0.1:5000
```

---

## Learning Objectives

- File upload bypass techniques
- Double extension attacks
- Improper file validation
- Dangerous server-side code execution
- Web exploitation fundamentals

---

## Warning

This challenge is intentionally vulnerable and designed for local educational use only.
Do not deploy this application in production environments.
