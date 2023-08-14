-- Student table
-- Fields -> id int, student_name, course int

create table students(
	id int not null auto_increment,
    course_id int not null,
    student_name varchar(25),
    primary key (id),
    foreign key (course_id) references courses(id)
)