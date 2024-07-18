SELECT AVG(salary) As AverageSalary, department_id As DepartmentId 
FROM employees
GROUP BY department_id;
