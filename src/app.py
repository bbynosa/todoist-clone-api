from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_cors import CORS
from flask_migrate import Migrate
from config import app, db
from models import Task


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

## TODO: Add try-catch blocks to return HTTP 500 for server-side errors
@app.get("/tasks")
def list():
    query_result = Task.query.all()
    tasks = [i.serialize for i in query_result]
    return tasks


@app.get("/tasks/<id>")
def get(id):
    task = Task.query.get(id)

    if task == None:
        return "", 404

    return task.serialize


@app.post("/tasks")
def add():
    req = request.get_json()
    new_task = Task(
        id=req["id"],
        name=req["name"],
        status=req["status"],
        priority=req["priority"],
        notes=req["notes"],
        created_by=req["created_by"],
        assigned_to=req["assigned_to"],
    )

    db.session.add(new_task)
    db.session.commit()

    ##TODO: Following HTTP semantics, return a 'Location' header with URI of the new resource
    return new_task.serialize, 201


@app.put("/tasks/<id>")
def edit(id):
    req = request.get_json()
    task = Task.query.get(id)
    
    if task == None:
        return "", 404

    task.name = req['name']
    task.status = req['status']
    task.priority = req['priority']
    task.notes = req['notes']
    task.created_by = req['created_by']
    task.assigned_to = req['assigned_to']

    db.session.add(task)
    db.session.commit()

    return "", 200


@app.delete("/tasks/<id>")
def delete(id):
    task = Task.query.get(id)
    
    if task == None:
        return "", 404

    db.session.delete(task)
    db.session.commit()

    return "", 204

