use test;
select * from cars_data;
select distinct(car_make) from cars_data;
select distinct(car_color) from cars_data;
select avg(purchase_year) from cars_data where car_make = "Honda";
