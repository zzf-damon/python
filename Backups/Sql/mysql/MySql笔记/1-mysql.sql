
-- mysql 学习笔记

-- 关系型数据库

-- 一、如何使用终端操作数据库？

-- 1. 如何登陆数据库服务器？
mac:~ zhengbing$ mysql -uroot -p123456


-- 2. 如何查询数据库服务器中所有的数据库？
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| company            |
| information_schema |
| mysql              |
| performance_schema |
| sushe              |
| sys                |
+--------------------+
6 rows in set (0.00 sec)

-- 3. 如何选中某一个数据库进行操作？
mysql> select * from admin;
ERROR 1046 (3D000): No database selected

mysql> use sushe
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed

-- SQL 语句中的查询
mysql> select * from admin;
+----------+----------------+----------------+------------+-----------+-----------+
| Admin_ID | Admin_Username | Admin_Password | Admin_Name | Admin_Sex | Admin_Tel |
+----------+----------------+----------------+------------+-----------+-----------+
|        1 | admin          | 123            | admin      |           | null      |
|        2 | root           | 123            | root       | NULL      | NULL      |
|        3 | zhangsan       | 123            | zhangsan   | NULL      | NULL      |
+----------+----------------+----------------+------------+-----------+-----------+
3 rows in set (0.00 sec)


mysql> select * from admin where Admin_ID=1;
+----------+----------------+----------------+------------+-----------+-----------+
| Admin_ID | Admin_Username | Admin_Password | Admin_Name | Admin_Sex | Admin_Tel |
+----------+----------------+----------------+------------+-----------+-----------+
|        1 | admin          | 123            | admin      |           | null      |
+----------+----------------+----------------+------------+-----------+-----------+
1 row in set (0.00 sec)


-- 如何退出数据库服务器？
mysql> exit;
Bye


-- 如何在数据库服务器中创建我们的数据库？
mysql> create database test;
Query OK, 1 row affected (0.07 sec)


mysql> use test;
Database changed

-- 如何查看某个数据库中所有的数据表？
mysql> show tablse;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'tablse' at line 1
mysql> show tables;
Empty set (0.01 sec)

-- 如何创建一个数据表？
CREATE TABLE pet (
	name VARCHAR(20),
	owner VARCHAR(20),
	species VARCHAR(20),
	sex CHAR(1), 
	birth DATE, 
	death DATE);

mysql> CREATE TABLE pet (
    -> name VARCHAR(20),
    -> owner VARCHAR(20),
    -> species VARCHAR(20),
    -> sex CHAR(1), 
    -> birth DATE, 
    -> death DATE);
Query OK, 0 rows affected (0.14 sec)

-- 查看数据表是否创建成功
mysql> show tables;
+----------------+
| Tables_in_test |
+----------------+
| pet            |
+----------------+
1 row in set (0.01 sec)


-- 查看创建好的数据表的结构
mysql> describe pet;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| name    | varchar(20) | YES  |     | NULL    |       |
| owner   | varchar(20) | YES  |     | NULL    |       |
| species | varchar(20) | YES  |     | NULL    |       |
| sex     | char(1)     | YES  |     | NULL    |       |
| birth   | date        | YES  |     | NULL    |       |
| death   | date        | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+
6 rows in set (0.02 sec)


-- 如何查看数据表中的记录？
mysql> select * from pet;
Empty set (0.00 sec)


-- 如何往数据表中添加数据记录呢？
mysql> INSERT INTO pet
    -> VALUES ('Puffball','Diane','hamster','f','1999-03-30',NULL);
Query OK, 1 row affected (0.03 sec)

-- 再一次查询？
mysql> select * from pet;
+----------+-------+---------+------+------------+-------+
| name     | owner | species | sex  | birth      | death |
+----------+-------+---------+------+------------+-------+
| Puffball | Diane | hamster | f    | 1999-03-30 | NULL  |
+----------+-------+---------+------+------------+-------+
1 row in set (0.00 sec)

INSERT INTO pet
VALUES('旺财','周星驰','狗','公','1990-01-01',NULL);

mysql> INSERT INTO pet
    -> VALUES('旺财','周星驰','狗','公',1990-01-01,NULL);
ERROR 1292 (22007): Incorrect date value: '1988' for column 'birth' at row 1

mysql> INSERT INTO pet
    -> VALUES('旺财','周星驰','狗','公','1990-01-01',NULL);
Query OK, 1 row affected (0.15 sec)


mysql> select * from pet;
+----------+-----------+---------+------+------------+-------+
| name     | owner     | species | sex  | birth      | death |
+----------+-----------+---------+------+------------+-------+
| Puffball | Diane     | hamster | f    | 1999-03-30 | NULL  |
| 旺财     | 周星驰    | 狗      | 公   | 1990-01-01 | NULL  |
+----------+-----------+---------+------+------------+-------+
2 rows in set (0.00 sec)


-- mysql 常用数据类型有哪些？

-- MySQL支持多种类型，大致可以分为三类：

create tables testType(
	number TINYINT
);

INSERT INTO testType VALUES(127);

mysql> INSERT INTO testType VALUES(128);
ERROR 1264 (22003): Out of range value for column 'number' at row 1

-- 数值
类型	大小	范围（有符号）	范围（无符号）	用途
TINYINT		1 字节	(-128，127)	(0，255)	小整数值
SMALLINT	2 字节	(-32 768，32 767)	(0，65 535)	大整数值
MEDIUMINT	3 字节	(-8 388 608，8 388 607)	(0，16 777 215)	大整数值
INT或INTEGER	4 字节	(-2 147 483 648，2 147 483 647)	(0，4 294 967 295)	大整数值
BIGINT		8 字节	(-9 233 372 036 854 775 808，9 223 372 036 854 775 807)	(0，18 446 744 073 709 551 615)	极大整数值
FLOAT		4 字节	(-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38)	0，(1.175 494 351 E-38，3.402 823 466 E+38)	单精度
浮点数值
DOUBLE		8 字节	(-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308)	0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308)	双精度
浮点数值
DECIMAL	对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2	依赖于M和D的值	依赖于M和D的值	小数值

-- 日期/时间
类型	大小
(字节)	范围	格式	用途
DATE	3	1000-01-01/9999-12-31	YYYY-MM-DD	日期值
TIME	3	'-838:59:59'/'838:59:59'	HH:MM:SS	时间值或持续时间
YEAR	1	1901/2155	YYYY	年份值
DATETIME	8	1000-01-01 00:00:00/9999-12-31 23:59:59	YYYY-MM-DD HH:MM:SS	混合日期和时间值
TIMESTAMP	4	
1970-01-01 00:00:00/2038
结束时间是第 2147483647 秒，北京时间 2038-1-19 11:14:07，格林尼治时间 2038年1月19日 凌晨 03:14:07
YYYYMMDD HHMMSS	混合日期和时间值，时间戳

-- 和字符串(字符)类型
类型	大小	用途
CHAR	0-255字节	定长字符串
VARCHAR	0-65535 字节	变长字符串
TINYBLOB	0-255字节	不超过 255 个字符的二进制字符串
TINYTEXT	0-255字节	短文本字符串
BLOB	0-65 535字节	二进制形式的长文本数据
TEXT	0-65 535字节	长文本数据
MEDIUMBLOB	0-16 777 215字节	二进制形式的中等长度文本数据
MEDIUMTEXT	0-16 777 215字节	中等长度文本数据
LONGBLOB	0-4 294 967 295字节	二进制形式的极大文本数据
LONGTEXT	0-4 294 967 295字节	极大文本数据


-- 数据类型如何选择？
日期 选择按照格式
数值和字符串按照大小！



-- 如何插入以下数据到数据表？
+----------+--------+---------+------+------------+------------+
| name     | owner  | species | sex  | birth      | death      |
+----------+--------+---------+------+------------+------------+
| Fluffy   | Harold | cat     | f    | 1993-02-04 | NULL       |
| Claws    | Gwen   | cat     | m    | 1994-03-17 | NULL       |
| Buffy    | Harold | dog     | f    | 1989-05-13 | NULL       |
| Fang     | Benny  | dog     | m    | 1990-08-27 | NULL       |
| Bowser   | Diane  | dog     | m    | 1979-08-31 | 1995-07-29 |
| Chirpy   | Gwen   | bird    | f    | 1998-09-11 | NULL       |
| Whistler | Gwen   | bird    | NULL | 1997-12-09 | NULL       |
| Slim     | Benny  | snake   | m    | 1996-04-29 | NULL       |
| Puffball | Diane  | hamster | f    | 1999-03-30 | NULL       |
+----------+--------+---------+------+------------+------------+


INSERT INTO pet VALUES('Fluffy','Harold','cat','f','1993-02-04',NULL);
INSERT INTO pet VALUES('Claws','Gwen','cat','m','1994-03-17',NULL);
INSERT INTO pet VALUES('Buffy','Harold','dog','f','1989-05-13',NULL);
INSERT INTO pet VALUES('Fang','Benny','dog','m','1990-08-27',NULL);
INSERT INTO pet VALUES('Bowser','Diane','dog','m','1979-08-31','1995-07-29');
INSERT INTO pet VALUES('Chirpy','Gwen','bird','f','1998-09-11',NULL);
INSERT INTO pet VALUES('Whistler','Gwen','bird',NULL,'1997-12-09',NULL);
INSERT INTO pet VALUES('Slim','Benny','snake','m','1996-04-29',NULL);
INSERT INTO pet VALUES('Puffball','Diane','hamster','f','1999-03-30',NULL);


-- 如何删除数据？

delete from pet where name='Fluffy';

mysql> delete from pet where name='Fluffy';
Query OK, 2 rows affected (0.01 sec)

-- 如何修改数据？
update pet set name='旺旺财' where owner='周星驰';

mysql> update set name='旺旺财' where owner='周星驰';
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'set name='旺旺财' where owner='周星驰'' at line 1

mysql> update pet set name='旺旺财' where owner='周星驰';
Query OK, 1 row affected (0.04 sec)
Rows matched: 1  Changed: 1  Warnings: 0


-- 总结一下：数据记录常见操作？

-- 增加
INSERT
-- 删除
DELETE
-- 修改
UPDATE
-- 查询
SELECT

-- pet.txt
-- 登录的时候加参数
mac:~ zhengbing$ mysql --local-infile=1 -uroot -p123456


mysql> LOAD DATA LOCAL INFILE '/Users/zhengbing/Desktop/pet.txt' INTO TABLE pet; 
ERROR 1148 (42000): The used command is not allowed with this MySQL version

-- 查询 local_infile 的值
mysql> show variables like 'local_infile';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| local_infile  | OFF   |
+---------------+-------+
1 row in set (0.04 sec)

-- 打开
mysql> set global local_infile=ON;
Query OK, 0 rows affected (0.00 sec)

mysql> show variables like 'local_infile';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| local_infile  | ON    |
+---------------+-------+
1 row in set (0.00 sec)

-- 加载数据 from pet.txt
mysql> LOAD DATA LOCAL INFILE '/Users/zhengbing/Desktop/pet.txt' INTO TABLE pet; 
Query OK, 8 rows affected (0.08 sec)
Records: 8  Deleted: 0  Skipped: 0  Warnings: 0





-- 二、如何使用可视化工具操作数据库？



-- 三、如何在编程语言中操作数据库？
