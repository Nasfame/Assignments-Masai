select count(*),c.name as class,s.name as section from student as std join class as c on std.class_id = c.id join section as s on s.id = std.section_id group by c.id,s.id order by count(*) desc limit 1;

