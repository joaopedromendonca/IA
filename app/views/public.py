from flask import render_template
from flask.blueprints import Blueprint

public_bp = Blueprint("public", __name__)

@public_bp.route("/", methods=["GET","POST"])
def home():
    
    return render_template("home.html")