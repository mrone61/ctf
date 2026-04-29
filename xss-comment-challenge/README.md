# XSS Comment Challenge

A beginner-friendly challenge that demonstrates Stored Cross-Site Scripting (XSS).

## Scenario

Users can post comments on a website.

The application fails to sanitize user input before rendering it back to users.

Attackers can inject JavaScript payloads and access sensitive admin content.

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

- Stored XSS
- Input sanitization failures
- JavaScript payload execution
- Session hijacking concepts

---

## Warning

For educational purposes only.
