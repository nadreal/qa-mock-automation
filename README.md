# QA Automation Platform - Demo
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/nadreal/qa-automation-platform/ci-cd-pipeline.yml?branch=main&style=flat-square) &nbsp;&nbsp;
![Pytest](https://img.shields.io/badge/Pytest-tested-success?style=flat-square) &nbsp;&nbsp;
![Python Version](https://img.shields.io/badge/Python-3.11-blue?style=flat-square) &nbsp;&nbsp;
![Playwright](https://img.shields.io/badge/Playwright-automation-blueviolet?style=flat-square) &nbsp;&nbsp;
[![Allure Test Report](https://img.shields.io/badge/%20Report-Allure-purple)](https://nadreal.github.io/qa-automation-platform/)
## Project Overview
   - Demonstrate a mock **FastAPI backend** using REST API, that simulates user management and health check endpoints with in-memory mock storage   

   - Clean test architecture

   - API client abstraction pattern

   - Pydantic Schema-based validation

   - Positive and negative test coverage

   - Test data isolation

   - CI integration

## Project Structure 
```
├── workflows/
│   └── ci-cd-pipeline.yml   # CI/CD workflow

backend/
│
├── app/
│   ├── main.py
│   ├── models.py
├── ├── routes/
│   │   ├── admin.py
│   │   └── users.py
│   ├── services/
│   │   ├── user_service.py
│   │   └── user_service_memory.py

tests/
│
├── api/
│   └── test_users.py
│   └── test_admin.py
│
├── clients/
│   └── users_client.py
│   └── admin_client.py
│
├── schemas/
│   └── user_schema.py
│
└── conftest.py
```
## Architecture Overview

- The backend follows a simple service abstraction pattern
- Business logic is isolated behind a `UserService` interface
- Currently, an in-memory implementation (`UserServiceMemory`) is used for both API execution and automated tests

This allows:
- deterministic and fast tests
- no external dependencies
- easy replacement with a database-backed service in the future

## CI-CD Integration Overview
 - A GitHub Actions workflow is included to automatically run tests on each commit
 - Workflow file: .github/workflows/ci-cd-pipeline.yml
 - Triggered on: push and pull_request events

## API endpoints

- **GET `/health`** – API health check. Returns: {"status": "ok"}

- **POST `/users/`** – Create a new user. Send JSON: 

- **GET `/users/{id}`** – Get a user by ID. Returns user JSON.

- **DELETE `/users/{id}`** - Delete a user by ID.

## Test Reporting

- Open Allure [Test Report ](https://nadreal.github.io/qa-automation-platform/index.html) 

## Author

👨‍🚀 Stevan Grubac [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourusername) <br>
💻 Software Engineer | QA Automation | DevOps


