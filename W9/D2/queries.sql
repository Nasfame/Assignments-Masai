create database world;
CREATE TABLE ubiquitous (
    continents VARCHAR(30),
    countries VARCHAR(60),
    cities VARCHAR(60)
);
insert into ubiquitous (continents,countries,cities) values ('Asia','India','Delhi');
insert into ubiquitous (continents,countries,cities) values ('Asia','China','Beijing');
insert into ubiquitous (continents,countries,cities) values ('Asia','Japan','Tokyo');
insert into ubiquitous (continents,countries,cities) values ('North America','Canada','Toronto');
insert into ubiquitous (continents,countries,cities) values ('Europe','UK','London');
SELECT 
    *
FROM
    ubiquitous
WHERE
    continents = 'Asia';

UPDATE ubiquitous 
SET 
    cities = 'New Delhi'
WHERE
    countries = 'India';
DELETE FROM ubiquitous 
WHERE
    continents = 'Europe';
truncate table ubiquitous;
drop table ubiquitous;
drop database world;






