-- Might not work. If not, run schema_drop manually and remove this line
\i schema_drop.sql

CREATE TABLE IF NOT EXISTS Users(
	username varchar(20) PRIMARY KEY,
	password varchar(120)
);

CREATE TABLE IF NOT EXISTS Accounts (
    account_number SERIAL PRIMARY KEY,
    account_name VARCHAR(60) CHECK (account_name IN ('Savings', 'Checking', 'Investment')),
    account_balance INTEGER CHECK (account_balance >= 0)
);



CREATE TABLE IF NOT EXISTS Owns(
	username varchar(20) NOT NULL REFERENCES Users(username),
	account_number INTEGER NOT NULL REFERENCES accounts
);
ALTER TABLE Owns ADD CONSTRAINT pk_manages
  PRIMARY KEY (username, account_number)
  ;

-- transfers
CREATE TABLE IF NOT EXISTS Transfers(
	id SERIAL PRIMARY KEY,
	transfer_date date,
	amount INTEGER,
	from_account  INTEGER REFERENCES accounts(account_number),
	to_account    INTEGER REFERENCES accounts(account_number)
);


