# CSRF Profile Change Challenge

A beginner-friendly web exploitation challenge demonstrating Cross-Site Request Forgery (CSRF).

## Scenario

A user profile page allows users to change their email address.

The application does not implement CSRF protection, allowing attackers to force authenticated users to perform unwanted actions.

Your objective is to exploit the vulnerability and change the email to retrieve the hidden flag.

---

## Requirements

Install Flask:

```bash
pip install flask
```

---

## Setup

Run:

```bash
python app.py
```

---

## Access Challenge

Open:

```bash
http://127.0.0.1:5000
```

---

## Learning Objectives

- CSRF attacks
- Missing CSRF token protection
- Forced authenticated actions
- Web exploitation fundamentals

---

## Warning

For educational purposes only.
