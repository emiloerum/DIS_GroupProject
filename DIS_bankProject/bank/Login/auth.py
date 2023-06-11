from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, request, flash
from bank.forms import CustomerLoginForm, TransferForm 
from bank import app, conn, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from bank.models import select_User, select_user_accounts, transfer_account


# and bcrypt.check_password_hash(user[1], form.password.data)
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('views.home'))
    form = CustomerLoginForm()
    if form.validate_on_submit():
        user = select_User(form.id.data)
        if user != None:
            login_user(user)
            flash('Login successful.','success')
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
    if not current_user.is_authenticated:
        flash('Please Login.','warning')
        return redirect(url_for('Login.login'))
    

    Username = current_user.get_id()
    print(Username)

    dropdown_accounts = select_user_accounts(current_user.get_id())
    drp_accounts = []
    for drp in dropdown_accounts:
        drp_accounts.append((drp[0], drp[1]))
    print(drp_accounts)
    form = TransferForm()
    form.sourceAccount.choices = drp_accounts
    form.targetAccount.choices = drp_accounts
    if form.validate_on_submit():
        date = datetime.date.today()
        amount = form.amount.data
        from_account = form.sourceAccount.data
        to_account = form.targetAccount.data
        transfer_account(date, amount, from_account, to_account)
        flash('Transfer succeed!', 'success')
        return redirect(url_for('Login.home'))
    return render_template('transfer.html', title='Transfer', drop_cus_acc=dropdown_accounts, form=form)
