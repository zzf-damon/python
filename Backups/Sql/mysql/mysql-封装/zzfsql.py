import pymysql


class zzfmysql(object):
    def __init__(self,host,user,password,db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.db = pymysql.Connect(self.host,self.user,self.password,self.db,port=3306)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_all(self,sql):
        res = ()
        try:
            # self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
        except:
            print("查询失败")
        return res

    def edit(self,sql):
        count = 0
        try:
            # self.connect()
            count = self.cursor.execute(sql)
            self.db.commit()
            print("操作执行成功")
        except:
            print("提交失败")
            self.db.rollback()
        return count


# 批量插入语句
"""
    qmarks = ', '.join(['%s'] * len(my_dict))  # 用于替换记录值
    cols = ', '.join(my_dict.keys())  # 字段名
    sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, cols, qmarks)
    try:
        cursor.execute(sql, my_dict.values())
    except:
        print
        "SQL error:", sys.exc_info()[0]
"""