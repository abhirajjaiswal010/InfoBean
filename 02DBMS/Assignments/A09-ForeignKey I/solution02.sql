
-- QNO 2: Hospital - Doctors and Patients Management

USE Assign03;

-- 1. Create Doctors Table

CREATE TABLE IF NOT EXISTS doctor (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    doctor_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(50) NOT NULL UNIQUE
);


-- 2. Create Patients Table

CREATE TABLE IF NOT EXISTS patient (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_name VARCHAR(50) NOT NULL,
    doctor_id INT NOT NULL,

    CONSTRAINT fk_doctor_patient
    FOREIGN KEY (doctor_id)
    REFERENCES doctor(doctor_id)
    ON DELETE CASCADE
);


-- 3. Insert Sample Doctors

INSERT IGNORE INTO doctor(doctor_name, specialization)
VALUES
('Dr. Rajesh Sharma', 'Cardiology'),
('Dr. Priya Verma', 'Neurology'),
('Dr. Amit Patel', 'Orthopedics');


-- 4. Insert Sample Patients

INSERT IGNORE INTO patient(patient_name, doctor_id)
VALUES
('Rahul Mehta', 1),
('Sneha Jain', 1),
('Aarav Gupta', 2),
('Ananya Singh', 2),
('Karan Malhotra', 3);


-- 5. Display All Doctors

SELECT * FROM doctor;


-- 6. Display All Patients

SELECT * FROM patient;


-- 7. Update a Patient's Doctor

UPDATE patient
SET doctor_id = 3
WHERE patient_id = 3;


-- 8. Verify Updated Patient Record

SELECT * FROM patient
WHERE patient_id = 3;


-- 9. Delete a Doctor and Observe ON DELETE CASCADE

DELETE FROM doctor
WHERE doctor_id = 2;


-- 10. Verify Remaining Doctors

SELECT * FROM doctor;


-- 11. Verify Remaining Patients

SELECT * FROM patient;
