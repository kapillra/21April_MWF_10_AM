-- Faculty table
-- Fields -> id int, faculty_name varhcar(25), course

create table faculty (
	id int,
    course_id int,
    faculty_name varchar(25),
    primary key (id),
    foreign key (course_id) references courses(id)
);