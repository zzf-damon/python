--- sql 的四种连接查询
-- 内连接

inner	join  或 join


 ---外链接
 1. 左连接 left join 或 left outer join
 2. 右连接 right join 或 right outer join
 3. 完全外链接 full join 或 full outer join
	
	
	创建两个表
	
	person 表
	 card 表


1
 	create table person(
	id int,
	name varchar(20),
	cardId int
)

2   	create table card(
	id int,
	name varchar(20),
)


insert into card values(1,"饭卡");
insert into card values(2,"建行卡");
insert into card values(3,"农行卡");
insert into card values(4,"工商卡");
insert into card values(5,"邮政卡");




insert into person values(1,"张三",1);
insert into person values(2,"李四",3);
insert into person values(3,"王五",6);
insert into person values(4,"张三",9);



--- inner join  内联查询

  select * from person inner join card on person.cardId=card.id;

-------就是把两张表中的数据，通过某个字段的相对，查询出相关记录数据


--- left join   左外连接
   select * from person left join card on person.cardId = card.id;

----	会把左边表里面的所有数据取出来，而左边的数据，如果有相等的，就会显示出来，如果没有就会补为null。



--- right join 右外连接 与左外连接相反




--- full join  全外连接

   select * from person full join card on person.cardId = card.id;

--- mysql 不支持全外连接,,但是可以用左外与右外的相合组成全外连接

	select * from person left join card on person.cardId=card.id
	union
	select * from person right join card on person.cardId = card.id;














