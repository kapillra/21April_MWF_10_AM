-- courses table
-- Fields -> id int, course_name varchar(50), duration int


create table courses (
	id int auto_increment,
    course_name varchar(50),
    duration int,
    primary key (id)
);