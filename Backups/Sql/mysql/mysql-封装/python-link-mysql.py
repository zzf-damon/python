import pymysql

# 连接数据库
# 参数1 mysql服务所在主机的IP
# 2 用户名
# 3 密码
#4 要连接的数据库名

db = pymysql.Connect(host="localhost",user="root",password="zhang00a",db="example",port=3306)

# 创建一个cursor对象
cursor = db.cursor()
sql1 = " insert into first values('lili',6);"

# 执行sql语句  ,返回执行结果的行数
cursor.execute(sql1)
db.commit()
# 获取返回的信息所有信息
datas = cursor.fetchall()
for data in datas:
    print(data, end="\n")  # 换行打印



# 断开
cursor.close()
db.close()
# rowcount 是一个只读属性，返回execute方法影响的行数
# fetchone():得到结果集的下一行，结果集是一个对象
# fetchmany([size = cursor.arraysize]):得到结果集的下几行
# executemany (sql, args):执行多个数据库查询或命令


#
#插入操作

# try:
#     cursor.execute("insert into tablename values('value')")
#     db.commit()  # 在这里才会真正的提交到数据库中，插入删除修改才需要这句话
# except:
#     db.rollback() # 如果提交失败，回滚到上一次的数据

