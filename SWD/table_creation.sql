create DATABASE School;
use School;
create table teacher (id int AUTO_INCREMENT not null, name varchar(150) unique,PRIMARY KEY(id));
create table class (id int AUTO_INCREMENT not null, name varchar(10) unique,PRIMARY KEY(id));
create table section (id int AUTO_INCREMENT not null, name varchar(10) unique,PRIMARY KEY(id), teacher_id int, FOREIGN KEY(teacher_id) REFERENCES teacher(id));
create table student (id int AUTO_INCREMENT not null,PRIMARY KEY(id), name varchar(150) unique,gender varchar(1),class_id int, FOREIGN KEY (class_id) REFERENCES class(id),section_id int, FOREIGN KEY (section_id) REFERENCES section(id));

#desc teacher;
#drop database School;