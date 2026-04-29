# SSTI Template Challenge

A beginner-friendly challenge demonstrating Server-Side Template Injection (SSTI) in Flask/Jinja2.

## Scenario

A website allows users to generate personalized greetings.

User input is directly embedded into templates without sanitization.

Attackers can inject template expressions and access sensitive server-side data.

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

```python
{{7*7}}
```

---

## Learning Objectives

- SSTI basics
- Template injection
- Jinja2 exploitation
- Server-side input handling flaws

---

## Warning

For educational purposes only.
