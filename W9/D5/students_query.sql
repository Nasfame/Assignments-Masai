use w9d5;
SELECT 
    AVG(maths)
FROM
    students_marks
WHERE
    gender = 'Female';
SELECT 
    AVG(maths), AVG(science), AVG(english)
FROM
    students_marks
WHERE
    gender = 'Male' AND maths > 85
        AND science > 85
        AND english > 85;
SELECT 
    AVG(maths), AVG(science), AVG(english)
FROM
    students_marks
WHERE
    maths BETWEEN 50 AND 75
        AND english BETWEEN 50 AND 75;
SELECT 
    AVG(science + maths + english)
FROM
    students_marks
WHERE
    class IN ('I' , 'II', 'III', 'IV', 'V')
        AND maths > 50
        AND science > 50
        AND english > 50;
SELECT 
    AVG(science + maths + english)
FROM
    students_marks
WHERE
    gender = 'Female' AND class = 'X'
        AND section = 'A'
        AND maths < 25
        AND science < 25
        AND english < 25;
SELECT 
    AVG(maths), AVG(science), AVG(english)
FROM
    students_marks
WHERE
    section = 'A' AND maths < 50
        AND science < 50
        AND english < 50;
SELECT 
    AVG(science + maths + english)
FROM
    students_marks
WHERE
    section = 'C' AND maths > 75
        AND science > 75
        AND english > 75;
SELECT 
    *
FROM
    students_marks
ORDER BY science + maths + english
LIMIT 10;
SELECT 
    *
FROM
    students_marks
ORDER BY (science + maths + english) / 3 DESC
LIMIT 6 , 20;
SELECT 
    *
FROM
    students_marks
WHERE
    gender = 'Female'
ORDER BY (science + maths + english)
LIMIT 2 , 5;
SELECT 
    *
FROM
    students_marks
WHERE
    gender = 'Male'
ORDER BY (science + maths + english) / 3 DESC
LIMIT 4 , 15;
