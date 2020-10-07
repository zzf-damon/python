import pymysql, os


class LinkMysql():
    def __enter__(self):
        self.db = pymysql.Connect(host="222.197.219.12", user="root", password="123456", db="recommend", port=3306)
        self.cursor = self.db.cursor()
        return self

    def get_all(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    # select 语句
    def select_sql(self, sql):
        self.cursor.execute(sql)
        result_data = self.cursor.fetchall()
        return result_data

    # 提交语句 insert update delete
    def commit_sql(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
        return "Yes"

    # 提交语句 insert update delete 使用字典的方式提交
    def commit_sql_tuple(self, sql, tuple):
        self.cursor.execute(sql, tuple)
        self.db.commit()
        return "Yes"

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    dict = {
        "CATEGORY": "test"
        ,
        "CODE": "1"
    }
    with LinkMysql() as L:
        # L.commit_sql_tuple("insert into category(category, code) values (%s,%s)", (dict["CATEGORY"], dict["CODE"]))
        print(L.select_sql("select * from category"))



#%%

# -*-coding:utf-8-*-
import pymysql, os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
dict1 = {'ID': '5d1b6e8fc5240cb6d41d11dc1',
         'TITLE': '厦门特大走私案7名案犯伏法',
         'CONTENT': '历史上的今天2001年2月23日，经最高法核准，厦门特大走私案首批案件中被判处死刑的王金挺等7名被告人分别在厦门、福州、泉州三地被执行死刑。王金挺等人于1996年至1998年间，分别与赖昌星走私犯罪集团相互勾结或事先通谋，大肆走私香烟、汽车等货物。',
         'COMMENT': '太原涉案民警王文军伤害女访民致死，举报半月被逮捕查办；安徽芜湖县建委主任邓立武预致女访民死地，举报超半年仍逍遥法外！官官相护腐败勾连凌于驾党纪国法之上，深受侵害访民群众死磕查处，让十八大后不收敛不收手者付出代价安徽芜湖县安徽发布人民网舆情监测室央视政务微博中国职务犯罪预防网\n很荣幸参与了我们国家历史上真正的惊天大案！难忘的经历！\n头头没事，小弟完了',
         }


class LinkMySql(object):
    def __enter__(self):
        self.db = pymysql.Connect(host="222.197.219.12", user="root", password="123456", db="recommend", port=3306)
        self.cursor = self.db.cursor()
        return self

    def get_all(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def select_up_down(self, number):
        self.cursor.execute("SELECT * FROM weibo_law WHERE id={}".format(number))
        res = self.cursor.fetchall()
        return res

    def Insert_All_Data(self, table, dict):
        qmarks = ', '.join(['%s'] * len(dict))
        cols = ', '.join(dict.keys())
        sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, cols, qmarks)
        self.cursor.execute(sql, list(dict.values()))
        self.db.commit()

    def select_not_sign(self):
        self.cursor.execute("select * from weibo_law WHERE SIGN is NULL  LIMIT 1")
        res = self.cursor.fetchall()
        return res

    def update_weibo_sign(self, sign, id):
        sql = "UPDATE weibo_law SET weibo_law.SIGN = {sign} WHERE ID = '{id}'".format(sign=sign, id=id)
        self.cursor.execute(sql)
        self.db.commit()

    def select_table_(self, table):
        self.cursor.execute("select * from {}".format(table))
        res = self.cursor.fetchall()
        return res

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    with LinkMySql() as L:
        COURT = L.select_table_("court")
    # with open("../Datas/court", "r", encoding='utf-8') as f:
    #     data = f.readlines()
    #
    # print(data)
    # print(COURT)
    # for i in COURT:
    #     if i in