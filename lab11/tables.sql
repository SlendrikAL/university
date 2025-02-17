DROP TABLE IF EXISTS 'group_';
DROP TABLE IF EXISTS 'student';
DROP TABLE IF EXISTS 'student_marks';
CREATE TABLE group_ (
  id INT PRIMARY KEY,
  name VARCHAR(255) UNIQUE,
  description VARCHAR(255) UNIQUE);
INSERT INTO 'group_' VALUES(1,'Group_A','Хорошая группа');
INSERT INTO 'group_' VALUES(2,'Group_B','Нормальная группа');
CREATE TABLE student (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  group_id REFERENCES group_ (id));
INSERT INTO 'student' VALUES(1,'Алекс',1);
INSERT INTO 'student' VALUES(2,'Алиса',1);
INSERT INTO 'student' VALUES(3,'Обама',2);
CREATE TABLE student_marks (
  student_id INT REFERENCES student (id),
  math_mark_average FLOAT NOT NULL,
  physics_mark_average FLOAT NOT NULL,
  python_mark_average FLOAT NOT NULL,
  PRIMARY KEY (student_id));
INSERT INTO 'student_marks' VALUES(1,3.34,4.44,3.44);
INSERT INTO 'student_marks' VALUES(2,1.78,4.44,3.44);
INSERT INTO 'student_marks' VALUES(3,5,4.95,4.53);
