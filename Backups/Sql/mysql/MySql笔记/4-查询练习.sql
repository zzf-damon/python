
-- mysql查询练习


-- 学生表
-- Student
-- 学号
-- 姓名
-- 性别
-- 出生年月日
-- 所在班级
create table student(
	sno varchar(20) primary key,
	sname varchar(20) not null,
	ssex varchar(10) not null,
	sbirthday datetime,
	class varchar(20)
);

-- 教师表
-- Teacher
-- 教师编号
-- 教师名字
-- 教师性别
-- 出生年月日
-- 职称
-- 所在部门
create table teacher(
	tno varchar(20) primary key,
	tname varchar(20) not null,
	tsex varchar(10) not null,
	tbirthday datetime,
	prof varchar(20) not null,
	depart varchar(20) not null
);

-- 课程表
-- Course
-- 课程号
-- 课程名称
-- 教师编号
create table course(
	cno varchar(20) primary key,
	cname varchar(20) not null,
	tno varchar(20) not null,
	foreign key(tno) references teacher(tno)
);


-- 成绩表
-- Score
-- 学号
-- 课程号
-- 成绩
create table score(
	sno varchar(20) not null,
	cno varchar(20) not null,
	degree decimal,
	foreign key(sno) references student(sno),
	foreign key(cno) references course(cno),
	primary key(sno, cno)
);


-- 往数据表中添加数据
#添加学生信息
insert into student values('101','曾华','男','1977-09-01','95033');
insert into student values('102','匡明','男','1975-10-02','95031');
insert into student values('103','王丽','女','1976-01-23','95033');
insert into student values('104','李军','男','1976-02-20','95033');
insert into student values('105','王芳','女','1975-02-10','95031');
insert into student values('106','陆君','男','1974-06-03','95031');
insert into student values('107','王尼玛','男','1976-02-20','95033');
insert into student values('108','张全蛋','男','1975-02-10','95031');
insert into student values('109','赵铁柱','男','1974-06-03','95031');


#添加教师表
insert into teacher values('804','李诚','男','1958-12-02','副教授','计算机系');
insert into teacher values('856','张旭','男','1969-03-12','讲师','电子工程系');
insert into teacher values('825','王萍','女','1972-05-05','助教','计算机系');
insert into teacher values('831','刘冰','女','1977-08-14','助教','电子工程系');



#添加课程表
insert into course values('3-105','计算机导论','825');
insert into course values('3-245','操作系统','804');
insert into course values('6-166','数字电路','856');
insert into course values('9-888','高等数学','831');


#添加成绩表
insert into score values('103','3-105','92');
insert into score values('103','3-245','86');
insert into score values('103','6-166','85');
insert into score values('105','3-105','88');
insert into score values('105','3-245','75');
insert into score values('105','6-166','79');
insert into score values('109','3-105','76');
insert into score values('109','3-245','68');
insert into score values('109','6-166','81');


-- 查询练习：

-- 1、 查询student表的所有记录。
mysql> select * from student;
+-----+-----------+------+---------------------+-------+
| sno | sname     | ssex | sbirthday           | class |
+-----+-----------+------+---------------------+-------+
| 101 | 曾华      | 男   | 1977-09-01 00:00:00 | 95033 |
| 102 | 匡明      | 男   | 1975-10-02 00:00:00 | 95031 |
| 103 | 王丽      | 女   | 1976-01-23 00:00:00 | 95033 |
| 104 | 李军      | 男   | 1976-02-20 00:00:00 | 95033 |
| 105 | 王芳      | 女   | 1975-02-10 00:00:00 | 95031 |
| 106 | 陆君      | 男   | 1974-06-03 00:00:00 | 95031 |
| 107 | 王尼玛    | 男   | 1976-02-20 00:00:00 | 95033 |
| 108 | 张全蛋    | 男   | 1975-02-10 00:00:00 | 95031 |
| 109 | 赵铁柱    | 男   | 1974-06-03 00:00:00 | 95031 |
+-----+-----------+------+---------------------+-------+
9 rows in set (0.01 sec)


-- 2、 查询student表中的所有记录的 sname 、 ssex 和 class 列。
mysql> select sname, ssex, class from student;
+-----------+------+-------+
| sname     | ssex | class |
+-----------+------+-------+
| 曾华      | 男   | 95033 |
| 匡明      | 男   | 95031 |
| 王丽      | 女   | 95033 |
| 李军      | 男   | 95033 |
| 王芳      | 女   | 95031 |
| 陆君      | 男   | 95031 |
| 王尼玛    | 男   | 95033 |
| 张全蛋    | 男   | 95031 |
| 赵铁柱    | 男   | 95031 |
+-----------+------+-------+
9 rows in set (0.00 sec)


-- 3、 查询教师所有的单位即不重复的depart列。
-- distinct 排除重复
mysql> select distinct depart from teacher;
+-----------------+
| depart          |
+-----------------+
| 计算机系        |
| 电子工程系      |
+-----------------+
2 rows in set (0.02 sec)


-- 4、 查询score表中成绩在60到80之间的所有记录。
-- 查询区间 between ... and ...
mysql> select * from score where degree between 60 and 80;
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 105 | 3-245 |     75 |
| 105 | 6-166 |     79 |
| 109 | 3-105 |     76 |
| 109 | 3-245 |     68 |
+-----+-------+--------+
4 rows in set (0.02 sec)

-- 直接使用运算符比较
mysql> select * from score where degree > 60 and degree < 80;
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 105 | 3-245 |     75 |
| 105 | 6-166 |     79 |
| 109 | 3-105 |     76 |
| 109 | 3-245 |     68 |
+-----+-------+--------+
4 rows in set (0.02 sec)


-- 5、 查询score表中成绩为85，86或88的记录。
-- 表示或者关系的查询 in
mysql> select * from score where degree in(85, 86, 88);
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 103 | 3-245 |     86 |
| 103 | 6-166 |     85 |
| 105 | 3-105 |     88 |
+-----+-------+--------+
3 rows in set (0.02 sec)


-- 6、 查询student表中“95031”班或性别为“女”的同学记录。
-- or 表示或者
mysql> select * from student where class='95031' or ssex='女';
+-----+-----------+------+---------------------+-------+
| sno | sname     | ssex | sbirthday           | class |
+-----+-----------+------+---------------------+-------+
| 102 | 匡明      | 男   | 1975-10-02 00:00:00 | 95031 |
| 103 | 王丽      | 女   | 1976-01-23 00:00:00 | 95033 |
| 105 | 王芳      | 女   | 1975-02-10 00:00:00 | 95031 |
| 106 | 陆君      | 男   | 1974-06-03 00:00:00 | 95031 |
| 108 | 张全蛋    | 男   | 1975-02-10 00:00:00 | 95031 |
| 109 | 赵铁柱    | 男   | 1974-06-03 00:00:00 | 95031 |
+-----+-----------+------+---------------------+-------+
6 rows in set (0.00 sec)


-- 7、 以class降序查询student表的所有记录。
-- 升序，降序
mysql> select * from student order by class desc;
+-----+-----------+------+---------------------+-------+
| sno | sname     | ssex | sbirthday           | class |
+-----+-----------+------+---------------------+-------+
| 101 | 曾华      | 男   | 1977-09-01 00:00:00 | 95033 |
| 103 | 王丽      | 女   | 1976-01-23 00:00:00 | 95033 |
| 104 | 李军      | 男   | 1976-02-20 00:00:00 | 95033 |
| 107 | 王尼玛    | 男   | 1976-02-20 00:00:00 | 95033 |
| 102 | 匡明      | 男   | 1975-10-02 00:00:00 | 95031 |
| 105 | 王芳      | 女   | 1975-02-10 00:00:00 | 95031 |
| 106 | 陆君      | 男   | 1974-06-03 00:00:00 | 95031 |
| 108 | 张全蛋    | 男   | 1975-02-10 00:00:00 | 95031 |
| 109 | 赵铁柱    | 男   | 1974-06-03 00:00:00 | 95031 |
+-----+-----------+------+---------------------+-------+
9 rows in set (0.00 sec)

-- asc; 升序
select * from student order by class; 


-- 8、 以cno升序、degree降序查询score表的所有记录。
mysql> select * from score order by cno asc,degree desc;
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 103 | 3-105 |     92 |
| 105 | 3-105 |     88 |
| 109 | 3-105 |     76 |
| 103 | 3-245 |     86 |
| 105 | 3-245 |     75 |
| 109 | 3-245 |     68 |
| 103 | 6-166 |     85 |
| 109 | 6-166 |     81 |
| 105 | 6-166 |     79 |
+-----+-------+--------+
9 rows in set (0.00 sec)


-- 9、 查询“95031”班的学生人数。
-- 统计 count
mysql> select count(*) from student where class='95031';
+----------+
| count(*) |
+----------+
|        5 |
+----------+
1 row in set (0.01 sec)


-- 10、查询score表中的最高分的学生学号和课程号。（子查询或者排序）
mysql> select sno,cno from score where degree=(select max(degree) from score);
+-----+-------+
| sno | cno   |
+-----+-------+
| 103 | 3-105 |
+-----+-------+
1 row in set (0.01 sec)

-- 1 找到最高分
select max(degree) from score;

-- 2 找最高分的 sno 和 cno

select sno,cno from score where degree=(select max(degree) from score);


-- 排序的做法：
select sno,cno,degree from score order by degree;

mysql> select sno,cno,degree from score order by degree;
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 109 | 3-245 |     68 |
| 105 | 3-245 |     75 |
| 109 | 3-105 |     76 |
| 105 | 6-166 |     79 |
| 109 | 6-166 |     81 |
| 103 | 6-166 |     85 |
| 103 | 3-245 |     86 |
| 105 | 3-105 |     88 |
| 103 | 3-105 |     92 |
+-----+-------+--------+
9 rows in set (0.00 sec)

-- select sno,cno,degree from score order by degree desc limit 0,1;
-- limit 第一个数子表示从多少开始
-- 第二个数子表示查多少条
mysql> select sno,cno,degree from score order by degree desc limit 0,1;
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 103 | 3-105 |     92 |
+-----+-------+--------+
1 row in set (0.00 sec)


-- 11、查询每门课的平均成绩。

select * from course;

-- avg()
select avg(degree) from score where cno='3-105';
select avg(degree) from score where cno='3-245';
select avg(degree) from score where cno='6-166';
select avg(degree) from score where cno='9-888';


select degree from score where cno='3-105';

-- 我能不能够在一个 sql 语句中写呢？
-- group by 分组
select cno,avg(degree) from score group by cno;


-- 12、查询score表中至少有2名学生选修的并以3开头的课程的平均分数。


select cno,avg(degree),count(*) from score 
group by cno 
having count(cno)>=2 
and cno like '3%';


mysql> select cno,avg(degree),count(*) from score group by cno 
    -> having count(cno)>=2 and cno like '3%';
+-------+-------------+----------+
| cno   | avg(degree) | count(*) |
+-------+-------------+----------+
| 3-105 |     85.3333 |        3 |
| 3-245 |     76.3333 |        3 |
+-------+-------------+----------+
2 rows in set (0.00 sec)


-- 13、查询分数大于70，小于90的sno列。

select sno,degree from score
where degree between 70 and 90;
-- where degree>70 and degree<90;

mysql> select sno,degree from score
    -> where degree>70 and degree<90;
+-----+--------+
| sno | degree |
+-----+--------+
| 103 |     86 |
| 103 |     85 |
| 105 |     88 |
| 105 |     75 |
| 105 |     79 |
| 109 |     76 |
| 109 |     81 |
+-----+--------+
7 rows in set (0.00 sec)

mysql> select sno,degree from score
    -> where degree between 70 and 90;
+-----+--------+
| sno | degree |
+-----+--------+
| 103 |     86 |
| 103 |     85 |
| 105 |     88 |
| 105 |     75 |
| 105 |     79 |
| 109 |     76 |
| 109 |     81 |
+-----+--------+
7 rows in set (0.01 sec)



-- 14、查询所有学生的 sname、cno 和 degree 列。


mysql> select sno,sname from student;
+-----+-----------+
| sno | sname     |
+-----+-----------+
| 101 | 曾华      |
| 102 | 匡明      |
| 103 | 王丽      |
| 104 | 李军      |
| 105 | 王芳      |
| 106 | 陆君      |
| 107 | 王尼玛    |
| 108 | 张全蛋    |
| 109 | 赵铁柱    |
+-----+-----------+
9 rows in set (0.00 sec)


mysql> select sno,cno,degree from score;
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 103 | 3-105 |     92 |
| 103 | 3-245 |     86 |
| 103 | 6-166 |     85 |
| 105 | 3-105 |     88 |
| 105 | 3-245 |     75 |
| 105 | 6-166 |     79 |
| 109 | 3-105 |     76 |
| 109 | 3-245 |     68 |
| 109 | 6-166 |     81 |
+-----+-------+--------+
9 rows in set (0.00 sec)


mysql> select sname,cno,degree from student,score
    -> where student.sno=score.sno;
+-----------+-------+--------+
| sname     | cno   | degree |
+-----------+-------+--------+
| 王丽      | 3-105 |     92 |
| 王丽      | 3-245 |     86 |
| 王丽      | 6-166 |     85 |
| 王芳      | 3-105 |     88 |
| 王芳      | 3-245 |     75 |
| 王芳      | 6-166 |     79 |
| 赵铁柱    | 3-105 |     76 |
| 赵铁柱    | 3-245 |     68 |
| 赵铁柱    | 6-166 |     81 |
+-----------+-------+--------+
9 rows in set (0.00 sec)


-- 15、查询所有学生的sno、cname和degree列。

mysql> select cno,cname from course;
+-------+-----------------+
| cno   | cname           |
+-------+-----------------+
| 3-105 | 计算机导论      |
| 3-245 | 操作系统        |
| 6-166 | 数字电路        |
| 9-888 | 高等数学        |
+-------+-----------------+
4 rows in set (0.00 sec)

select cno,sno,degree from score;
mysql> select cno,sno,degree from score;
+-------+-----+--------+
| cno   | sno | degree |
+-------+-----+--------+
| 3-105 | 103 |     92 |
| 3-245 | 103 |     86 |
| 6-166 | 103 |     85 |
| 3-105 | 105 |     88 |
| 3-245 | 105 |     75 |
| 6-166 | 105 |     79 |
| 3-105 | 109 |     76 |
| 3-245 | 109 |     68 |
| 6-166 | 109 |     81 |
+-------+-----+--------+
9 rows in set (0.00 sec)


mysql> select sno,cname,degree from course,score
    -> where course.cno = score.cno;
+-----+-----------------+--------+
| sno | cname           | degree |
+-----+-----------------+--------+
| 103 | 计算机导论      |     92 |
| 105 | 计算机导论      |     88 |
| 109 | 计算机导论      |     76 |
| 103 | 操作系统        |     86 |
| 105 | 操作系统        |     75 |
| 109 | 操作系统        |     68 |
| 103 | 数字电路        |     85 |
| 105 | 数字电路        |     79 |
| 109 | 数字电路        |     81 |
+-----+-----------------+--------+
9 rows in set (0.00 sec)



-- 16、查询所有学生的sname、cname和degree列。

-- sname -> student
-- cname -> course
-- degree -> score

select sname,cname,degree,student.sno as stu_sno,score.sno,course.cno as cou_cno,score.cno from student,course,score
where student.sno=score.sno 
and course.cno=score.cno;


mysql> select sname,cname,degree from student,course,score
    -> where student.sno=score.sno 
    -> and course.cno=score.cno;
+-----------+-----------------+--------+
| sname     | cname           | degree |
+-----------+-----------------+--------+
| 王丽      | 计算机导论      |     92 |
| 王丽      | 操作系统        |     86 |
| 王丽      | 数字电路        |     85 |
| 王芳      | 计算机导论      |     88 |
| 王芳      | 操作系统        |     75 |
| 王芳      | 数字电路        |     79 |
| 赵铁柱    | 计算机导论      |     76 |
| 赵铁柱    | 操作系统        |     68 |
| 赵铁柱    | 数字电路        |     81 |
+-----------+-----------------+--------+
9 rows in set (0.00 sec)



-- 17、查询“95031”班学生每门课的平均分。

select * from student where class='95031';
select sno from student where class='95031';


mysql> select * from score where sno in (select sno from student where class='95031');
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 105 | 3-105 |     88 |
| 105 | 3-245 |     75 |
| 105 | 6-166 |     79 |
| 109 | 3-105 |     76 |
| 109 | 3-245 |     68 |
| 109 | 6-166 |     81 |
+-----+-------+--------+
6 rows in set (0.00 sec)


select cno,avg(degree)
from score 
where sno in (select sno from student where class='95031') 
group by cno;

+-------+-------------+
| cno   | avg(degree) |
+-------+-------------+
| 3-105 |     82.0000 |
| 3-245 |     71.5000 |
| 6-166 |     80.0000 |
+-------+-------------+
3 rows in set (0.01 sec)


-- 18、查询选修“3-105”课程的成绩高于“109”号同学“3-105”成绩的所有同学的记录。

select degree from score where sno='109' and cno='3-105';

+--------+
| degree |
+--------+
|     76 |
+--------+
1 row in set (0.00 sec)


select * from score where cno='3-105' and degree>(select degree from score where sno='109' and cno='3-105');

+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 103 | 3-105 |     92 |
| 105 | 3-105 |     88 |
+-----+-------+--------+
2 rows in set (0.00 sec)


-- 19、查询成绩高于学号为“109”、课程号为“3-105”的成绩的所有记录。

select * from score where degree>(select degree from score where sno='109' and cno='3-105');

+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 103 | 3-105 |     92 |
| 103 | 3-245 |     86 |
| 103 | 6-166 |     85 |
| 105 | 3-105 |     88 |
| 105 | 6-166 |     79 |
| 109 | 6-166 |     81 |
+-----+-------+--------+
6 rows in set (0.00 sec)


-- 20、查询和学号为108、101的同学同年出生的所有学生的sno、sname和sbirthday列。

mysql> select * from student where sno in (108,101);
+-----+-----------+------+---------------------+-------+
| sno | sname     | ssex | sbirthday           | class |
+-----+-----------+------+---------------------+-------+
| 101 | 曾华      | 男   | 1977-09-01 00:00:00 | 95033 |
| 108 | 张全蛋    | 男   | 1975-02-10 00:00:00 | 95031 |
+-----+-----------+------+---------------------+-------+
2 rows in set (0.00 sec)

mysql> select year(sbirthday) from student where sno in (108,101);
+-----------------+
| year(sbirthday) |
+-----------------+
|            1977 |
|            1975 |
+-----------------+
2 rows in set (0.01 sec)


mysql> select * from student where year(sbirthday) in (select year(sbirthday) from student where sno in (108,101));
+-----+-----------+------+---------------------+-------+
| sno | sname     | ssex | sbirthday           | class |
+-----+-----------+------+---------------------+-------+
| 101 | 曾华      | 男   | 1977-09-01 00:00:00 | 95033 |
| 102 | 匡明      | 男   | 1975-10-02 00:00:00 | 95031 |
| 105 | 王芳      | 女   | 1975-02-10 00:00:00 | 95031 |
| 108 | 张全蛋    | 男   | 1975-02-10 00:00:00 | 95031 |
+-----+-----------+------+---------------------+-------+
4 rows in set (0.01 sec)



-- 21、查询“张旭“教师任课的学生成绩。


select tno from teacher where tname='张旭';

select cno from course where tno=(select tno from teacher where tname='张旭');

select * from score where cno=(select cno from course where tno=(select tno from teacher where tname='张旭'));

+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 103 | 6-166 |     85 |
| 105 | 6-166 |     79 |
| 109 | 6-166 |     81 |
+-----+-------+--------+
3 rows in set (0.00 sec)



-- 22、查询选修某课程的同学人数多于5人的教师姓名。

insert into score values('101','3-105','90');
insert into score values('102','3-105','91');
insert into score values('104','3-105','89');

insert into score values('103','3-105','92');
insert into score values('103','3-245','86');
insert into score values('103','6-166','85');
insert into score values('105','3-105','88');
insert into score values('105','3-245','75');
insert into score values('105','6-166','79');
insert into score values('109','3-105','76');
insert into score values('109','3-245','68');
insert into score values('109','6-166','81');


select cno from score group by cno having count(*)>5; 

select * from teacher;

select tno from course where cno=(select cno from score group by cno having count(*)>5);

select tname from teacher where tno=(select tno from course where cno=(select cno from score group by cno having count(*)>5));

+--------+
| tname  |
+--------+
| 王萍   |
+--------+
1 row in set (0.00 sec)


-- 23、查询95033班和95031班全体学生的记录。

insert into student values('110','张飞','男','1974-06-03','95038');

select * from student;

select * from student where class in ('95031','95033');
+-----+-----------+------+---------------------+-------+
| sno | sname     | ssex | sbirthday           | class |
+-----+-----------+------+---------------------+-------+
| 101 | 曾华      | 男   | 1977-09-01 00:00:00 | 95033 |
| 102 | 匡明      | 男   | 1975-10-02 00:00:00 | 95031 |
| 103 | 王丽      | 女   | 1976-01-23 00:00:00 | 95033 |
| 104 | 李军      | 男   | 1976-02-20 00:00:00 | 95033 |
| 105 | 王芳      | 女   | 1975-02-10 00:00:00 | 95031 |
| 106 | 陆君      | 男   | 1974-06-03 00:00:00 | 95031 |
| 107 | 王尼玛    | 男   | 1976-02-20 00:00:00 | 95033 |
| 108 | 张全蛋    | 男   | 1975-02-10 00:00:00 | 95031 |
| 109 | 赵铁柱    | 男   | 1974-06-03 00:00:00 | 95031 |
+-----+-----------+------+---------------------+-------+
9 rows in set (0.00 sec)



-- 24、查询存在有85分以上成绩的课程Cno.

select cno,degree from score where degree>85;

+-------+--------+
| cno   | degree |
+-------+--------+
| 3-105 |     90 |
| 3-105 |     91 |
| 3-105 |     92 |
| 3-245 |     86 |
| 3-105 |     89 |
| 3-105 |     88 |
+-------+--------+
6 rows in set (0.00 sec)



-- 25、查询出“计算机系“教师所教课程的成绩表。

select * from teacher where depart='计算机系';

+-----+--------+------+---------------------+-----------+--------------+
| tno | tname  | tsex | tbirthday           | prof      | depart       |
+-----+--------+------+---------------------+-----------+--------------+
| 804 | 李诚   | 男   | 1958-12-02 00:00:00 | 副教授    | 计算机系     |
| 825 | 王萍   | 女   | 1972-05-05 00:00:00 | 助教      | 计算机系     |
+-----+--------+------+---------------------+-----------+--------------+
2 rows in set (0.00 sec)


select * from course where tno in (select tno from teacher where depart='计算机系');

+-------+-----------------+-----+
| cno   | cname           | tno |
+-------+-----------------+-----+
| 3-245 | 操作系统        | 804 |
| 3-105 | 计算机导论      | 825 |
+-------+-----------------+-----+
2 rows in set (0.00 sec)


select * from score where cno in (select cno from course where tno in (select tno from teacher where depart='计算机系'));

+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 103 | 3-245 |     86 |
| 105 | 3-245 |     75 |
| 109 | 3-245 |     68 |
| 101 | 3-105 |     90 |
| 102 | 3-105 |     91 |
| 103 | 3-105 |     92 |
| 104 | 3-105 |     89 |
| 105 | 3-105 |     88 |
| 109 | 3-105 |     76 |
+-----+-------+--------+
9 rows in set (0.00 sec)



-- 26、查询“计算机系”与“电子工程系“不同职称的教师的tname和prof。
-- union 求并集

select prof from teacher where depart='电子工程系';

select * from teacher where depart='计算机系' and prof not in(select prof from teacher where depart='电子工程系')
union
select * from teacher where depart='电子工程系' and prof not in(select prof from teacher where depart='计算机系');

+-----+--------+------+---------------------+-----------+-----------------+
| tno | tname  | tsex | tbirthday           | prof      | depart          |
+-----+--------+------+---------------------+-----------+-----------------+
| 804 | 李诚   | 男   | 1958-12-02 00:00:00 | 副教授    | 计算机系        |
| 856 | 张旭   | 男   | 1969-03-12 00:00:00 | 讲师      | 电子工程系      |
+-----+--------+------+---------------------+-----------+-----------------+
2 rows in set (0.00 sec)



-- 27、查询选修编号为“3-105“课程且成绩至少高于选修编号为“3-245”的同学的Cno、Sno和Degree,
-- 	   并按Degree从高到低次序排序。

select * from score where cno='3-245';
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 103 | 3-245 |     86 |
| 105 | 3-245 |     75 |
| 109 | 3-245 |     68 |
+-----+-------+--------+
3 rows in set (0.00 sec)

select * from score where cno='3-105';
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 101 | 3-105 |     90 |
| 102 | 3-105 |     91 |
| 103 | 3-105 |     92 |
| 104 | 3-105 |     89 |
| 105 | 3-105 |     88 |
| 109 | 3-105 |     76 |
+-----+-------+--------+
6 rows in set (0.00 sec)

-- 至少？ 大于其中至少一个，any

select * from score 
where cno='3-105' 
and degree>any(select degree from score where cno='3-245')
order by degree desc;

+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 103 | 3-105 |     92 |
| 102 | 3-105 |     91 |
| 101 | 3-105 |     90 |
| 104 | 3-105 |     89 |
| 105 | 3-105 |     88 |
| 109 | 3-105 |     76 |
+-----+-------+--------+
6 rows in set (0.00 sec)


-- 28、查询选修编号为“3-105”且成绩高于选修编号为“3-245”课程的同学的Cno、Sno和Degree.

-- 且？ all 表示所有的关系

select * from score 
where cno='3-105' 
and degree>all(select degree from score where cno='3-245');

+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 101 | 3-105 |     90 |
| 102 | 3-105 |     91 |
| 103 | 3-105 |     92 |
| 104 | 3-105 |     89 |
| 105 | 3-105 |     88 |
+-----+-------+--------+
5 rows in set (0.00 sec)



-- 29、查询所有教师和同学的name、sex和birthday.

-- 别名？as

select tname as name,tsex as sex,tbirthday as birthday from teacher
union
select sname,ssex,sbirthday from student;

+-----------+-----+---------------------+
| name      | sex | birthday            |
+-----------+-----+---------------------+
| 李诚      | 男  | 1958-12-02 00:00:00 |
| 王萍      | 女  | 1972-05-05 00:00:00 |
| 刘冰      | 女  | 1977-08-14 00:00:00 |
| 张旭      | 男  | 1969-03-12 00:00:00 |
| 曾华      | 男  | 1977-09-01 00:00:00 |
| 匡明      | 男  | 1975-10-02 00:00:00 |
| 王丽      | 女  | 1976-01-23 00:00:00 |
| 李军      | 男  | 1976-02-20 00:00:00 |
| 王芳      | 女  | 1975-02-10 00:00:00 |
| 陆君      | 男  | 1974-06-03 00:00:00 |
| 王尼玛    | 男  | 1976-02-20 00:00:00 |
| 张全蛋    | 男  | 1975-02-10 00:00:00 |
| 赵铁柱    | 男  | 1974-06-03 00:00:00 |
| 张飞      | 男  | 1974-06-03 00:00:00 |
+-----------+-----+---------------------+
14 rows in set (0.00 sec)



-- 30、查询所有“女”教师和“女”同学的name、sex和birthday.


select tname as name,tsex as sex,tbirthday as birthday from teacher where tsex='女'
union
select sname,ssex,sbirthday from student where ssex='女';


+--------+-----+---------------------+
| name   | sex | birthday            |
+--------+-----+---------------------+
| 王萍   | 女  | 1972-05-05 00:00:00 |
| 刘冰   | 女  | 1977-08-14 00:00:00 |
| 王丽   | 女  | 1976-01-23 00:00:00 |
| 王芳   | 女  | 1975-02-10 00:00:00 |
+--------+-----+---------------------+
4 rows in set (0.00 sec)



-- 31、查询成绩比该课程平均成绩低的同学的成绩表。


select cno,avg(degree) from score group by cno;

+-------+-------------+
| cno   | avg(degree) |
+-------+-------------+
| 3-105 |     87.6667 |
| 3-245 |     76.3333 |
| 6-166 |     77.3333 |
+-------+-------------+
3 rows in set (0.00 sec)


select * from score;
a 								b
+-----+-------+--------+		+-----+-------+--------+
| sno | cno   | degree |		| sno | cno   | degree |
+-----+-------+--------+		+-----+-------+--------+
| 101 | 3-105 |     90 |		| 101 | 3-105 |     90 |
| 102 | 3-105 |     91 |		| 102 | 3-105 |     91 |
| 103 | 3-105 |     92 |		| 103 | 3-105 |     92 |
| 103 | 3-245 |     86 |		| 103 | 3-245 |     86 |
| 103 | 6-166 |     85 |		| 103 | 6-166 |     85 |
| 104 | 3-105 |     89 |		| 104 | 3-105 |     89 |
| 105 | 3-105 |     88 |		| 105 | 3-105 |     88 |
| 105 | 3-245 |     75 |		| 105 | 3-245 |     75 |
| 105 | 6-166 |     79 |		| 105 | 6-166 |     79 |
| 109 | 3-105 |     76 |		| 109 | 3-105 |     76 |
| 109 | 3-245 |     68 |		| 109 | 3-245 |     68 |
| 109 | 6-166 |     68 |		| 109 | 6-166 |     68 |
+-----+-------+--------+		+-----+-------+--------+
12 rows in set (0.00 sec)		12 rows in set (0.00 sec)


select * from score a where degree < (select avg(degree) from score b where a.cno=b.cno);
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 105 | 3-245 |     75 |
| 109 | 3-105 |     76 |
| 109 | 3-245 |     68 |
| 109 | 6-166 |     68 |
+-----+-------+--------+
4 rows in set (0.00 sec)


-- 32、查询所有任课教师的Tname和Depart.

-- 课程表中安排了课程
select * from course;
+-------+-----------------+-----+
| cno   | cname           | tno |
+-------+-----------------+-----+
| 3-105 | 计算机导论      | 825 |
| 3-245 | 操作系统        | 804 |
| 6-166 | 数字电路        | 856 |
| 9-888 | 高等数学        | 831 |
+-------+-----------------+-----+
4 rows in set (0.00 sec)


select tname,depart from teacher where tno in (select tno from course);
+--------+-----------------+
| tname  | depart          |
+--------+-----------------+
| 李诚   | 计算机系        |
| 王萍   | 计算机系        |
| 刘冰   | 电子工程系      |
| 张旭   | 电子工程系      |
+--------+-----------------+
4 rows in set (0.00 sec)



-- 33、查询至少有2名男生的班号。

select * from student;
+-----+-----------+------+---------------------+-------+
| sno | sname     | ssex | sbirthday           | class |
+-----+-----------+------+---------------------+-------+
| 101 | 曾华      | 男   | 1977-09-01 00:00:00 | 95033 |
| 102 | 匡明      | 男   | 1975-10-02 00:00:00 | 95031 |
| 103 | 王丽      | 女   | 1976-01-23 00:00:00 | 95033 |
| 104 | 李军      | 男   | 1976-02-20 00:00:00 | 95033 |
| 105 | 王芳      | 女   | 1975-02-10 00:00:00 | 95031 |
| 106 | 陆君      | 男   | 1974-06-03 00:00:00 | 95031 |
| 107 | 王尼玛    | 男   | 1976-02-20 00:00:00 | 95033 |
| 108 | 张全蛋    | 男   | 1975-02-10 00:00:00 | 95031 |
| 109 | 赵铁柱    | 男   | 1974-06-03 00:00:00 | 95031 |
| 110 | 张飞      | 男   | 1974-06-03 00:00:00 | 95038 |
+-----+-----------+------+---------------------+-------+
10 rows in set (0.00 sec)


select class from student where ssex='男' group by class having count(*)>1;
+-------+
| class |
+-------+
| 95033 |
| 95031 |
+-------+
2 rows in set (0.00 sec)



-- 34、查询student表中不姓“王”的同学记录。

select * from student;

select * from student where sname not like '王%';
+-----+-----------+------+---------------------+-------+
| sno | sname     | ssex | sbirthday           | class |
+-----+-----------+------+---------------------+-------+
| 101 | 曾华      | 男   | 1977-09-01 00:00:00 | 95033 |
| 102 | 匡明      | 男   | 1975-10-02 00:00:00 | 95031 |
| 104 | 李军      | 男   | 1976-02-20 00:00:00 | 95033 |
| 106 | 陆君      | 男   | 1974-06-03 00:00:00 | 95031 |
| 108 | 张全蛋    | 男   | 1975-02-10 00:00:00 | 95031 |
| 109 | 赵铁柱    | 男   | 1974-06-03 00:00:00 | 95031 |
| 110 | 张飞      | 男   | 1974-06-03 00:00:00 | 95038 |
+-----+-----------+------+---------------------+-------+
7 rows in set (0.00 sec)



-- 35、查询student表中每个学生的姓名和年龄。

-- 年龄=当前年份-出生年份
select year(now());
+-------------+
| year(now()) |
+-------------+
|        2018 |
+-------------+
1 row in set (0.01 sec)


select year(sbirthday) from student;
+-----------------+
| year(sbirthday) |
+-----------------+
|            1977 |
|            1975 |
|            1976 |
|            1976 |
|            1975 |
|            1974 |
|            1976 |
|            1975 |
|            1974 |
|            1974 |
+-----------------+
10 rows in set (0.00 sec)


select sname,year(now())-year(sbirthday) as '年龄' from student;
+-----------+--------+
| sname     | 年龄   |
+-----------+--------+
| 曾华      |     41 |
| 匡明      |     43 |
| 王丽      |     42 |
| 李军      |     42 |
| 王芳      |     43 |
| 陆君      |     44 |
| 王尼玛    |     42 |
| 张全蛋    |     43 |
| 赵铁柱    |     44 |
| 张飞      |     44 |
+-----------+--------+
10 rows in set (0.01 sec)



-- 36、查询student表中最大和最小的sbirthday日期值。

select sbirthday from student order by sbirthday;


-- max min
select max(sbirthday) as '最大',min(sbirthday) as '最小' from student;
+---------------------+---------------------+
| 最大                | 最小                |
+---------------------+---------------------+
| 1977-09-01 00:00:00 | 1974-06-03 00:00:00 |
+---------------------+---------------------+
1 row in set (0.00 sec)



-- 37、以班号和年龄从大到小的顺序查询student表中的全部记录。


select * from student order by class desc,sbirthday;
+-----+-----------+------+---------------------+-------+
| sno | sname     | ssex | sbirthday           | class |
+-----+-----------+------+---------------------+-------+
| 110 | 张飞      | 男   | 1974-06-03 00:00:00 | 95038 |
| 103 | 王丽      | 女   | 1976-01-23 00:00:00 | 95033 |
| 104 | 李军      | 男   | 1976-02-20 00:00:00 | 95033 |
| 107 | 王尼玛    | 男   | 1976-02-20 00:00:00 | 95033 |
| 101 | 曾华      | 男   | 1977-09-01 00:00:00 | 95033 |
| 106 | 陆君      | 男   | 1974-06-03 00:00:00 | 95031 |
| 109 | 赵铁柱    | 男   | 1974-06-03 00:00:00 | 95031 |
| 105 | 王芳      | 女   | 1975-02-10 00:00:00 | 95031 |
| 108 | 张全蛋    | 男   | 1975-02-10 00:00:00 | 95031 |
| 102 | 匡明      | 男   | 1975-10-02 00:00:00 | 95031 |
+-----+-----------+------+---------------------+-------+
10 rows in set (0.00 sec)



-- 38、查询“男”教师及其所上的课程。

select * from teacher where tsex='男';

+-----+--------+------+---------------------+-----------+-----------------+
| tno | tname  | tsex | tbirthday           | prof      | depart          |
+-----+--------+------+---------------------+-----------+-----------------+
| 804 | 李诚   | 男   | 1958-12-02 00:00:00 | 副教授    | 计算机系        |
| 856 | 张旭   | 男   | 1969-03-12 00:00:00 | 讲师      | 电子工程系      |
+-----+--------+------+---------------------+-----------+-----------------+
2 rows in set (0.01 sec)


select * from course where tno in (select tno from teacher where tsex='男');
+-------+--------------+-----+
| cno   | cname        | tno |
+-------+--------------+-----+
| 3-245 | 操作系统     | 804 |
| 6-166 | 数字电路     | 856 |
+-------+--------------+-----+
2 rows in set (0.00 sec)


-- 39、查询最高分同学的sno、cno和degree列。

select max(degree) from score;
+-------------+
| max(degree) |
+-------------+
|          92 |
+-------------+
1 row in set (0.00 sec)


select * from score where degree=(select max(degree) from score);
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 103 | 3-105 |     92 |
+-----+-------+--------+
1 row in set (0.00 sec)


-- 40、查询和“李军”同性别的所有同学的Sname.


select ssex from student where sname='李军';
+------+
| ssex |
+------+
| 男   |
+------+
1 row in set (0.00 sec)


select sname from student where ssex=(select ssex from student where sname='李军');
+-----------+
| sname     |
+-----------+
| 曾华      |
| 匡明      |
| 李军      |
| 陆君      |
| 王尼玛    |
| 张全蛋    |
| 赵铁柱    |
| 张飞      |
+-----------+
8 rows in set (0.00 sec)



-- 41、查询和“李军”同性别并同班的同学Sname.


select sname from student 
where ssex=(select ssex from student where sname='李军')
and class=(select class from student where sname='李军');

+-----------+
| sname     |
+-----------+
| 曾华      |
| 李军      |
| 王尼玛    |
+-----------+
3 rows in set (0.00 sec)



-- 42、查询所有选修“计算机导论”课程的“男”同学的成绩表。

select * from student where ssex='男';

+-----+-----------+------+---------------------+-------+
| sno | sname     | ssex | sbirthday           | class |
+-----+-----------+------+---------------------+-------+
| 101 | 曾华      | 男   | 1977-09-01 00:00:00 | 95033 |
| 102 | 匡明      | 男   | 1975-10-02 00:00:00 | 95031 |
| 104 | 李军      | 男   | 1976-02-20 00:00:00 | 95033 |
| 106 | 陆君      | 男   | 1974-06-03 00:00:00 | 95031 |
| 107 | 王尼玛    | 男   | 1976-02-20 00:00:00 | 95033 |
| 108 | 张全蛋    | 男   | 1975-02-10 00:00:00 | 95031 |
| 109 | 赵铁柱    | 男   | 1974-06-03 00:00:00 | 95031 |
| 110 | 张飞      | 男   | 1974-06-03 00:00:00 | 95038 |
+-----+-----------+------+---------------------+-------+
8 rows in set (0.00 sec)


select * from course where cname='计算机导论';
+-------+-----------------+-----+
| cno   | cname           | tno |
+-------+-----------------+-----+
| 3-105 | 计算机导论      | 825 |
+-------+-----------------+-----+
1 row in set (0.00 sec)

select * from score 
where cno=(select cno from course where cname='计算机导论')
and sno in (select sno from student where ssex='男');
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 101 | 3-105 |     90 |
| 102 | 3-105 |     91 |
| 104 | 3-105 |     89 |
| 109 | 3-105 |     76 |
+-----+-------+--------+
4 rows in set (0.00 sec)



-- 43、假设使用如下命令建立了一个grade表：

create table grade(
	low int(3),
	upp int(3),
	grade char(1)
);

insert into grade values(90,100,'A');
insert into grade values(80,89,'B');
insert into grade values(70,79,'C');
insert into grade values(60,69,'D');
insert into grade values(0,59,'E');

-- 现查询所有同学的sno、cno 和 grade 列。

select sno,cno,grade from score,grade where degree between low and upp;

+-----+-------+-------+
| sno | cno   | grade |
+-----+-------+-------+
| 101 | 3-105 | A     |
| 102 | 3-105 | A     |
| 103 | 3-105 | A     |
| 103 | 3-245 | B     |
| 103 | 6-166 | B     |
| 104 | 3-105 | B     |
| 105 | 3-105 | B     |
| 105 | 3-245 | C     |
| 105 | 6-166 | C     |
| 109 | 3-105 | C     |
| 109 | 3-245 | D     |
| 109 | 6-166 | D     |
+-----+-------+-------+
12 rows in set (0.00 sec)


















