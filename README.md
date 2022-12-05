# FastAPI-Postgres-Starter-Template
This Github template provides a quick and easy way to get started with a FastAPI and Postgres database project. It provides the necessary setup to connect to a Postgres database and build API endpoints with FastAPI. The template also includes a basic database model and example API endpoints. This is a great starting point for any developer looking to build a fast and reliable API with Postgres.

## Acknowledgements

 - [FastAPI official website](https://fastapi.tiangolo.com/)
 - [My learning FastAPI repo](https://github.com/reubendeekay/learning-fastapi)



## API Reference

#### Get all users

```http
  GET /users/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get a user

```http
  GET /users/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of user to fetch details|



## Project Structure
This template uses the MVC pattern of development to offer a consistent stucture for easy of development
### app.py
This is the entry point to the app.
### models.py 
Contains all the database tables that are to be defined
### schemas.py
Contains the data models, how data will be structured and received. It uses the pydantic package
### oauth2.py
Contains all the authentication helpers to create access tokens,decode and verify them
### utils.py
Contains helper functions such as hashing and verification of hashed passwords
### database.py
Contains the database setup with Postgress
### config.py
Contains the base settings file that imports the .env file to be used in the app

### Environment Variables
To use this template, create a .env file in the route of the project with the following file structure:
```python
ALGORITHM=HS256

SECRET_KEY=secret
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_NAME=example-database
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=password
DATABASE_URI=postgresql://postgres:password@localhost:5432/example-database
```
* Note the above .env file is a dummy file. Replace it with your real credentials

## How to use
* Create a virtual environment and ensure you are running on a virtual environment.
```bash
run python3 -m venv venv
```
* Run  
```bash
pip install -r requirements.txt
```
To install all necessary packages
* Run 
```bash
uvicorn app.main:app --reload 
```
To run the API on localhost
* Access the API on the browser by typing localhost:8000
* View the documentation of the API from http://localhost:8000/docs or http://localhost:8000/redocs
