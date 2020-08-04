 主键 PK

它能够唯一确定一张表中的一条记录，也就是我们通过给某个字段添加约束，就可以使得该字段不重复且不为空
create table user(
	id int primary key,  # 主键约束，不为空，且唯一，查找方便
    name varchar(20)
)


联合主键

 自增 AI
create table user(
	id int ,
    name varchar(20),
    password varchar(20),
    primary key(id,name) # 同时给多个列命名不让有重复元素出现，主键加起来不重复就可以
)


 自增约束
create table user(
	id int primary key auto_increment, # 自动生成主键的值，
    name varchar(20)
)


# 后期添加主键
alter table table_name add primary key(id);   # 删除 drop，修改modify


 外键

涉及到两个表，主表，子表

--班级--
create table classes(
	id int primary key ,
    name varchar(20)
)


--学生--
create table students(
	id int primary key ,
    name varchar(20),
    class_id int,
    foreign key(class_id) references classes(id)
)
子表不能给主表自动添加元素，如果主表中不存在元素，那么就不能添加元素，不能删除



 唯一 UQ

约束修饰的字段的值不可以重复,不可以为空

创建
alter table table_name add unique(key);

create table user(
	id int ,
    name varchar(20),
    password varchar(20), #也可以写后面
    unique(name)
)
同样的也有联合键，道理同联合主键。

删除
alter table table_name drop index key;


添加
alter table table_name modify  key  varchar(20)  unique;

非空 NN
默认

  当我们插入字段值的时候，如果没有传值，就会使用默认值。
create table user(
	id int ,
    name varchar(20),
    age int default 10   # 如果没有插入数据，那么就会默认的使用10
)




BIN 二进制
UN 整数
ZF 填充 0 位
