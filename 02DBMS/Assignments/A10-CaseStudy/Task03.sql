-- TASK 10
-- Test ON DELETE CASCADE.
-- Delete a patient having appointments.
-- Check the appointment table before and after deletion.
-- Explain what happened.

delete from patient
where patient_id=301;

-- TASK 11
-- Test ON DELETE SET NULL.
-- Delete a doctor.
-- Check the appointment table.
-- Verify that the appointment remains but doctor_id becomes NULL.

delete from doctor
where doctor_id=201;


-- TASK 12
-- Test ON DELETE RESTRICT.
-- Try deleting a medicine that is referenced by prescription_medicine.
-- Observe the error.
-- Explain why MySQL rejected the deletion.

DELETE FROM medicine
WHERE medicine=403;

-- TASK 13
-- Test ON UPDATE CASCADE.
-- Change a department primary key.
-- Verify that the related foreign keys are automatically updated.

UPDATE department
set department_id=105
WHERE department_id=101;

-- TASK 14
-- Test ON UPDATE SET NULL.
-- Change a doctor primary key.
-- Verify that the configured child foreign key becomes NULL.

UPDATE doctor
set doctor_id=206
WHERE doctor_id=205;