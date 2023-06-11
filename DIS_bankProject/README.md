# DIS_GroupProject
HOW TO RUN THE WEB APPLICATION:

Make sure you have Python and flask installed (verify this by flask --version)
Otherwise install using "pip install flask"

1. Open a terminal and change directory to DIS_bankProject

2. type the following command: "python run.py" open a browser and go to http://127.0.0.1:5000

3. Click on login in the navigation bar and login using one of our dummy accounts:
    Username: john123
    Password: P@ssw0rd123! (this is the same for all the users in the database)

4. After logging in you should be moved to the transaction page where you can move money 
    to you different accounts.

SETTING UP THE DATABASE:

1. Open pgadmin or your prefered database management tool (dbeaver)

2. Create a database called "bank" (or whatever - you can change it in the __init__.py file if you want)

3. Run the scripts in this order: "schema_drop.sql", "schema.sql", "schema_ins.sql"

After making a transaction it should now be possible to see that the database changes accordingly.
