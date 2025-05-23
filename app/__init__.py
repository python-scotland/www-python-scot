from flask import Flask, g, render_template, url_for
from markupsafe import Markup
from pyhead import Head

from app.config import Config, DebugConfig


def create_app():
    app = Flask(__name__, static_url_path="/")
    app.config.from_object(DebugConfig)

    @app.route("/")
    def home():
        return render_template("pages/home.html")

    @app.route("/support-us")
    def support_us():
        return render_template("pages/support-us.html")

    @app.route("/our-mission")
    def our_mission():
        return render_template("pages/our-mission.html")

    @app.route("/get-involved")
    def get_involved():
        return render_template("pages/get-involved.html")

    @app.route("/code-of-conduct")
    def code_of_conduct():
        return render_template("pages/code-of-conduct.html")

    @app.before_request
    def before_request():
        g.head = Head(
            title="Python Scotland"
        )
        g.head.set_favicon(
            ico_icon_href="/favicons/favicon.ico",
            png_icon_16_href="/favicons/favicon-16x16.png",
            png_icon_32_href="/favicons/favicon-32x32.png",
            png_icon_64_href="/favicons/favicon-64x64.png",
            png_icon_96_href="/favicons/favicon-96x96.png",
            png_icon_180_href="/favicons/favicon-180x180.png",
            png_icon_196_href="/favicons/favicon-196x196.png",
            png_apple_touch_icon_57_href="/favicons/apple-touch-icon-57x57.png",
            png_apple_touch_icon_60_href="/favicons/apple-touch-icon-60x60.png",
            png_apple_touch_icon_72_href="/favicons/apple-touch-icon-72x72.png",
            png_apple_touch_icon_76_href="/favicons/apple-touch-icon-76x76.png",
            png_apple_touch_icon_114_href="/favicons/apple-touch-icon-114x114.png",
            png_apple_touch_icon_120_href="/favicons/apple-touch-icon-120x120.png",
            png_apple_touch_icon_144_href="/favicons/apple-touch-icon-144x144.png",
            png_apple_touch_icon_152_href="/favicons/apple-touch-icon-152x152.png",
            png_apple_touch_icon_167_href="/favicons/apple-touch-icon-167x167.png",
            png_apple_touch_icon_180_href="/favicons/apple-touch-icon-180x180.png",
            png_mstile_70_href="/favicons/mstile-70x70.png",
            png_mstile_270_href="/favicons/mstile-270x270.png",
            png_mstile_310x150_href="/favicons/mstile-310x150.png",
            png_mstile_310_href="/favicons/mstile-310x150.png",
        )
        g.head.set_stylesheet(
            href=url_for("static", filename="css/main.css")
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
