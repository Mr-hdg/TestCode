import pymysql.cursors

class MySql(object):

    # 用构造函数实现数据库连接，并引入mydb参数，实现调用不同的数据库
    def __init__(self, con_name):
        server_ip, server_port, server_user, server_pwd, server_db = con_name
        if server_db == "-":
            server_db = None
        config = {
            "host": server_ip,
            "port": int(server_port),
            "user": server_user,
            "password": server_pwd,
            "db": server_db,
        }
        self.con = pymysql.connect(**config)
        self.cursor = self.con.cursor()

    def show_db(self):
        self.cursor.execute("show databases")
        result = self.cursor.fetchall()
        return result

    def init_sql(self, table_name):
        sql = """
         CREATE TABLE %s(
        emp_Id int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
        emp_name VARCHAR(50) NOT NULL COMMENT '姓名',
        emp_month VARCHAR(50) NOT NULL COMMENT '月份',
        emp_lr DOUBLE COMMENT '利润',
        emp_count DOUBLE COMMENT '人数',
        emp_gr DOUBLE COMMENT '个人业务',
        emp_gs DOUBLE COMMENT '公司业务',
        emp_yf DOUBLE COMMENT '应发提成',
        emp_sf DOUBLE COMMENT '实发提成',
        PRIMARY KEY(emp_id))DEFAULT CHARSET=utf8, COMMENT="员工提成表";
         """%table_name
        self.cursor.execute(sql)

    # 定义查看数据表信息函数，并引入table_field、table_name参数，实现查看不同数据表的建表语句
    def FindAll(self, table_name):
        # 实例变量
        #self.table_name = table_name
        # 定义SQL语句
        sql = "select * from %s" % (table_name)
        sql1 = "desc %s"%table_name
        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 处理结果
            data = self.cursor.fetchall()
            return data
        except Exception as err:
            print("SQL执行错误，原因：", err)

    def input_data(self, table_name, args):
        a, b, c, d, e, f, g, h= args
        i = h-g
        find_sql = "select * from %s where emp_name='%s' and emp_month='%s'"%("test4", a, b)
        self.cursor.execute(find_sql)
        if self.cursor.fetchall():
            print("%s已经添加"%a)
            return
        sql = """insert into %s(emp_name, emp_month, emp_lr, emp_count,emp_gr, emp_gs, emp_yf, emp_sf) 
        values('%s', '%s', '%.2f', '%d', '%.2f', '%.2f', '%.2f', '%.2f')"""%(table_name, a, b, c, d, e, f, g, h)
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)

    def find_name(self, name):
        # 定义SQL语句
        sql = "select * from test4 WHERE emp_name='%s'"%(name)
        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 处理结果
            data = self.cursor.fetchall()
            if not data:
                print("没有数据")
            return data
        except Exception as err:
            print("SQL执行错误，原因：", err)

if __name__ == '__main__':
    con_list = ["10.100.0.100", "3306", "root", "test123", "test"]
    e_name = "戴建龙"
    e_lr = 12860
    e_count = 166
    e_gr = 0
    e_gs = 0
    e_yf = 0
    e_sf = 0
    test_sql = MySql(con_list)

    a = [e_name, e_count]
    b, c = a
    print(b, c)
