select * from employee_salary;
select avg(salary) as avg_salary,department from employee_salary GROUP BY department;
select avg(salary),company from employee_salary group by company;
select count(*) as counting,company,department from employee_salary where salary<1000000 group by company,department;
select avg(salary) as avg_engine from employee_salary where salary<100000 and department="Engineering";
select department,sum(salary) from employee_salary where gender = "Female" GROUP BY department;
select company,avg(salary) from employee_salary where department="Human Resources" group by company;
