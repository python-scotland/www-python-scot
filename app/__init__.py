from flask import Flask, g, render_template, url_for
from pyhead import Head

from app.config import Config, DebugConfig


def create_app():
    app = Flask(__name__, static_url_path="/")
    app.config.from_object(DebugConfig)

    @app.before_request
    def before_request():
        g.head = Head(
            title="Python Scotland"
        )
        g.head.set_stylesheet(
            href=url_for("static", filename="main.css")
        )

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
