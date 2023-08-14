-- fetch records from multiple tables using join

select students.student_name, courses.course_name, courses.duration, faculty.faculty_name
from courses
join students on students.course_id = courses.id
join faculty on faculty.course_id = courses.id;