from bank import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql


def select_User(username):
# Change name of database at some point
    cur = conn.cursor()
    sql = """
    SELECT * FROM Customer
    WHERE username = %s
    """
    cur.execute(sql, (username,))
    user = Customer(cur.fetchone()) if cur.rowcount > 0 else None
    cur.close()
    return user



@login_manager.user_loader
def load_user(username):
    select_User(username)

class Customer(tuple, UserMixin):
    def __init__(self, user_data):
        self.username = user_data[0]
        self.password = user_data[1]


    def get_id(self):
       return (self.username)

def select_user_accounts(username):
    cur = conn.cursor()
    sql = """
    SELECT
      a.account_name Accounts
    , a.account_balance Accounts
    FROM Owns o
      NATURAL JOIN Accounts a on o.account_number = a.account_number 
	WHERE o.username = %s
    ;
    """
    cur.execute(sql, (username,))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset

