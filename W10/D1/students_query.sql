select * from students_marks;
#select *,avg(ft.maths) from (select * from students_marks where gender="Female") as ft;
select class,avg(maths) from students_marks where gender="Female" group by class;
#select *,avg(ft.maths) from (select * from students_marks where gender="Female") as ft group by class;
select section,avg(maths),avg(science),avg(english) from students_marks where gender="Male" and maths>85 and english>85 and science>85;
select avg(maths),avg(science),avg(english) from students_marks where gender="Male" and maths between 50 and 75 and science between 50 and 75;
select (maths+science+english)/3 as avg_score,class from students_marks where class in ('I','II','III','IV','V') and maths>50 and english>50 and science>50  group by class;
select name,(maths+science+english)/3 as avg_score from students_marks where class in ('X')  and section in ('A') and  gender="Female" having avg_score<25;
select name,(maths+science+english)/3 as avg_score from students_marks where class in ('X')  and section in ('A') having avg_score<50;
select avg(newtab.totalmarks) as avg_score,class from (select *,(maths+english+science) as "totalmarks" from students_marks where section = "C") as newtab GROUP BY newtab.class;
select class,section,count(gender) as female_count from students_marks where gender="Female" group by class,section;


