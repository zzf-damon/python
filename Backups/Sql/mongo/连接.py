from pymongo import MongoClient
# from bson.objectid import ObjectId# 根据id查询
import pymongo

## 创建连接
connect = MongoClient(host="127.0.0.1", port=27017)
# client = MongoClient('mongodb://localhost:27017/')使用MongoDB的URI格式
## 选择数据库
list = connect.list_database_names()  # 显示所有数据库的名字
print(list)
db = connect.test  # test是数据库的名字
### 打印当前库名字
print(db.name)
### 查看当前中的所有集合
ret = db.list_collection_names()  # 显示所有集合的名字并返回一个列表
print(ret)

# 接下里就可以用collection来完成对数据库表的一些操作
# 连接所用集合，也就是我们通常所说的表，test为表名
collection = db.stus
# 查找集合中所有数据
for item in collection.find():  # 如何是find，返回的不知道是什么，只能用for，如果是find_one 可以成功打印，
    print(item)

res = collection.find().sort("age")  # 升序
# res = collection.find().sort("age",pymongo.DESCENDING) #降序
# res  = collection.find().skip(3).limit(5) # 越过三条，拿五条 分页查询
for row in res:
    print(row)

# 查找集合中单条数据
# print(collection.find_one({"name":"白晶晶"}))
# print(collection.count() == 0)

# 向集合中插入数据
# collection.insert({"name": 'Tom', "age": 25, "addr": 'Cleveland'})
#
# # 更新集合中的数据,第一个大括号里为更新条件，第二个大括号为更新之后的内容
# collection.update({"_id": '白晶晶'}, {"$set":{"name":"白晶晶","age":17,"gender":"women"}})
# 删除
# collection.remove("条件")
## 关闭连接
connect.close()

# # 删除集合collection中的所有数据
# collection.remove()
