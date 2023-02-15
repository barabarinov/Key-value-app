import json
import os

from flask import Flask
from flask import request
from flask_api import status
from redis import Redis

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))

app = Flask(__name__)
redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT)


@app.route("/key/", methods=["POST"])
def create():
    data = request.get_json()
    if not isinstance(data, dict):
        return "Bad request!", status.HTTP_400_BAD_REQUEST
    if "key" not in data or "value" not in data:
        return "Bad request!", status.HTTP_400_BAD_REQUEST
    key = data["key"]
    value = data["value"]
    redis_client.set(name=key, value=value)
    return {"key": key, "value": value}, status.HTTP_201_CREATED


@app.route("/key/<string:key>/", methods=["GET"])
def get(key: str):
    if not redis_client.exists(key):
        return "Not Found!", status.HTTP_404_NOT_FOUND
    value = redis_client.get(name=key)
    return value, status.HTTP_200_OK


@app.route("/key/<string:key>/", methods=["PUT"])
def update(key: str):
    if not redis_client.exists(key):
        return "Not Found!", status.HTTP_404_NOT_FOUND
    data = request.get_json()
    if "value" not in data:
        return "Bad request!", status.HTTP_400_BAD_REQUEST
    new_value = data["value"]
    redis_client.set(name=key, value=new_value)
    return {"key": key, "value": new_value}, status.HTTP_200_OK


@app.route("/key/<string:key>/", methods=["DELETE"])
def delete(key: str):
    if not redis_client.exists(key):
        return "Bad request!", status.HTTP_400_BAD_REQUEST
    redis_client.delete(key)
    return f"The Key '{key}' was Successfully Deleted!", status.HTTP_200_OK


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
