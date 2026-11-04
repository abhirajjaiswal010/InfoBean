
CREATE DATABASE IF NOT EXISTS CaseStudy;
USE CaseStudy;


-- 1. DEPARTMENT TABLE

CREATE TABLE IF NOT EXISTS department (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(50) NOT NULL,
    floor_no INT
) AUTO_INCREMENT = 101;


-- 2. DOCTOR TABLE

CREATE TABLE IF NOT EXISTS doctor (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    doctor_name VARCHAR(30),
    specialization VARCHAR(30),
    department_id INT,

    CONSTRAINT fk_doctor_department
    FOREIGN KEY (department_id)
    REFERENCES department(department_id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
) AUTO_INCREMENT = 201;


-- 3. PATIENT TABLE

CREATE TABLE IF NOT EXISTS patient (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_name VARCHAR(40),
    gender ENUM('male', 'female', 'other'),
    city VARCHAR(40)
) AUTO_INCREMENT = 301;


-- 4. MEDICINE TABLE

CREATE TABLE IF NOT EXISTS medicine (
    medicine_id INT PRIMARY KEY AUTO_INCREMENT,
    medicine_name VARCHAR(100),
    manufacturer VARCHAR(100),
    price DECIMAL(10,2)
) AUTO_INCREMENT = 401;


-- 5. APPOINTMENT TABLE

CREATE TABLE IF NOT EXISTS appointment (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    appointment_date DATE,
    appointment_time TIME,
    patient_id INT,
    doctor_id INT,
    department_id INT,
    status VARCHAR(50),

    CONSTRAINT fk_appointment_patient
    FOREIGN KEY (patient_id)
    REFERENCES patient(patient_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

    CONSTRAINT fk_appointment_doctor
    FOREIGN KEY (doctor_id)
    REFERENCES doctor(doctor_id)
    ON DELETE SET NULL
    ON UPDATE SET NULL,

    CONSTRAINT fk_appointment_department
    FOREIGN KEY (department_id)
    REFERENCES department(department_id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
) AUTO_INCREMENT = 501;


-- 6. PRESCRIPTION TABLE

CREATE TABLE IF NOT EXISTS prescription (
    prescription_id INT PRIMARY KEY AUTO_INCREMENT,
    prescription_date DATE,
    appointment_id INT UNIQUE,
    patient_id INT,
    doctor_id INT,
    remarks VARCHAR(200),

    CONSTRAINT fk_prescription_appointment
    FOREIGN KEY (appointment_id)
    REFERENCES appointment(appointment_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

    CONSTRAINT fk_prescription_patient
    FOREIGN KEY (patient_id)
    REFERENCES patient(patient_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

    CONSTRAINT fk_prescription_doctor
    FOREIGN KEY (doctor_id)
    REFERENCES doctor(doctor_id)
    ON DELETE SET NULL
    ON UPDATE SET NULL
) AUTO_INCREMENT = 601;


-- 7. PRESCRIPTION_MEDICINE TABLE

CREATE TABLE IF NOT EXISTS prescriptionMedicine (
    prescription_id INT,
    medicine_id INT,
    dosage VARCHAR(20),
    duration_days INT,
    quantity INT,

    CONSTRAINT pk_prescription_medicine
    PRIMARY KEY (prescription_id, medicine_id),

    CONSTRAINT fk_prescriptionMedicine_prescription
    FOREIGN KEY (prescription_id)
    REFERENCES prescription(prescription_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

    CONSTRAINT fk_prescriptionMedicine_medicine
    FOREIGN KEY (medicine_id)
    REFERENCES medicine(medicine_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);



