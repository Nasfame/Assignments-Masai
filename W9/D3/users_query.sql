#create DATABASE test;
show databases;
use test;
#/. J:\3D objects\SWD\learn_db.sql;
show TABLES;
select name from user_data where gender = 'Female';
select name,language from user_data where gender = 'Female' and language in ('Kannada','Hindi');
select * from user_data where shirt_size = 'S';
select name from user_data where gender = 'Female' and  shirt_size = 'XL';
select * from user_data where gender = 'Male' and language = 'English' or (gender = 'Female' and language = 'Hindi');
select * from user_data where gender = 'Male' and language in ('Hindi','English') or (gender = 'Female' and language in ('Kanada','German'));
select * from user_data where gender = 'Female' and shirt_size = 'XL' or (gender = 'Male' and language = 'German' and shirt_size in ('XL','M'));
select * from user_data where gender = 'Female'and language in ('Hindi','Punjabi','Bengali','Tamil','Malayalam','Gujarati');
select * from user_data where gender = 'Male' and language = 'Korean';





