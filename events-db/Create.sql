CREATE TABLE IF NOT EXISTS events (
    id INT PRIMARY KEY AUTO_INCREMENT,
    event_name VARCHAR(50) NOT NULL,
    unit_type VARCHAR(50) NOT NULL,
    status_effect VARCHAR(50) NOT NULL,
    date_generated DATE NOT NULL
);