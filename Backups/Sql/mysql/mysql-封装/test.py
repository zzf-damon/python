from zzfsql import zzfmysql
from time import sleep
db = zzfmysql ("localhost","root","123456","self")


while True:
    sql = input("请输入sql语句：   (不输入，表示退出)")
    model = input("请输入模式:(1表示查询，2表示其他提交操作)")
    if sql and model == "1":
        results = db.get_all(sql)
        print(results)
    elif model is "2":
        results = db.edit(sql)
        print(results)  
    else:
        print("正在结束程序......")
        sleep(0.5)
        db.close()
        print("程序结束")
        sleep(0.5)
        break

