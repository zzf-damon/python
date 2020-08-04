-- mysql建表约束.sql


-- 主键约束

它能够唯一确定一张表中的一条记录，也就是我们通过给某个字段添加约束，就可以使得改字段
不重复且不为空。

create table user(
	id int primary key,
	name varchar(20)
);

insert into user values(1,'张三');


mysql> insert into user values(1,'张三');
Query OK, 1 row affected (0.17 sec)


mysql> insert into user values(1,'张三');
ERROR 1062 (23000): Duplicate entry '1' for key 'PRIMARY'

insert into user values(2,'张三');

mysql> select * from user;
+----+--------+
| id | name   |
+----+--------+
|  1 | 张三   |
|  2 | 张三   |
+----+--------+

mysql> insert into user values(NULL,'张三');
ERROR 1048 (23000): Column 'id' cannot be null


-- 联合主键
-- 只要联合的主键值加起来不重复就可以
create table user2(
	id int,
	name varchar(20),
	password varchar(20),
	primary key(id,name)
);

insert into user2 values(1,'张三','123');
insert into user2 values(2,'张三','123');
insert into user2 values(1,'李四','123');


insert into user2 values(NULL,'李四','123');



-- 自增约束
-- auto_increment

create table user3(
	id int primary key auto_increment,
	name varchar(20)
);

insert into user3 (name) values('zhangsan');

mysql> insert into user3 (name) values('zhangsan');
Query OK, 1 row affected (0.14 sec)

mysql> select * from user3;
+----+----------+
| id | name     |
+----+----------+
|  1 | zhangsan |
+----+----------+
1 row in set (0.00 sec)


mysql> insert into user3 (name) values('zhangsan');
Query OK, 1 row affected (0.06 sec)

mysql> 
mysql> 
mysql> select * from user3;
+----+----------+
| id | name     |
+----+----------+
|  1 | zhangsan |
|  2 | zhangsan |
+----+----------+
2 rows in set (0.00 sec)


-- 如果说我们创建表的时候，忘记创建主键约束了？改怎么办？

create table user4(
	id int,
	name varchar(20)
);


mysql> desc user4;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | YES  |     | NULL    |       |
| name  | varchar(20) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)


-- 修改表结构，添加主键
alter table user4 add primary key(id);

mysql> desc user4;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | NO   | PRI | NULL    |       |
| name  | varchar(20) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)

-- 如何删除？
alter table user4 drop primary key;

mysql> alter table user4 drop primary key;
Query OK, 0 rows affected (0.17 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc user4;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | NO   |     | NULL    |       |
| name  | varchar(20) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)


-- 使用 modify 修改字段，添加约束
alter table user4 modify id int primary key;

mysql> alter table user4 modify id int primary key;
Query OK, 0 rows affected (0.17 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> 
mysql> desc user4;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | NO   | PRI | NULL    |       |
| name  | varchar(20) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)



-- 唯一约束
-- 约束修饰的字段的值不可以重复

create table user5(
	id int,
	name varchar(20)
);

mysql> alter table user5 add unique(name);
Query OK, 0 rows affected (0.16 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> 
mysql> 
mysql> desc user5;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | YES  |     | NULL    |       |
| name  | varchar(20) | YES  | UNI | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)

insert into user5 values(1,'zhangsan');

mysql> insert into user5 values(1,'zhangsan');
Query OK, 1 row affected (0.16 sec)

mysql> insert into user5 values(1,'zhangsan');
ERROR 1062 (23000): Duplicate entry 'zhangsan' for key 'name'

-- name = lisi
mysql> insert into user5 values(1,'lisi');
Query OK, 1 row affected (0.17 sec)



create table user6(
	id int,
	name varchar(20),
	unique(name)
);


create table user7(
	id int,
	name varchar(20) unique
);

create table user8(
	id int,
	name varchar(20),
	unique(id,name)
);

-- unique(id,name) 表示两个键在一起不重复就行
mysql> create table user8(
    -> id int,
    -> name varchar(20),
    -> unique(id,name)
    -> );
Query OK, 0 rows affected (0.05 sec)
 
mysql> desc user8;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | YES  | MUL | NULL    |       |
| name  | varchar(20) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.01 sec)

insert into user8 values(1,'zhangsan');
insert into user8 values(2,'zhangsan');
insert into user8 values(1,'lisi');

mysql> select * from user8;
+------+----------+
| id   | name     |
+------+----------+
|    1 | lisi     |
|    1 | zhangsan |
|    2 | zhangsan |
+------+----------+


-- 如何删除唯一约束？
alter table user7 drop index name;

mysql> alter table user7 drop index name;
Query OK, 0 rows affected (0.14 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc user7;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | YES  |     | NULL    |       |
| name  | varchar(20) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)

-- modify 添加？

alter table user7 modify name varchar(20) unique;

mysql> alter table user7 modify name varchar(20) unique;
Query OK, 0 rows affected (0.17 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc user7;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | YES  |     | NULL    |       |
| name  | varchar(20) | YES  | UNI | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)


-- 总结：
-- 1、建表的时候就添加约束
-- 2、可以使用 alter 。。。 add 。。。。
-- 3、alter 。。。 modif 。。。

-- 4、删除 alter 。。。。 drop 。。。



-- 非空约束 not null
-- 修饰的字段不能为空 NULL

create table user9(
id int,
name varchar(20) not null
);

mysql> create table user9(
    -> id int,
    -> name varchar(20) not null
    -> );
Query OK, 0 rows affected (0.15 sec)

mysql> desc user9;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | YES  |     | NULL    |       |
| name  | varchar(20) | NO   |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)


insert into user9 (id) values(1);

mysql> insert into user9 (id) values(1);
-- ERROR 1364 (HY000): Field 'name' doesn't have a default value

insert into user9 values(1,'张三');
mysql> select * from user9;
+------+--------+
| id   | name   |
+------+--------+
|    1 | 张三   |
+------+--------+
1 row in set (0.00 sec)

insert into user9 (name) values('lisi');
mysql> select * from user9;
+------+--------+
| id   | name   |
+------+--------+
|    1 | 张三   |
| NULL | lisi   |
+------+--------+
2 rows in set (0.00 sec)


-- 默认约束
-- 就是当我们插入字段值的时候，如果没有传值，就会使用默认值

create table user10(
	id int,
	name varchar(20),
	age int default 10
);


mysql> create table user10(
    -> id int,
    -> name varchar(20),
    -> age int default 10
    -> );

Query OK, 0 rows affected (0.16 sec)

mysql> desc user10;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | YES  |     | NULL    |       |
| name  | varchar(20) | YES  |     | NULL    |       |
| age   | int(11)     | YES  |     | 10      |       |
+-------+-------------+------+-----+---------+-------+
3 rows in set (0.01 sec)


insert into user10 (id, name) values(1,'zhangsan');
mysql> insert into user10 (id, name) values(1,'zhangsan');
Query OK, 1 row affected (0.09 sec)

mysql> 
mysql> select * from user10;
+------+----------+------+
| id   | name     | age  |
+------+----------+------+
|    1 | zhangsan |   10 |
+------+----------+------+
1 row in set (0.00 sec)

-- 传了值，就不会使用默认值
mysql> insert into user10 values(1,'zhangsan', 19);
Query OK, 1 row affected (0.01 sec)

mysql> 
mysql> select * from user10;
+------+----------+------+
| id   | name     | age  |
+------+----------+------+
|    1 | zhangsan |   10 |
|    1 | zhangsan |   19 |
+------+----------+------+
2 rows in set (0.00 sec)


-- 外键约束
-- 涉及到两个表：父表，子表
-- 主表，副表。

-- 班级
create table classes(
	id int primary key,
	name varchar(20)
);


-- 学生表
create table students(
	id int primary key,
	name varchar(20),
	class_id int,
	foreign key(class_id) references classes(id)
);


insert into students values(1001,'张三',1);
insert into students values(1002,'张三',2);
insert into students values(1003,'张三',3);
insert into students values(1004,'张三',4);

insert into students values(1005,'lisi',5);

mysql> insert into students values(1005,'lisi',5);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`test`.`students`, CONSTRAINT `students_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `classes` (`id`))

insert into classes values(1,'一班');
insert into classes values(2,'二班');
insert into classes values(3,'三班');
insert into classes values(4,'四班');

mysql> select * from classes;
+----+--------+
| id | name   |
+----+--------+
|  1 | 一班   |
|  2 | 二班   |
|  3 | 三班   |
|  4 | 四班   |
+----+--------+
4 rows in set (0.01 sec)


-- 1 主表(父表) classes 中没有的数据值，在副表（子表）中，是不可以使用的。
-- 2 主表中的记录被副表引用，是不可以被删除的。

delete from classes where id=4;
mysql> delete from classes where id=4;
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`test`.`students`, CONSTRAINT `students_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `classes` (`id`))






















