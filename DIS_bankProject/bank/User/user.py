from flask import render_template, url_for, flash, redirect, request, Blueprint
from bank import app, conn, bcrypt
from bank.forms import TransferForm
from flask_login import current_user
from bank.models import select_user_accounts,  transfer_account



User = Blueprint('User', __name__)

@User.route("/transfer", methods=['GET', 'POST'])
def transfer():
    if not current_user.is_authenticated:
        flash('Please Login.','warning')
        return redirect(url_for('Login.login'))
    

    Username = current_user.get_id()
    print(Username)

    # dropdown_accounts = select_cus_accounts(current_user.get_id())
    # drp_accounts = []
    # for drp in dropdown_accounts:
    #     drp_accounts.append((drp[3], drp[1]+' '+str(drp[3])))
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
