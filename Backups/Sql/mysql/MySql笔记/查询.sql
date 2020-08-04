select   key from table_name;
distinct 去除重复的


区间   没有num1 num2
select * from table_name where key between num1 and num2;
select * from table_name where key > num1 and key < num2;

表示或  同一个属性
select * from table_name where key in(num1,num2,num3);
        同一个表中的不同属性
select * from table_name where key1=value1 or key2= value2;

降序  从高到低
select * from table_name order by key desc;  去除desc就是升序 也是asc

以key1升序，以key2降序
select * from table_name order by key1 asc,key2 desc;

排序 选出指定的排序的第一个，由0,1控制，
select key1,key2,key3 from table_name order by key1 desc limit 0,1;

统计 count
select count(*) from table_name where key=value;

子查询或排序
select key1,key2 from table_name where key3=(select max(key3) from table_name);

平均成绩 avg（）
select avg(key) from table_name where key2=value;
查询对于某一列的所有的平均值
group by 分组
select key2,avg(key) from table_name group  by key2;

查询score表中至少有2名学生选修的并以3开头的课程的平均成绩
select cno,avg（degree） from score group by cno 
having  count(cno)>=2 and cno like '3%';
        like 多以查找以什么开头的  ,模糊查询
        后面时正则   % 是sql中的通配符
        having 条件

从不同的两个表中选中两列，同时展示
select t1_key1,t2_key2,t2_key3 from t1,t2 
where t1.key1 = t2.key1;

多表查询，
select t1_key1,t2_key2,t3_key3 from t1,t2,t3
where t1.key_num1 = t2.key_num1 and t3.key_num2 = t2.key_num2;

别名   同时可以与其他的语句一起使用
select t1.key1 as alias from t1; 


子查询加分组求平均分

select key1,avg（key2） 
from t1
where key3 in   或者关系，
(select key3 from t2 where key4=value)  先把key3在第二张表中的key4=value取出来
group by key1;  用key1，分组



查询选修value1课程的成绩高于value2号同学的value1成绩的所有同学

select * from t1 
where key1= value1 and  degree>
(select degree from 
where key1=value1 and key2 = value2
);

year() 可以查出年份


union 可以拼接两个查询语句，如果前后两个表的名字不同会默认使用第一个表的名字

任意一个 any
所有 all   语句可以嵌套

select * from table_name name where name.key;  # name就是table_name的别名，同时别名可以在同一条语句中使用真实表的属性。



select year(now()); 查询当前年份


max 最大  min 最小













