from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("blog", __name__)

# show all of the posts, most recent first
@bp.route("/")
def index():
    db = get_db()
    posts = db.execute(
        "SELECT p.id, title, body, created, author_id, username"
        " FROM post p JOIN user u ON p.author_id = u.id"
        " ORDER BY created DESC"
    ).fetchall()
    return render_template("blog/index.html", posts=posts)


# can be used to get a post without checking the author
def get_post(id, check_author=True):
    post = (
        get_db()
        .execute(
            "SELECT p.id, title, body, created, author_id, username"
            " FROM post p JOIN user u ON p.author_id = u.id"
            " WHERE p.id = ?",
            (id,),
        )
        .fetchone()
    )

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post["author_id"] != g.user["id"]:
        abort(403)

    return post


# create a new post for the current user
# or update a post if the current user is the author
@bp.route("/<int:id>/post", methods=("GET", "POST"))
@login_required
def post(id):
    def create():
        db = get_db()
        db.execute(
            "INSERT INTO post (title, body, author_id)" " VALUES (?, ?, ?)",
            (title, body, g.user["id"]),
        )
        db.commit()

    def update():
        db = get_db()
        db.execute(
            "UPDATE post SET title = ?, body = ?" " WHERE id = ?",
            (title, body, id),
        )
        db.commit()

    # since AUTOINCREMENT is used for post id,
    # setting id to 0 will allow one view and template
    # to be used for creating and updating posts
    if id == 0:
        post = None

    else:
        post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)

        if id == 0:
            create()

        else:
            update()

        return redirect(url_for("blog.index"))

    return render_template("blog/post.html", post=post)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute("DELETE FROM post WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("blog.index"))