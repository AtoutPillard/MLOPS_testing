# MLOPS-PROJECT

## 1- Prerequisite

- Docker : 20.10.22, build 3a2c30b
- Docker Compose : v2.15.1
- Python : 3.9.6

## 2- Run

### 2.1 - the project

In root folder

```cmd
docker-compose up
```

### 2.2- Run separatly each component

#### 2.2.1 - Prediction API

In backend_rating folder

```cmd
docker build -t prediction_api .
docker run -p 5000:5000 prediction_api
```

It should be accessible at <http://localhost/5000>

## 3- Information

### 3.1 - Use the anime prediction API

To use the api, after launching the project/api you must **use a post method** on <http://localhost:5000> having as body one of these fields :

- string :
  - title
  - synopsis
  - type

- list of string :
  - producers
  - studio
  - genders

Note :
    - These details can be seen directly on browser at <http://localhost:5000>
    - An example of possible values is available in ./backend_rating/model.py with the test_predict variable
    - If you want to test the predict endpoint, you can use the Postman tool. To make it easier, you can import the Postman collection file located in ./backend_rating/postman. It's a ready to go test who work with the API
