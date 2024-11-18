from flask_jwt_extended import create_access_token
from flask import Blueprint, request
from http import HTTPStatus
from src.app import User, db
# from sqlalchemy import inspect


app = Blueprint("auth", __name__, url_prefix="/auth")


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    print(username, password)
    user = db.session.execute(db.select(User.id)
                              .where(User.username == username)).scatar()
    print(user)
    if not user or user.password != password:
        return {"msg": "Bad username or password"}, HTTPStatus.UNAUTHORIZED

    access_token = create_access_token(identity=user.id)
    return {"access_token": access_token}, HTTPStatus.CREATED
