# SSRF Metadata Challenge

A beginner-friendly challenge demonstrating Server-Side Request Forgery (SSRF).

## Scenario

A website allows users to fetch content from external URLs.

Improper validation allows attackers to force the server to make requests to internal services.

Your objective is to access internal metadata and retrieve the hidden flag.

---

## Requirements

```bash
pip install flask requests
```

---

## Setup

```bash
python app.py
```

---

## Access Challenge

```bash
http://127.0.0.1:5000
```

---

## Learning Objectives

- SSRF fundamentals
- Internal network access
- Cloud metadata abuse
- URL validation issues

---

## Warning

For educational purposes only.
