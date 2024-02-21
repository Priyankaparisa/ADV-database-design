CREATE TABLE Users (
  user_id INT PRIMARY KEY,
  username VARCHAR(50),
  name VARCHAR(100),
  age INT,
  email VARCHAR(100)
);

CREATE TABLE Purchases (
  purchase_id INT PRIMARY KEY,
  user_id INT,
  product VARCHAR(100),
  price DECIMAL(10, 2),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
