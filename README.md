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

## API Endpoints (Postman collection is added in the project)

- GET /observations: Get all observations
- POST /observations: Create a new observation
- GET /observations/{observation_id}: Get a specific observation by ID
- PUT /observations/{observation_id}: Update a specific observation by ID
- DELETE /observations/{observation_id}: Delete a specific observation by ID
- GET /observations/closest_location: Get observations closest to a given location
- GET /observations/date_range: Get observations within a specified date range
- GET /observations/quality_parameters: Filter observations by quality parameters

## Note - 
- I have created the APIs using FastAPI with a PostGres database. The documentation for the API can be found in the POSTMAN collections. At this point the requirement 1,2 is completed.
  ![Screenshot (22)](https://github.com/madhurjyasarma/FastAPI-PostGres/assets/77984764/0a8eec12-e0b7-415e-a594-a5efac42d484)
  Example of one API with POSTMAN
  ![Screenshot (7)](https://github.com/madhurjyasarma/FastAPI-PostGres/assets/77984764/5becd497-7d55-4b48-9951-c8b8b47bbe8e)

- But while creating the docker container I was facing error some problem with Docker daemon. Since I could't able to create a docker container.
  Since I couldn't able to create the image, I also didn't tried Localstack since it requires that docker image.
  ![Screenshot (15)](https://github.com/madhurjyasarma/FastAPI-PostGres/assets/77984764/0afceb67-c822-4698-82ad-51adfe1ec7cb)

- So, I have decided to deploy the application directly to a AWS EC2 instance, Using a CURL command I am able to add a record in the database.
![Screenshot (20)](https://github.com/madhurjyasarma/FastAPI-PostGres/assets/77984764/bb4c8ce0-08e8-46f1-8fef-bbb7a16bd762)

- Here is a screenshot of the inserted records in the PostGres database. Here (Index 7) "New Observation has been inserted" from the EC2 machine to database.
![Screenshot (21)](https://github.com/madhurjyasarma/FastAPI-PostGres/assets/77984764/0ffbc6ec-229c-4cf6-aaae-e2c671ffc4cd)

## Thanks
- To conclude
- I will also add Authentication using JWT in this project in future.
- I will also add testing for the API endpoints to ensure reliability and
facilitate continuous integration and deployment processes.


