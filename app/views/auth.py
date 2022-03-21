from flask.blueprints import Blueprint
from flask import request, redirect, url_for, render_template, flash, current_app
from flask_login import login_required, current_user, logout_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("public.home"))