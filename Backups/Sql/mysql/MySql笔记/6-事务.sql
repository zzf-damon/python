
-- mysql事务


mysql 中，事务其实是一个最小的不可分割的工作单元。事务能够保证一个业务的完整性。

比如我们的银行转账：
	
	a -> -100
	update user set money=money-100 where name='a';

	b -> +100
	update user set money=money+100 where name='b';

-- 实际的程序中，如果只有一条语句执行成功了，而另外一条没有执行成功？
-- 出现数据前后不一致。

	update user set money=money-100 where name='a';
	update user set money=money+100 where name='b';

-- 多条sql 语句，可能会有同时成功的要求，要么就同时失败。


-- mysql 中如何控制事务？

1、mysql 默认是开启事务的(自动提交)。 

mysql> select @@autocommit;
+--------------+
| @@autocommit |
+--------------+
|            1 |
+--------------+
1 row in set (0.00 sec)

-- 默认事务开启的作用是什么？
-- 当我们去执行一个sql 语句的时候，效果会立即体现出来，且不能回滚。

create database bank;

create table user(
	id int primary key,
	name varchar(20),
	money int
);

insert into user values(1,'a',1000);

-- 事务回滚：撤销sql语句执行效果
rollback;

mysql> rollback;
Query OK, 0 rows affected (0.00 sec)

mysql> select * from user;
+----+------+-------+
| id | name | money |
+----+------+-------+
|  1 | a    |  1000 |
+----+------+-------+
1 row in set (0.00 sec)


-- 设置 mysql 自动提交为 false

set autocommit=0;

mysql> set autocommit=0;
Query OK, 0 rows affected (0.00 sec)

mysql> select @@autocommit;
+--------------+
| @@autocommit |
+--------------+
|            0 |
+--------------+
1 row in set (0.00 sec)

-- 上面的操作，关闭了 mysql 的自动提交（commit）

insert into user values(2,'b',1000);

mysql> insert into user values(2,'b',1000);
Query OK, 1 row affected (0.00 sec)

mysql> select * from user;
+----+------+-------+
| id | name | money |
+----+------+-------+
|  1 | a    |  1000 |
|  2 | b    |  1000 |
+----+------+-------+
2 rows in set (0.00 sec)

mysql> rollback;
Query OK, 0 rows affected (0.11 sec)

mysql> select * from user;
+----+------+-------+
| id | name | money |
+----+------+-------+
|  1 | a    |  1000 |
+----+------+-------+
1 row in set (0.00 sec)

-- 再一次插入数据
mysql> insert into user values(2,'b',1000);
Query OK, 1 row affected (0.00 sec)

-- 手动提交数据
mysql> commit;
Query OK, 0 rows affected (0.06 sec)

-- 再撤销，是不可以撤销的（持久性）
mysql> rollback;
Query OK, 0 rows affected (0.00 sec)

mysql> select * from user;
+----+------+-------+
| id | name | money |
+----+------+-------+
|  1 | a    |  1000 |
|  2 | b    |  1000 |
+----+------+-------+
2 rows in set (0.00 sec)

-- 自动提交？@@autocommit=1   取消=0；

-- 手动提交？commit;

-- 事务回滚？rollback;

-- 如果说这个时候转账：

update user set money=money-100 where name='a';
update user set money=money+100 where name='b';


mysql> select * from user;
+----+------+-------+
| id | name | money |
+----+------+-------+
|  1 | a    |   900 |
|  2 | b    |  1100 |
+----+------+-------+
2 rows in set (0.00 sec)

mysql> rollback;
Query OK, 0 rows affected (0.15 sec)

mysql> select * from user;
+----+------+-------+
| id | name | money |
+----+------+-------+
|  1 | a    |  1000 |
|  2 | b    |  1000 |
+----+------+-------+
2 rows in set (0.00 sec)

-- 事务给我们提供了一个返回的机会。

set autocommit=1;

mysql> set autocommit=1;
Query OK, 0 rows affected (0.00 sec)

mysql> select @@autocommit;   
+--------------+
| @@autocommit |
+--------------+
|            1 |
+--------------+
1 row in set (0.00 sec)


begin; 
-- 或者 
start transaction; 
-- 都可以帮我们手动开启一个事务

mysql> select * from user;
+----+------+-------+
| id | name | money |
+----+------+-------+
|  1 | a    |  1000 |
|  2 | b    |  1000 |
+----+------+-------+
2 rows in set (0.00 sec)

mysql> update user set money=money-100 where name='a';
Query OK, 1 row affected (0.07 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> update user set money=money+100 where name='b';
Query OK, 1 row affected (0.06 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> 
mysql> select * from user;
+----+------+-------+
| id | name | money |
+----+------+-------+
|  1 | a    |   900 |
|  2 | b    |  1100 |
+----+------+-------+
2 rows in set (0.00 sec)

-- 事务回滚
mysql> rollback;
Query OK, 0 rows affected (0.00 sec)

-- 没有被撤销
mysql> select * from user;
+----+------+-------+
| id | name | money |
+----+------+-------+
|  1 | a    |   900 |
|  2 | b    |  1100 |
+----+------+-------+
2 rows in set (0.00 sec)




-- 手动开启事务（1）

begin;
update user set money=money-100 where name='a';
update user set money=money+100 where name='b';


mysql> begin;
Query OK, 0 rows affected (0.00 sec)

mysql> update user set money=money-100 where name='a';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> update user set money=money+100 where name='b';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from user;
+----+------+-------+
| id | name | money |
+----+------+-------+
|  1 | a    |   800 |
|  2 | b    |  1200 |
+----+------+-------+
2 rows in set (0.00 sec)

mysql> rollback;
Query OK, 0 rows affected (0.04 sec)

mysql> select * from user;
+----+------+-------+
| id | name | money |
+----+------+-------+
|  1 | a    |   900 |
|  2 | b    |  1100 |
+----+------+-------+
2 rows in set (0.00 sec)


-- 手动开启事务（2）

start transaction;
update user set money=money-100 where name='a';
update user set money=money+100 where name='b';


mysql> start transaction;
Query OK, 0 rows affected (0.00 sec)

mysql> update user set money=money-100 where name='a';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> update user set money=money+100 where name='b';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from user;
+----+------+-------+
| id | name | money |
+----+------+-------+
|  1 | a    |   800 |
|  2 | b    |  1200 |
+----+------+-------+
2 rows in set (0.00 sec)

mysql> rollback;
Query OK, 0 rows affected (0.17 sec)

mysql> select * from user;
+----+------+-------+
| id | name | money |
+----+------+-------+
|  1 | a    |   900 |
|  2 | b    |  1100 |
+----+------+-------+
2 rows in set (0.00 sec)



-- 事务开启之后，一旦 commit 提交，就不可以回滚（也就是当前的这个事务在提交的时候就结束了）
mysql> start transaction;
Query OK, 0 rows affected (0.00 sec)

mysql> update user set money=money-100 where name='a';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> update user set money=money+100 where name='b';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> commit;
Query OK, 0 rows affected (0.08 sec)

mysql> select * from user;
+----+------+-------+
| id | name | money |
+----+------+-------+
|  1 | a    |   800 |
|  2 | b    |  1200 |
+----+------+-------+
2 rows in set (0.00 sec)

mysql> rollback;
Query OK, 0 rows affected (0.00 sec)

mysql> select * from user;
+----+------+-------+
| id | name | money |
+----+------+-------+
|  1 | a    |   800 |
|  2 | b    |  1200 |
+----+------+-------+
2 rows in set (0.00 sec)


事务的四大特征：
A 原子性：事务是最小的单位，不可以在分割。
C 一致性：事务要求，同一事务中的 sql 语句，必须保证同时成功或者同时失败。
I 隔离性：事务1 和 事务2 之间是具有隔离性的。
D 持久性：事务一旦结束（commit，rollback），就不可以返回。

事务开启:
	1. 修改默认提交  set autocommit=0;
	2. begin;
	3. start transaction;

事务手动提交：
	commit;

事务手动回滚：
	rollback;



-- 事务的隔离性：

1、read uncommitted;		读未提交的
2、read committed;		读已经提交的
3、repeatable read;		可以重复读
4、serializable;			串行化

1-read uncommitted

如果有事务a,和事务b，
a 事务对数据进行操作，在操作的过程中，事务没有被提交，但是b 可以看见a 操作的结果。



bank数据库 user表

insert into user values(3,'小明',1000);
insert into user values(4,'淘宝店',1000);

mysql> select * from user;
+----+-----------+-------+
| id | name      | money |
+----+-----------+-------+
|  1 | a         |   800 |
|  2 | b         |  1200 |
|  3 | 小明      |  1000 |
|  4 | 淘宝店    |  1000 |
+----+-----------+-------+
4 rows in set (0.00 sec)

-- 如何查看数据库的隔离级别？

mysql  8.0:
-- 系统级别的
select @@global.transaction_isolation;	
-- 会话级别的
select @@transaction_isolation;

-- mysql 默认隔离级别 REPEATABLE-READ
mysql> select @@global.transaction_isolation;
+--------------------------------+
| @@global.transaction_isolation |
+--------------------------------+
| REPEATABLE-READ                |
+--------------------------------+
1 row in set (0.00 sec)


mysql  5.x:
select @@global.tx_isolation;
select @@tx_isolation;


-- 如何修改隔离级别？

mysql> set global transaction isolation level read uncommitted;
Query OK, 0 rows affected (0.00 sec)

mysql> 
mysql> select @@global.transaction_isolation;
+--------------------------------+
| @@global.transaction_isolation |
+--------------------------------+
| READ-UNCOMMITTED               |
+--------------------------------+
1 row in set (0.00 sec)



-- 转账：小明在淘宝店买鞋子:800块钱，
	小明-》成都 ATM
	淘宝店-》广州 ATM

start transaction;
update user set money=money-800 where name='小明';
update user set money=money+800 where name='淘宝店';


mysql> select * from user;
+----+-----------+-------+
| id | name      | money |
+----+-----------+-------+
|  1 | a         |   800 |
|  2 | b         |  1200 |
|  3 | 小明      |   200 |
|  4 | 淘宝店    |  1800 |
+----+-----------+-------+
4 rows in set (0.00 sec)

-- 给淘宝店打电话，说你去查一下，是不是到账了

-- 淘宝店在广州查账
mysql> select * from user;
+----+-----------+-------+
| id | name      | money |
+----+-----------+-------+
|  1 | a         |   800 |
|  2 | b         |  1200 |
|  3 | 小明      |   200 |
|  4 | 淘宝店    |  1800 |
+----+-----------+-------+
4 rows in set (0.00 sec)


-- 发货
-- 晚上请女朋友吃好吃的
-- 1800

-- 小明-》成都
mysql> rollback;
Query OK, 0 rows affected (0.02 sec)

mysql> select * from user;
+----+-----------+-------+
| id | name      | money |
+----+-----------+-------+
|  1 | a         |   800 |
|  2 | b         |  1200 |
|  3 | 小明      |  1000 |
|  4 | 淘宝店    |  1000 |
+----+-----------+-------+
4 rows in set (0.00 sec)

-- 结账的时候发现钱不够
mysql> select * from user;
+----+-----------+-------+
| id | name      | money |
+----+-----------+-------+
|  1 | a         |   800 |
|  2 | b         |  1200 |
|  3 | 小明      |  1000 |
|  4 | 淘宝店    |  1000 |
+----+-----------+-------+
4 rows in set (0.00 sec)


-- 如果两个不同的地方，都在进行操作，如果事务a 开启之后，他的数据可以被其他事务读取到。
-- 这样就会出现（脏读）
-- 脏读：一个事务读到了另外一个事务没有提交的数据，就叫做脏读。
-- 实际开发是不允许脏读出现的。


2、read committed;		读已经提交的


set global transaction isolation level read committed;

select @@global.transaction_isolation;	

-- 修改隔离级别为 READ-COMMITTED
mysql> select @@global.transaction_isolation;
+--------------------------------+
| @@global.transaction_isolation |
+--------------------------------+
| READ-COMMITTED                 |
+--------------------------------+
1 row in set (0.00 sec)

bank 数据库 user 表

小张：银行的会计
start transaction;
select * from user;
+----+-----------+-------+
| id | name      | money |
+----+-----------+-------+
|  1 | a         |   800 |
|  2 | b         |  1200 |
|  3 | 小明      |  1000 |
|  4 | 淘宝店    |  1000 |
+----+-----------+-------+
4 rows in set (0.00 sec)

小张出去上厕所去了。。。抽烟

小王：
start transaction;
insert into user values(5,'c',100);
commit;

+----+-----------+-------+
| id | name      | money |
+----+-----------+-------+
|  1 | a         |   800 |
|  2 | b         |  1200 |
|  3 | 小明      |  1000 |
|  4 | 淘宝店    |  1000 |
|  5 | c         |   100 |
+----+-----------+-------+
5 rows in set (0.00 sec)


-- 小张上完厕所，抽完烟回来了
select avg(money) from user;

+------------+
| avg(money) |
+------------+
|   820.0000 |
+------------+
1 row in set (0.00 sec)

-- money 的平均值不是 1000，变少了？

-- 虽然我只能读到另外一个事务提交的数据，但还是会出现问题，就是
-- 读取同一个表的数据，发现前后不一致。
-- 不可重复读现象：read committed


3、repeatable read;		可以重复读


set global transaction isolation level repeatable read;

select @@global.transaction_isolation;	

mysql> select @@global.transaction_isolation;
+--------------------------------+
| @@global.transaction_isolation |
+--------------------------------+
| REPEATABLE-READ                |
+--------------------------------+
1 row in set (0.00 sec)

-- 在 REPEATABLE-READ 隔离级别下又会出现什么问题？

select * from user;

mysql> select * from user;
+----+-----------+-------+
| id | name      | money |
+----+-----------+-------+
|  1 | a         |   800 |
|  2 | b         |  1200 |
|  3 | 小明      |  1000 |
|  4 | 淘宝店    |  1000 |
|  5 | c         |   100 |
+----+-----------+-------+
5 rows in set (0.00 sec)


-- 张全蛋-成都
start transaction;


-- 王尼玛-北京
start transaction;


-- 张全蛋-成都
mysql> insert into user values(6,'d',1000);
Query OK, 1 row affected (0.00 sec)

mysql> commit;
Query OK, 0 rows affected (0.11 sec)

mysql> select * from user;
+----+-----------+-------+
| id | name      | money |
+----+-----------+-------+
|  1 | a         |   800 |
|  2 | b         |  1200 |
|  3 | 小明      |  1000 |
|  4 | 淘宝店    |  1000 |
|  5 | c         |   100 |
|  6 | d         |  1000 |
+----+-----------+-------+
6 rows in set (0.00 sec)

-- 王尼玛-北京
mysql> select * from user;
+----+-----------+-------+
| id | name      | money |
+----+-----------+-------+
|  1 | a         |   800 |
|  2 | b         |  1200 |
|  3 | 小明      |  1000 |
|  4 | 淘宝店    |  1000 |
|  5 | c         |   100 |
+----+-----------+-------+
5 rows in set (0.00 sec)

mysql> insert into user values(6,'d',1000);
ERROR 1062 (23000): Duplicate entry '6' for key 'PRIMARY'


-- 这种现象就叫做幻读！！
-- 事务a和事务b 同时操作一张表，事务a提交的数据，也不能被事务b读到，就可以造成幻读。




4、serializable;			串行化


set global transaction isolation level serializable;

select @@global.transaction_isolation;	

-- 修改隔离级别为串行化
mysql> select @@global.transaction_isolation;
+--------------------------------+
| @@global.transaction_isolation |
+--------------------------------+
| SERIALIZABLE                   |
+--------------------------------+
1 row in set (0.00 sec)


mysql> select * from user;
+----+-----------+-------+
| id | name      | money |
+----+-----------+-------+
|  1 | a         |   800 |
|  2 | b         |  1200 |
|  3 | 小明      |  1000 |
|  4 | 淘宝店    |  1000 |
|  5 | c         |   100 |
|  6 | d         |  1000 |
+----+-----------+-------+
6 rows in set (0.00 sec)

-- 张全蛋-成都
start transaction;


-- 王尼玛-北京
start transaction;


-- 张全蛋-成都
mysql> insert into user values(7,'赵铁柱',1000);
Query OK, 1 row affected (0.01 sec)

mysql> commit;
Query OK, 0 rows affected (0.17 sec)

mysql> select * from user;
+----+-----------+-------+
| id | name      | money |
+----+-----------+-------+
|  1 | a         |   800 |
|  2 | b         |  1200 |
|  3 | 小明      |  1000 |
|  4 | 淘宝店    |  1000 |
|  5 | c         |   100 |
|  6 | d         |  1000 |
|  7 | 赵铁柱    |  1000 |
+----+-----------+-------+
7 rows in set (0.00 sec)


-- 王尼玛-北京
mysql> select * from user;
+----+-----------+-------+
| id | name      | money |
+----+-----------+-------+
|  1 | a         |   800 |
|  2 | b         |  1200 |
|  3 | 小明      |  1000 |
|  4 | 淘宝店    |  1000 |
|  5 | c         |   100 |
|  6 | d         |  1000 |
|  7 | 赵铁柱    |  1000 |
+----+-----------+-------+
7 rows in set (0.00 sec)


-- 张全蛋-成都

start transaction;
insert into user values(8,'王小花',1000);

-- sql语句被卡主了？
mysql> insert into user values(8,'王小花',1000);


-- 当user 表被另外一个事务操作的时候，其他事务里面的写操作，是不可以进行的。
-- 进入排队状态（串行化），指导王尼玛那边事务结束之后，张全蛋这个的写入操作才会执行。
-- 在没有等待超时的情况下。


-- 王尼玛-北京
mysql> commit;
Query OK, 0 rows affected (0.00 sec)


-- 张全蛋-成都
Query OK, 1 row affected (7.76 sec)




-- 串行化问题是，性能特差！！！

READ-UNCOMMITTED > READ-COMMITTED > REPEATABLE-READ > SERIALIZABLE;
-- 隔离级别越高，性能越差

mysql 默认隔离级别是 REPEATABLE-READ


实际开发中，一般都是使用默认，但是幻读问题我们需要解决！
使用加锁的方式解决：



-- 乐观锁

乐观锁不是数据库自带的，需要我们自己去实现。乐观锁是指操作数据库时(更新操作)，想法很乐观，
认为这次的操作不会导致冲突，在操作数据时，并不进行任何其他的特殊处理（也就是不加锁），
而在进行更新后，再去判断是否有冲突了。

通常实现是这样的：在表中的数据进行操作时(更新)，先给数据表加一个版本(version)字段，
每操作一次，将那条记录的版本号加1。
也就是先查询出那条记录，获取出version字段,
如果要对那条记录进行操作(更新),则先判断此刻version的值是否与刚刚查询出来时的version的值相等，
如果相等，则说明这段期间，没有其他程序对其进行操作，则可以执行更新，将version字段的值加1；
如果更新时发现此刻的version值与刚刚获取出来的version的值不相等，
则说明这段期间已经有其他程序对其进行操作了，则不进行更新操作。

-- 悲观锁
与乐观锁相对应的就是悲观锁了。
悲观锁就是在操作数据时，认为此操作会出现数据冲突，
所以在进行每次操作时都要通过获取锁才能进行对相同数据的操作，
这点跟java中的synchronized很相似，所以悲观锁需要耗费较多的时间。
另外与乐观锁相对应的，悲观锁是由数据库自己实现了的，
要用的时候，我们直接调用数据库的相关语句就可以了。

说到这里，由悲观锁涉及到的另外两个锁概念就出来了，

它们就是共享锁与排它锁。
共享锁和排它锁是悲观锁的不同的实现，它俩都属于悲观锁的范畴


1.共享锁

共享锁指的就是对于多个不同的事务，对同一个资源共享同一个锁。
相当于对于同一把门，它拥有多个钥匙一样。
就像这样，你家有一个大门，大门的钥匙有好几把，
你有一把，你女朋友有一把，你们都可能通过这把钥匙进入你们家，进去啪啪啪啥的，
一下理解了哈，没错，这个就是所谓的共享锁。

刚刚说了，对于悲观锁，一般数据库已经实现了，共享锁也属于悲观锁的一种，
那么共享锁在mysql中是通过什么命令来调用呢。
通过查询资料，了解到通过在执行语句后面加上lock in share mode就代表对某些资源加上共享锁了。


2.排它锁

排它锁与共享锁相对应，就是指对于多个不同的事务，对同一个资源只能有一把锁。
与共享锁类型，在需要执行的语句后面加上for update就可以了


3.行锁
行锁，由字面意思理解，就是给某一行加上锁，也就是一条记录加上锁。

4.表锁
表锁，和行锁相对应，给这个表加上锁。

































