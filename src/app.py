import json
import boto3
import os

from flask import Flask
from flask import request
from boto3.dynamodb.conditions import Key
from flask_cors import CORS

table_name = os.environ["DYNAMODB_TABLE_NAME"]
dynamodb_endpoint = os.environ["DYNAMODB_SERVICE_ENDPOINT"]
dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_endpoint)
table = dynamodb.Table(table_name)

app = Flask(__name__)

CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.get("/todos")
def list():
    res = table.scan()

    return res["Items"]


@app.get("/todos/<id>")
def get(id):
    res = table.query(
        KeyConditionExpression=Key('id').eq(id)
    )

    return res["Items"][0]


@app.post("/todos")
def create():
    req = request.get_json()

    table.put_item(
        Item={
            'id': req['id'],
            'name': req['name'],
            'status': req['status'],
            'priority': req['priority'],
            'notes': req['notes'],
            'created_by': req['created_by'],
            'assigned_to': req['assigned_to']
        }
    )

    return "", 201


@app.put("/todos/<id>")
def edit(id):
    req = request.get_json()

    table.put_item(
        Item={
            'id': id,
            'name': req['name'],
            'status': req['status'],
            'priority': req['priority'],
            'notes': req['notes'],
            'created_by': req['created_by'],
            'assigned_to': req['assigned_to']
        }
    )
    return "", 200


@app.delete("/todos/<id>")
def delete(id):
    table.delete_item(
        Key={
            'id': id
        }
    )

    return "", 204
