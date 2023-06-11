from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, request, flash
from bank.forms import CustomerLoginForm 
from bank import app, conn, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from bank.models import select_User


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Login.home'))
    form = CustomerLoginForm()
    if form.validate_on_submit():
        user = select_User(form.id.data)
        if user != None and bcrypt.check_password_hash(user[1], form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Login successful.','success')
            return redirect(url_for('Login.home'))  
    else:
        flash('Login Unsuccessful. Please check identifier and password', 'danger')

    return render_template("login.html", form=form)

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up')
def sign_up():
    return render_template("sign-up.html")

