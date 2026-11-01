use Assign03;
CREATE TABLE if NOT EXISTS student (
    student_id INT primary key auto_increment,
    student_name varchar(20) NOT NULL
);
CREATE TABLE if NOT EXISTS exam (
    exam_id INT primary key auto_increment,
    subject_name varchar(20) NOT NULL unique
);
CREATE TABLE if NOT EXISTS result (
    result_id INT primary key auto_increment,
    student_id INT NOT null,
    exam_id INT NOT null,
    score INT NOT NULL check (
        score BETWEEN 0 AND 100
    ),
    constraint fk_result_student foreign key (student_id) references student(student_id),
    constraint fk_result_exam foreign key(exam_id) references exam(exam_id)
);
INSERT IGNORE INTO student(student_name)
VALUES ('Rahul Sharma'),
    ('Priya Verma'),
    ('Amit Patel');
INSERT IGNORE INTO exam (subject_name)
VALUES ('Database Management System'),
    ('Java Programming'),
    ('Computer Networks');
INSERT IGNORE INTO result (student_id, exam_id, score)
VALUES (1, 1, 85),
    (1, 2, 90),
    (2, 1, 78),
    (2, 3, 88),
    (3, 2, 92);
ALTER TABLE result DROP foreign key fk_result_student,
    DROP foreign key fk_result_exam;
ALTER TABLE result
add constraint fk_result_student foreign key (student_id) references student(student_id) on DELETE CASCADE,
    add constraint fk_result_exam foreign key (exam_id) references exam(exam_id);
-- Delete a student and verify that their associated results are automatically deleted.
delete from student
where student_id = 2;

select r.result_id,
    s.student_name,
    e.subject_name,
    r.score
from result r,
    student s,
    exam e
where r.student_id = s.student_id
    and r.exam_id = e.exam_id;


-- Update an exam's subject name and observe the effect.

update exam
set subject_name="IoT"
where exam_id=1;