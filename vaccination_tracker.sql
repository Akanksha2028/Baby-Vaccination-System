create database Vaccination_tracker;
use Vaccination_tracker;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(150) UNIQUE,
    role ENUM('admin', 'user') DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE vaccination_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    baby_name VARCHAR(100) NOT NULL,
    parent_name VARCHAR(100),
    vaccine_name VARCHAR(100),
    dose_number INT,
    vaccination_date DATE,
    next_due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE
);
INSERT INTO users (username, password, email, role)
VALUES
('akanksha', '12345', 'akanksha@gmail.com', 'admin'),
('rohit', '12345', 'rohit@gmail.com', 'user'),
('sneha', '12345', 'sneha@gmail.com', 'user'),
('amit', '12345', 'amit@gmail.com', 'user'),
('priya', '12345', 'priya@gmail.com', 'user');
SELECT * From users;

INSERT INTO vaccination_records 
(user_id, baby_name, parent_name, vaccine_name, dose_number, vaccination_date, next_due_date)
VALUES
(1, 'Rahul', 'Akanksha', 'Polio', 1, '2026-03-01', '2026-04-01'),
(2, 'Riya', 'Rohit', 'BCG', 1, '2026-03-05', '2026-04-05'),
(3, 'Arjun', 'Sneha', 'Hepatitis B', 2, '2026-03-10', '2026-04-10'),
(4, 'Anaya', 'Amit', 'DPT', 1, '2026-03-12', '2026-04-12'),
(5, 'Kabir', 'Priya', 'MMR', 1, '2026-03-15', '2026-04-15');
SELECT * From vaccination_records;

