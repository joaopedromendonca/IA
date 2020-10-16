from flask import Flask

tic = Flask(__name__)


@tic.route("/")
def index():
    return "Hello world!"

@tic.route("/about")
def about():
    return "<h1 style='color: red'>About</h1>"


if __name__ == "__main__":
    tic.run()