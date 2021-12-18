from flask import Flask, render_template, url_for
from my_flask_app import app
from my_flask_app.models import User, Post


@app.route("/")
def home_function():
    posts = Post.query.all()
    return render_template("home_template.html", posts=posts)


@app.route("/post/<int:post_id>")
def detail_function(post_id):
    post_individual = Post.query.get_or_404(post_id)
    return render_template("detail_view.html", post_individual=post_individual)
