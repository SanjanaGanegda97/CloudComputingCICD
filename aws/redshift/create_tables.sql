CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY,
    doctor_id INT,
    patient_id INT,
    condition VARCHAR(255),
    appointment_date DATE
);

CREATE TABLE metrics (
    metric_id INT IDENTITY(1,1) PRIMARY KEY,
    metric_name VARCHAR(255),
    metric_value FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
