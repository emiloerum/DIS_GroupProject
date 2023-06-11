DELETE FROM Users;
DELETE FROM Accounts;
DELETE FROM Transfers;

-- Insert statements for Users Table
-- Password is randomly generated and hashed.
INSERT INTO Users (username, password)
VALUES ('john123', '$2b$12$liXkFXgFcxyEehQo3fZTKOd4x23wAaoLMX6nyCnbSlF5fhKrQkO6q'),
       ('emma456', '$2b$12$liXkFXgFcxyEehQo3fZTKOd4x23wAaoLMX6nyCnbSlF5fhKrQkO6q'),
       ('alex789', '$2b$12$liXkFXgFcxyEehQo3fZTKOd4x23wAaoLMX6nyCnbSlF5fhKrQkO6q'),
       ('lily222', '$2b$12$liXkFXgFcxyEehQo3fZTKOd4x23wAaoLMX6nyCnbSlF5fhKrQkO6q'),
       ('mark777', '$2b$12$liXkFXgFcxyEehQo3fZTKOd4x23wAaoLMX6nyCnbSlF5fhKrQkO6q');

-- Insert statements for Accounts Table
INSERT INTO Accounts (account_number, account_name, account_balance)
VALUES (1, 'Savings', 5000),
       (2, 'Checking', 2500),
       (3, 'Investment', 10000),
       (4, 'Savings', 2000),
       (5, 'Checking', 1500),
       (6, 'Savings', 3000),
       (7, 'Checking', 4000),
       (8, 'Investment', 8000),
       (9, 'Checking', 1000),
       (10, 'Savings', 6000);

-- Insert statements for Owns Table
INSERT INTO Owns (username, account_number)
VALUES ('john123', 1),
       ('john123', 2),
       ('emma456', 3),
       ('emma456', 4),
       ('alex789', 5),
       ('alex789', 6),
       ('lily222', 7),
       ('lily222', 8),
       ('mark777', 9),
       ('mark777', 10);
