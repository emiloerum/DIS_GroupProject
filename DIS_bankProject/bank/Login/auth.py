from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, request, flash
from bank.forms import CustomerLoginForm, TransferForm 
from bank import app, conn, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from bank.models import select_User

# and bcrypt.check_password_hash(user[1], form.password.data)
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    form = CustomerLoginForm()
    if form.validate_on_submit():
        user = select_User(form.id.data)
        if user != None:
            login_user(user)
            flash('Login successful.','danger')
            return redirect(url_for('auth.transfer'))  
    else:
        flash('Login Unsuccessful. Please check identifier and password', 'danger')

    return render_template("login.html", form=form)

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up')
def sign_up():
    return render_template("sign-up.html")

@auth.route('/transfer')
def transfer():
    form = TransferForm
    return render_template("transfer.html", form=form)

