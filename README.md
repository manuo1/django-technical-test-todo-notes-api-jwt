# Django Todo & Notes API (Technical Test)

This project is a small Django REST API built for a technical test.
It exposes two independent apps : **Todos** and **Notes**, with a simple link between them.

The goal is to demonstrate clean structuring, app isolation, REST patterns, and optional JWT authentication.

## Documentation of Required Technical Test Explanations



For a deeper understanding of the design choices and project context, and to see the explanations requested in the technical test, you can consult the following documents ( *documents in French* ):

- [Project Context](docs/CONTEXT.md)
- [App Architecture](docs/ARCHITECTURE.md)
- [Technical Decisions](docs/DECISIONS.md)



## Requirements

- Python **3.12** (compatible 3.9+)
- Virtualenv recommended
- Dependencies in `requirements.txt`

---

## Installation

```bash
# Clone repository
git clone https://github.com/manuo1/django-technical-test-todo-notes-api-jwt.git
cd django-technical-test-todo-notes-api-jwt

# Create virtual environment
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser
```
## Run App
```bash
python manage.py runserver
```

## Authentication (JWT)
```bash
# Obtain token
curl -X POST http://localhost:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin"}'

# Example response:
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.refresh_token_example",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.access_token_example"
}

# Using the access token
curl -X GET http://localhost:8000/api/todos/ \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.access_token_example"
```
For more details on how JWT works and how tokens should be used, refer to the official SimpleJWT documentation:
https://django-rest-framework-simplejwt.readthedocs.io/

## Endpoints Summary
```bash
    GET    /api/notes/
    POST   /api/notes/
    GET    /api/notes/{id}/
    PUT    /api/notes/{id}/
    PATCH  /api/notes/{id}/
    DELETE /api/notes/{id}/

    GET    /api/todos/
    POST   /api/todos/
    GET    /api/todos/{id}/
    PUT    /api/todos/{id}/
    PATCH  /api/todos/{id}/
    DELETE /api/todos/{id}/
```
## Running Tests

This project uses `pytest` and `pytest-django` for testing.

  *(Make sure your virtual environment is activated and dependencies are installed)*

  ```bash
  # Run the tests:
  pytest
  ```

All tests cover the API endpoints for `Todos` and `Notes`, including CRUD operations and JWT authentication.


## Important note
This implementation only follows the technical test requirements.
For production-ready usage, more business context and constraints would be necessary.
