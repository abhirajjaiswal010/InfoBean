INSERT ignore INTO department
(department_name, floor_no)
VALUES
('Cardiology', 3),
('Neurology', 4),
('Orthopedics', 2),
('Dermatology', 1);

INSERT ignore INTO doctor
(doctor_name, specialization, department_id)
VALUES
('Dr. Rajesh Sharma', 'Cardiologist', 101),
('Dr. Neha Verma', 'Neurologist', 102),
('Dr. Amit Jain', 'Orthopedic', 103),
('Dr. Priya Singh', 'Dermatologist', 104),
('Dr. Karan Mehta', 'Cardiologist', 101);

INSERT ignore INTO patient
(patient_name, gender, city)
VALUES
('Rahul Verma', 'Male', 'Indore'),
('Sneha Sharma', 'Female', 'Bhopal'),
('Amit Patel', 'Male', 'Indore'),
('Pooja Gupta', 'Female', 'Ujjain'),
('Rohan Jain', 'Male', 'Dewas'),
('Neha Patel', 'Female', 'Indore');

INSERT ignore INTO medicine
(medicine_name, manufacturer, price)
VALUES
('Paracetamol', 'ABC Pharma', 30),
('Azithromycin', 'XYZ Pharma', 120),
('Pantoprazole', 'MedLife', 80),
('Amoxicillin', 'HealthCare Pharma', 150),
('Ibuprofen', 'ABC Pharma', 60),
('Cetirizine', 'MedLife', 45);

INSERT ignore INTO appointment
(appointment_date, appointment_time, patient_id, doctor_id, department_id, status)
VALUES
('2026-09-01', '10:00:00', 301, 201, 101, 'Completed'),
('2026-09-01', '11:00:00', 302, 202, 102, 'Completed'),
('2026-09-02', '09:30:00', 303, 203, 103, 'Completed'),
('2026-09-02', '12:00:00', 304, 204, 104, 'Cancelled'),
('2026-09-03', '10:30:00', 301, 205, 101, 'Completed'),
('2026-09-03', '11:30:00', 305, 203, 103, 'Completed'),
('2026-09-04', '09:00:00', 306, 201, 101, 'Scheduled'),
('2026-09-04', '14:00:00', 302, 202, 102, 'Scheduled');

INSERT ignore INTO prescription
(prescription_date, appointment_id, patient_id, doctor_id, remarks)
VALUES
('2026-09-01', 501, 301, 201, 'BP observation'),
('2026-09-01', 502, 302, 202, 'Migraine treatment'),
('2026-09-02', 503, 303, 203, 'Knee pain'),
('2026-09-03', 505, 301, 205, 'Heart checkup'),
('2026-09-03', 506, 305, 203, 'Back pain');

INSERT ignore INTO PrescriptionMedicine
(prescription_id, medicine_id, dosage, duration_days, quantity)
VALUES
(601, 401, '1-0-1', 5, 10),
(601, 403, '1-0-0', 5, 5),
(602, 403, '1-0-0', 7, 7),
(602, 406, '0-0-1', 5, 5),
(603, 405, '1-0-1', 5, 10),
(603, 403, '1-0-0', 5, 5),
(604, 401, '1-0-1', 3, 6),
(604, 403, '1-0-0', 3, 3),
(605, 405, '1-0-1', 7, 14);