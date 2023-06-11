\i schema_drop.sql

CREATE TABLE IF NOT EXISTS Users(
	username varchar(10) PRIMARY KEY,
	password varchar(120),
);

-- Solving the accounts ISA Hierachy. 
-- (-)relational style. In this case every entity is implemented
-- -objects atyle. In this case only typed objects. Implement a type on manages
-- -nulls style. In this case only accounts

-- Serial this is the account number across the system
-- 

CREATE TABLE IF NOT EXISTS Accounts(
	account_number SERIAL PRIMARY KEY,
	created_date date,
	CPR_number integer  REFERENCES Customers(CPR_number)
);


CREATE TABLE IF NOT EXISTS Owns(
	username INTEGER NOT NULL REFERENCES Users(username),
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


