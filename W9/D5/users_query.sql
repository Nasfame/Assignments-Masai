use test;
SELECT 
    *
FROM
    user_data;
SELECT DISTINCT
    (shirt_size)
FROM
    user_data;
SELECT DISTINCT
    (language)
FROM
    user_data;
SELECT 
    COUNT(*)
FROM
    user_data
WHERE
    gender = 'Female' AND name LIKE '%a'
        OR '%e'
        OR '%o'
        OR '%i'
        OR '%u';
SELECT 
    COUNT(*)
FROM
    user_data
WHERE
    gender = 'Male' AND name LIKE '_a%'
        OR '_e%'
        OR '_o%'
        OR '_i%'
        OR '_u%';
SELECT 
    COUNT(*)
FROM
    user_data
WHERE
    name LIKE 'a%a';
SELECT 
    COUNT(*)
FROM
    user_data
WHERE
    name LIKE '%z%';
SELECT 
    COUNT(*)
FROM
    user_data
WHERE
    gender = 'Male' AND name LIKE '%dev%';
