from bank import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql


class User(tuple, UserMixin):
    def __init__(self, user_data):
        self.username = user_data[0]
        self.password = user_data[1]
    
    def get_id(self):
       return (self.username)

def select_User(username):
# Change name of database at some point
    cur = conn.cursor()
    sql = """
    SELECT * FROM Users
    WHERE username = %s
    """
    cur.execute(sql, (username,))
    user = User(cur.fetchone()) if cur.rowcount > 0 else None
    cur.close()
    return user
 

@login_manager.user_loader
def load_user(username):
    user = select_User(username)
    return user

def select_user_accounts(username):
    cur = conn.cursor()
    sql = """
    SELECT
      a.account_name Accounts
    , a.account_balance Accounts
    FROM Owns o
      INNER JOIN Accounts a ON o.account_number = a.account_number 
	WHERE o.username = %s
    ;
    """
    cur.execute(sql, (username,))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset

def transfer_account(date, amount, from_account, to_account):
    cur = conn.cursor()
    sql = """
    INSERT INTO Transfers(transfer_date, amount, from_account, to_account)
    VALUES (%s, %s, %s, %s)
    """
    cur.execute(sql, (date, amount, from_account, to_account))
    conn.commit()
    cur.close()

def update_balance(account_id, amount):
    cur = conn.cursor()
    sql = """
    UPDATE Accounts 
    SET account_balance = account_balance + %s
    WHERE account_number = %s
    """
    cur.execute(sql, (amount, account_id))
    conn.commit()
    cur.close()



