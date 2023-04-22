
from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Habit Tracking System with Python Flask and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "flask", "web"],
        "slug": "habit-tracking",
        "prod": "https://habit-tracker-using-flask.onrender.com",
    },
    {
        "name": "Micro blog application Python Flask and MongoDB",
        "thumb": "img/micro-blog.png",
        "hero": "img/microblog.png",
        "categories": ["python", "flask", "web"],
        "slug": "micro-blog",
        "prod": "https://python-web-microblog-d5g5.onrender.com",
    },

]

slug_to_project = {project['slug']: project for project in projects}


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404