# Lottery Management System — AISSCE 2027

A Python and MySQL-based Lottery Management System developed as a **CBSE AISSCE 2027 Computer Science project**.

## Problem Statement

Manual lottery management can lead to errors in ticket registration, duplicate entries, winner selection, and result recordkeeping. A computerized system is needed to manage user records, register lottery tickets, maintain ticket purchase history, randomly select winners using Python, and store and retrieve lottery records efficiently through a database.

## Objectives

- Automate lottery ticket registration and recordkeeping.
- Maintain user information and ticket purchase history.
- Manage lottery sessions using start and end times.
- Implement random lottery-number generation using Python.
- Store and retrieve records using MySQL.
- Provide separate interfaces for public users and administrators.

## Features

### Public User
- Register a new account.
- Log in using a user ID and password.
- Join an active lottery session.
- Generate lottery ticket numbers.
- View previously recorded lottery tickets.
- Log out of the application.

### Administrator
- Initialize the database tables.
- View registered users.
- View lottery logs.
- Create lottery sessions.
- Generate lottery numbers.
- End lottery sessions.
- Optionally clear lottery logs.

> **Note:** Winner selection currently generates a random number without verifying that it belongs to an eligible purchased ticket. This must be corrected before the system can be considered a reliable lottery implementation.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and random-number generation |
| MySQL | Persistent storage of user, session, and ticket records |
| MySQL Connector/Python | Communication between Python and MySQL |
| Git and GitHub | Source-code version control and project hosting |

## Project Structure

```text
Lottery-System-AISSCE-2027/
├── MODULES/
│   ├── admin.py
│   └── public.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Database Design

The application uses a MySQL database named `LOTTERY`.

### 1. USERS

Stores registered user information.

| Column | Purpose |
|---|---|
| `user_id` | Unique user identifier and primary key |
| `name` | User's name |
| `password` | User authentication data |
| `address` | User's address |
| `phone_number` | Contact number |
| `email` | Email address |
| `registration_date` | Account registration timestamp |

**Security requirement:** Passwords must be stored as secure password hashes, not as plaintext.

### 2. LOTTERY_LOGS

Stores ticket purchase records.

| Column | Purpose |
|---|---|
| `log_id` | Auto-incremented primary key |
| `user_id` | References the registered user |
| `lottery_number` | Generated lottery ticket number |
| `date` | Record creation timestamp |

The `user_id` column references `USERS(user_id)` through a foreign-key relationship.

### 3. SESSIONS

Stores lottery session schedules.

| Column | Purpose |
|---|---|
| `session_id` | Auto-incremented primary key |
| `start_time` | Scheduled start time |
| `end_time` | Scheduled end time |

**Design limitation:** The current schema does not contain a dedicated table for finalized winners and lottery results. Adding one would improve traceability and recordkeeping.

## Installation and Setup

### Prerequisites

- Python 3.10 or a compatible newer version
- MySQL Server
- Git

### Step 1: Clone the repository

git clone https://github.com/AltF4Soul-JaY/Lottery-System-AISSCE-2027.git
cd Lottery-System-AISSCE-2027

### Step 2: Create a virtual environment

python -m venv .venv

Activate it in Windows PowerShell:

.venv\Scripts\Activate.ps1

Or in Git Bash:

source .venv/Scripts/activate

### Step 3: Install dependencies

pip install -r requirements.txt

### Step 4: Configure MySQL

Ensure that MySQL Server is running.

The current implementation contains hardcoded database connection settings. Configure these locally to match your MySQL installation before running the program.

**Never commit real database passwords, API keys, or other credentials to GitHub.** Environment variables or an ignored `.env` file are preferable for local configuration.

### Step 5: Run the application

python main.py

Follow the terminal menu to access the public-user or administrator interface.

## Security Considerations

This project is an educational prototype. The following issues must be addressed before it handles real users or sensitive data.

| Issue | Recommended improvement |
|---|---|
| Hardcoded database credentials | Load credentials from environment variables |
| Hardcoded administrator credentials | Implement secure, configurable administrator authentication |
| SQL queries built using string interpolation | Use parameterized SQL queries |
| Plaintext user passwords | Hash passwords using Argon2 or bcrypt |
| Authentication checks that can be bypassed | Validate credentials before granting access |
| Lottery numbers not consistently tied to eligible tickets | Select winners exclusively from valid entries |
| Possible duplicate ticket registrations | Enforce appropriate database constraints |
| Incomplete session and result management | Validate session states and persist finalized results |

### Security Disclaimer

This application is intended for educational use and demonstration purposes. It has known security and correctness limitations and has not undergone a comprehensive independent security assessment.

Do not use it for real-money lotteries, production authentication, or the storage of sensitive personal information until the identified issues have been resolved and tested.

## Future Improvements

- Secure user and administrator authentication.
- Centralized database configuration through environment variables.
- Parameterized SQL queries throughout the application.
- Duplicate-entry prevention and stronger database constraints.
- Winner selection based on eligible purchased tickets.
- Persistent winner history and finalized session records.
- Input validation and improved exception handling.
- Automated tests for authentication, ticket registration, and session management.

## License

This project is distributed under the MIT License. See the `LICENSE` file for the applicable terms.

## Project Information

**Project:** Lottery Management System  
**Academic session:** AISSCE 2027  
**Subject:** Computer Science  
**Programming Language:** Python  
**Database:** MySQL