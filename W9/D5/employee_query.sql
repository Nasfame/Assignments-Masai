SELECT 
    *
FROM
    employee_salary;
SELECT DISTINCT
    (department)
FROM
    employee_salary;
SELECT DISTINCT
    (company)
FROM
    employee_salary;
SELECT 
    SUM(salary)
FROM
    employee_salary
WHERE
    salary < 80000 AND gender = 'Female';
SELECT 
    company, department
FROM
    employee_salary
WHERE
    salary < 80000;
SELECT 
    AVG(salary)
FROM
    employee_salary
WHERE
    salary < 100000
        AND department = 'Accounting'
        OR 'Legal';
SELECT 
    AVG(salary)
FROM
    employee_salary
WHERE
    gender = 'Male'
ORDER BY salary DESC
LIMIT 10;
SELECT 
    AVG(salary)
FROM
    employee_salary
WHERE
    gender = 'Female'
ORDER BY salary
LIMIT 10;
SELECT 
    AVG(salary)
FROM
    employee_salary
WHERE
    department = 'Engineering';
SELECT 
    AVG(salary)
FROM
    employee_salary
WHERE
    gender = 'Female'
ORDER BY salary
LIMIT 30 , 20;
SELECT 
    SUM(salary)
FROM
    employee_salary
WHERE
    gender = 'Male'
ORDER BY salary
LIMIT 50 , 50;
SELECT 
    SUM(salary) AS total_salary
FROM
    employee_salary
WHERE
    department = 'Engineering'
        AND gender = 'Female'
ORDER BY salary
LIMIT 50;
SELECT 
    AVG(salary)
FROM
    employee_salary
WHERE
    gender = 'Male'
        AND department = 'Human Resources'
ORDER BY salary DESC
LIMIT 50;
