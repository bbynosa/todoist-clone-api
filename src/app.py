from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_cors import CORS
from flask_migrate import Migrate
from config import app, db
from models import Task
import uuid
from datetime import datetime


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

## TODO: Add try-catch blocks to return HTTP 500 for server-side errors
## TODO: Find a "cleaner" way to prefix the "/api" path on these routes
## TODO: Is there an async-await in Flask?

@app.get("/api/tasks")
def list():
    query_result = Task.query.all()
    tasks = [i.serialize for i in query_result]
    return tasks


@app.get("/api/tasks/<id>")
def get(id):
    task = Task.query.get(id)

    if task == None:
        return "", 404

    return task.serialize


@app.post("/api/tasks")
def add():
    req = request.get_json()
    new_task = Task(
        id = str(uuid.uuid4()),
        name = req["name"],
        description = req["description"],
        priority = req["priority"],
        author = req["author"],
        due_date = req["due_date"],
        created_at = datetime.now(), ## TODO: Maybe include timezone?
        updated_at = datetime.now(),
        is_complete = req["is_complete"]
    )

    db.session.add(new_task)
    db.session.commit()

    ##TODO: Following HTTP semantics, return a 'Location' header with URI of the new resource
    return new_task.serialize, 201


@app.put("/api/tasks/<id>")
def edit(id):
    req = request.get_json()
    task = Task.query.get(id)
    
    if task == None:
        return "", 404

    task.name = req['name']
    task.description = req['description']
    task.priority = req['priority']
    task.author = req['author']
    task.due_date = req['due_date']
    task.updated_at = datetime.now()
    task.is_complete = req['is_complete']

    db.session.add(task)
    db.session.commit()

    return "", 200


@app.delete("/api/tasks/<id>")
def delete(id):
    task = Task.query.get(id)
    
    if task == None:
        return "", 404

    db.session.delete(task)
    db.session.commit()

    return "", 204

