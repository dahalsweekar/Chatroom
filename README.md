# Introduction

This repository is an implementation of FastAPI, SQLALCHEMY, HTML/CSS Javascript, and WebSocket to create a Login system to authenticate a user into a chatroom. 

| Ramesh  | Sita |
| ------------- | ------------- |
| ![chat2](https://github.com/dahalsweekar/Chatroom/assets/99968233/b4473b1a-341e-432b-b977-dd2aceae2fca) | ![chat1](https://github.com/dahalsweekar/Chatroom/assets/99968233/1f14ead2-987d-4eea-8262-50b1807fc641) | 

# Features
## 1.	FastAPI:
FastAPI is a high-performance web framework for building Application Programming Interface (API) using python programming language. FastAPI basically sits between the front-end and the backend. It may act as a authenticator or a validator of data being passed between front-end and back-end. In this project, I have not implemented JWT Authentication, but I have used hash password generator to generate a unique and undecodable string and stored them in a database. The CRUD operation is performed on a seperate python file to ensure readability and organization of the code. The routes that are implemented in this project are as follows:

| Routes  | Method |
| ------------- | ------------- |
| ```register/``` | *GET* | 
| ```register/user```  | *POST*	|                                                                   
| ```login/```  | *GET* |
| ```login/user```  | *POST* |
| ```/chat```  | *GET* |

Types of HTTP methods:

1. GET: This method is used to retrieve data on a server. Clients can use this method to receive a data. In this project get method is used to receive a HTML Template
2. POST: This method is used to send data to the back-end, usually database to perform operations such as insertion. In this project post method is used to register a user into the database and to validate the registry of a user during login phase.
 
## 2. WebSocket:
WebSocket is a birdirectional, a full-duplex protocal that is used to perform real-time communication. Unlike HTTP, WebSocket starts with ws://. In this project websocket is used to perform chat between two or multiple parties on the same localhost. WebSocket has the ability to perform communication without the need for sending another request to server (meaning the server is kept alive for a entirity of a session until deliberately terminated).

## 3. 	SQLALCHEMY

SQLALCHEMY is a python SQL toolkit and Object Relational Mapper (ORM) that gives us, the developer, to utilize the power of databases using class and objects. In this project, I used SQLITE database to perform data storage. Other alternatives are PostgreSQL and MYSQL.
Features of SQLALCHEMY are:
1. Engines:
It allows us to bind the declared database, in this case SQLITE, to define the behaviour of the database and the object. For example, a database having a name as 'name' should be accurately mapped with object name 'name' to avoid errors.
2. SQL Statements: It allows us to perform SQL operations without the need for traditional SQL language (INSERT, DELETE and so on).
3. Pydantic Model: By using pydantic validation technique with SQLalchemy, we will be able to gain a fast, powerful and efficient 	control over our databases. Features of pydantic model includes data transfer in the form of NoSQL (JSON) file makes it easier to understand and relaiable to apply data validation.

## 4. HTML/CSS
It is a language for front-end development. I have used HTML to create layout such as Fields and Forms. I have used CSS to create styles.

## 4. JavaScript
In this project, I used JQuery and its library Ajax to transfer data between server and client. Ajax is a powerful and efficient method which allows us to establish and maintain a workflow without the need for page to reload. I have used Ajax to transfer the data such as 'Email' and 'Password' to the API in the back-end. I have also used Ajax for invoking bootstraps functions. Furthermore, Ajax sends the data in the form of JSON, which makes it easier to understand.

# Installation:
     1. git clone https://github.com/dahalsweekar/Chatroom.git
     2. pip install -r requirements.txt
     3. python sql_dir/init_db.py
     4. uvicorn main:app --reload

# Sample:
## Welcome
![welcome](https://github.com/dahalsweekar/Chatroom/assets/99968233/25b6c0d3-5d3d-4144-8644-026570492a17)

## Login page
![Login](https://github.com/dahalsweekar/Chatroom/assets/99968233/b5bcfb4d-81ba-4375-9f97-944dc7943eec)

## Registration page
![registration](https://github.com/dahalsweekar/Chatroom/assets/99968233/c340a5f4-60ce-4bb0-8254-201ca542c13f)

## Chatroom
![chatroom](https://github.com/dahalsweekar/Chatroom/assets/99968233/3aa639c6-517c-46aa-85c1-0b5ea3b4163d)

# References:
1. FastAPI: https://fastapi.tiangolo.com/
2. Websockets: https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API
            https://fastapi.tiangolo.com/advanced/websockets/
3. JQuery/Ajax: https://api.jquery.com/jQuery.ajax/
4. ChatGPT

 
