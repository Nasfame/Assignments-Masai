select name from city where country_id = (select id from countries where name="US");