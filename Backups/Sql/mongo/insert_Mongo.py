from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.recommend  # 指定数据库，如果没有会自动创建  相当于 db = client['test']
collection = db.weibo  # 指定集合如果没有回自动创建  相当于 collection = db['test']


student = {
    '_id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

result = collection.insert_one(student)   # result = collection.insert([student1, student2])    插入多条  inert_many
print(result)