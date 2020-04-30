use test;
select * from cars_data;
select distinct(car_make) from cars_data;
select distinct(car_color) from cars_data;
 SELECT AVG(2020 - purchase_year) AS car_age FROM cars_data WHERE car_make = 'Honda';
