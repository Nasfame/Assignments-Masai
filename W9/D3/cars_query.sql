use test;
show tables;
describe cars_data;
select * from cars_data where gender = 'Male' and car_color = 'Pink';
select * from cars_data where gender = 'Female' and car_color = 'Red'or 'Blue';
select * from cars_data where gender = 'Male' and purchase_year = 1998;
select * from cars_data where gender = 'Female' and car_color = 'Yellow' and purchase_year = 1985;
select * from cars_data where gender = 'Male' and car_color = 'Red' or 'Green' and country in ('Germany','Kenya');
select * from cars_data where country = 'India' and purchase_year = 2001;
select * from cars_data where country in ('German','Egypt') and purchase_year = 1985;
select * from cars_data where gender = 'Female' and car_color = 'Blue' and country = 'India';
select * from cars_data where gender = 'Male' and ((country = 'Germany' and purchase_year = 1998));
select * from cars_data where gender = 'Female' and car_color = 'Green' and not country = 'Pakistan';







