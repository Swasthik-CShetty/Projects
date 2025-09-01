# Project 2: Secure Login System using Python , Flask and Bycrypt

## Objective
Build a simple and secure login system using **Flask**, with **hashed passwords** and **input validation**, to demonstrate secure authentication practices.

---

## Tools & Technologies
- **Python**
- **Flask** (web framework)
- **Flask-Bcrypt** (for password hashing)
- **SQLite** (database)

---

## Security Features

**Password Hashing**
All passwords are stored securely using bcrypt (no plain text storage).

**Input Validation**

Usernames restricted to letters, numbers, underscores (3–20 chars).

Password must be at least 4 characters.

Prevents SQL injection using parameterized queries.

**Session Management**
User sessions are tracked securely with Flask sessions.

## How it Works
**Signup**

User enters a new username & password.

Password is hashed and stored in the database.

**Login**

User enters credentials.

Password entered is hashed and compared with the stored hash.

If valid → user logged in, else → error message.

**Logout**

Session is cleared, user is logged out securely.
