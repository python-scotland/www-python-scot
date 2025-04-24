from flask import Flask, g, render_template, url_for
from markupsafe import Markup
from pyhead import Head

from app.config import Config, DebugConfig


def create_app():
    app = Flask(__name__, static_url_path="/")
    app.config.from_object(DebugConfig)

    @app.route("/")
    def home():
        return render_template("pages/home/0_index.html")

    @app.before_request
    def before_request():
        g.head = Head(
            title="Python Scotland"
        )
        g.head.set_stylesheet(
            href=url_for("static", filename="main.css")
        )

    @app.context_processor
    def pinned_article_wrapper():
        def pinned_article(template):
            emoji = render_template('includes/pinned_emoji.html')

            return Markup(
                '<article class="pinned-article">'
                f'{emoji}'
                '<div class="article-content">'
                f'{render_template(template)}'
                '</div>'
                '</article>'
            )

        return dict(pinned_article=pinned_article)

    return app
