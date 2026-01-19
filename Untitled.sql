-- 데이터 베이스 생성
CREATE DATABASE oz_db_test;
-- 데이터 베이스 사용
USE oz_db_test;

-- employees 테이블 생성
CREATE TABLE employees(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2)
);

-- 직원 데이터 employees 테이블에 추가
INSERT INTO employees (name, position, salary)
VALUES
('혜린', 'PM', 90000),
('은우','Frontend', 80000),
('가을','Backend', 92000),
('지수','Frontend', 78000),
('민혁','Frontend', 96000),
('하은','Backend', 130000);

-- 모든 직원의 연봉 및 정보 조회
SELECT * FROM employees;

-- Frontend 직책을 가진 인원 중 연봉이 90000 이하인 직원 조회
SELECT name, salary 
FROM employees 
WHERE position = 'Frontend' AND salary <= 90000;

-- PM 직책을 가진 직원의 연봉 인상 및 결과 확인
UPDATE employees
SET salary = salary * 1.10
WHERE position = 'PM';
SELECT * FROM employees WHERE position = 'PM';

-- 모든 Backend 직책을 가진 직원의 연봉 인상
UPDATE employees
SET salary = salary * 1.05
WHERE position = 'Backend';

-- 민혁 사원의 데이터 삭제
DELETE FROM employees WHERE name = '민혁';

-- 모든 직원을 position별로 그룹화 시킨 뒤 각 직책의 평균 연봉 계산
SELECT position, AVG(salary) AS average_salary FROM employees GROUP BY position;

-- employees 테이블 삭제
DROP TABLE employees;