from flask import Blueprint, request
from src.app import Post, db
from http import HTTPStatus
from sqlalchemy import inspect

app_post = Blueprint("post", __name__, url_prefix="/post")


@app_post.route("/", methods=["POST", "GET"])
def handle_post():
    print(request.method)
    if request.method == "POST":
        _create_post()
        return {"message": "User created!"}, HTTPStatus.CREATED
    else:
        return {'post': _list_posts()}


def _create_post():
    data = request.json
    post = Post(title=data['title'], body=data['body'],
                author_id=data['author_id'])
    db.session.add(post)
    db.session.commit()


def _list_posts():
    query = db.select(Post)
    posts = db.session.execute(query).scalars()
    return [
        {
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'created': post.created,
            'author_id': post.author_id
        } for post in posts
    ]


@app_post.route("/<int:post_id>")
def get_user(post_id):
    post = db.get_or_404(Post, post_id)
    return {
        "id": post.id,
        'title': post.title,
        'body': post.body,
        'created': post.created,
        'author_id': post.author_id
    }


@app_post.route("/<int:post_id>", methods=["PATCH"])
def update_user(post_id):
    post = db.get_or_404(Post, post_id)
    data = request.json

    mapper = inspect(Post)
    for column in mapper.attrs:
        if column.key in data:
            setattr(post, column.key, data[column.key])
    db.session.commit()

    return {
        "id": post.id,
        "title": post.title,
        "body": post.body,
        "created": post.created,
        "author_id": post.author_id
    }


@app_post.route("/<int:post_id>", methods=["DELETE"])
def remove_user(post_id):
    post = db.get_or_404(Post, post_id)
    db.session.delete(post)
    db.session.commit()

    return "", HTTPStatus.NO_CONTENT
