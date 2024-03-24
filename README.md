# FastAPI NatureDots

FastAPI NatureDots is a RESTful API project built using FastAPI, SQLAlchemy, and PostgreSQL for managing water quality observations.

## Features

- CRUD operations for water quality observations
- Filtering observations by date range, location, and quality parameters
- Error handling for invalid requests
- PostgreSQL database integration with SQLAlchemy ORM
- API documentation using Swagger UI (FastAPI's built-in documentation)

## Technologies Used

- FastAPI: FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- SQLAlchemy: SQLAlchemy is an SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- PostgreSQL: PostgreSQL is a powerful, open-source relational database management system. We have used cloud PostGres database NeonDB: https://neon.tech/

## Setup

1. Clone the repository:
git clone https://github.com/your-username/fastapi-naturedots.git
2. Change directory into it -
cd fastapi-naturedots
3. Install the dependencies -
pip install -r requirements.txt
4. Run the server-
uvicorn main:app --reload
5. http://127.0.0.1:8000/docs

