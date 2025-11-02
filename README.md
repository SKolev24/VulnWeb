# Vulnerable Web App 

**Overview**

This project is a deliberately vulnerable web application built with Django. It serves as a learning environment for studying and demonstrating common web security flaws. The goal is to understand how these vulnerabilities work, how attackers exploit them, and how to secure applications against them.

**Purpose**

Created as part of a personal learning process. The focus is on hands-on exploration of web security principles through practical implementation.

**Technologies**

- Django (Python)  
- SQLite (default for simplicity)  
- HTML, CSS, JavaScript  

**Vulnerabilities Planned**  
The project aims to demonstrate examples of:  
- Injection (SQL injection implemented)
- Broken Authentication
- Sensitive Data Exposure
- XML External Entities (XXE)
- Broken Access Control
- Security Misconfiguration
- Cross-Site Scripting (XSS)
- Insecure Deserialization

**Current Status**
- SQL Injection: Implemented
- Remaining vulnerabilities: Work in progress

**Learning Goals**
- Build and configure a Django application from scratch
- Understand common security flaws in web applications
- Learn how to patch and secure these vulnerabilities

**Setup**  

1. Clone the Repository   

2. Install Dependancies  
```bash
pip install -r requirements.txt
```

3. Run the server  
```bash
python manage.py runserver
```

4.Access the app at http://127.0.0.1:8000/
