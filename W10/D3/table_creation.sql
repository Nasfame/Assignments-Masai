create database W10;
use W10;
create table user (id INT AUTO_INCREMENT not null,name varchar(255),PRIMARY key(id) );
create table countries ( id INT AUTO_INCREMENT not null,name varchar(255),PRIMARY key(id) );
create TABLE city ( id INT AUTO_INCREMENT not null,name varchar(255),country_id int, PRIMARY key(id) , foreign key(country_id) REFERENCES countries(id));
describe city;
