from flask import Blueprint, render_template, request, flash, redirect, url_for


auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return render_template("ov.html")

@auth.route('/inventory')
def inventory():
    return render_template("home.html")

@auth.route('/insert')
def insert():
    return render_template("insert.html")