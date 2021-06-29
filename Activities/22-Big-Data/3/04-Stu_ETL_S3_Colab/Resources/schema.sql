-- Table schema
CREATE TABLE employee_personal_info (
  employee_id INTEGER PRIMARY KEY NOT NULL,
  email VARCHAR,
  marital_status VARCHAR,
  gender VARCHAR,
  salaried VARCHAR  
);

CREATE TABLE employee_password (
	employee_id INT PRIMARY KEY NOT NULL,
	password TEXT
);
