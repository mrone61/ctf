# Command Injection Challenge

A beginner-friendly challenge demonstrating OS Command Injection vulnerabilities.

## Scenario

A web application provides a network diagnostic tool that allows users to ping a target host.

User input is directly passed into a system command without sanitization.

Attackers can inject arbitrary system commands to access sensitive information.

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

## Example Payload

```bash
127.0.0.1; whoami
```

---

## Learning Objectives

- Command Injection
- Shell command abuse
- Input validation failures
- Web exploitation fundamentals

---

## Warning

For educational purposes only.
