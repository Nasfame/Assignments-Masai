use w9d5;
SELECT 
    COUNT(id)
FROM
    students_marks
WHERE
    gender = 'Female';
SELECT 
    COUNT(id)
FROM
    students_marks
WHERE
    gender = 'Male' AND maths > 85
        AND science > 85
        AND english > 85;
SELECT 
    COUNT(id)
FROM
    students_marks
WHERE
    maths BETWEEN 50 AND 75
        AND english BETWEEN 50 AND 75;
SELECT 
    COUNT(id)
FROM
    students_marks
WHERE
    class IN ('I' , 'II', 'III', 'IV', 'V')
        AND maths > 50
        AND science > 50
        AND english > 50;
SELECT 
    *
FROM
    students_marks
WHERE
    gender = 'Female' AND class = 'X'
        AND section = 'A'
        AND maths > 25
        AND science > 25
        AND english > 25;
SELECT 
    *
FROM
    students_marks
WHERE
    class = 'V'
ORDER BY maths DESC
LIMIT 3;
SELECT 
    *
FROM
    students_marks
WHERE
    class = 'I'
ORDER BY science
LIMIT 5;
SELECT 
    *
FROM
    students_marks
WHERE
    section = 'A' AND maths < 50
        AND science < 50
        AND english < 50;
select *
FROM
    students_marks
WHERE
    section='A'
     AND maths < 50
        AND science < 50
        AND english <50;
  select  *
FROM
    students_marks
WHERE
    section='A'
     AND maths < 50
        AND science < 50
        AND english <50;
SELECT 
    *
FROM
    students_marks
WHERE
    section = 'A' AND maths < 50
        AND science < 50
        AND english < 50;
elect
    *
FROM
    students_marks
WHERE
    section='A'
     AND maths < 50
        AND science < 50
        AND english <50;

select
    *
FROM
    students_marks
WHERE
    section='C'
     AND maths >75
        AND science >75
        AND english >75;
        
select * from students_marks order by maths limit 3,10;
select * from students_marks order by science desc limit 5,20;
select * from students_marks where gender = 'Female' order by science,maths limit 4,5;
select * from students_marks where gender = 'Male' order by science desc ,maths desc,english desc limit 3,15;


