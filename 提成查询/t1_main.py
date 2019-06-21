from t1_sql import MySql
from t1_rdxls import rd_excel

class Main_Sql(object):

    def __init__(self):
        db_list = ["10.100.0.100", "3306", "root", "test123", "test"]
        self.my_xls = rd_excel()
        self.my_sql = MySql(db_list)
        #res = self.my_sql.find_tbheader("test8")

    def _query_salesman(self, name):
        tb_name = "test8"
        res = self.my_sql.find_name(tb_name, name)
        row = len(res)
        col = len(res[0])-1
        return row, col, res

    def _header_name(self):
        res = self.my_sql.find_tbheader("test8")
        res.remove("id")
        return res

    def _tabe_row_col(self):
        np = self.my_sql.FindAll("test8")
        row = len(np)
        col = len(np[0])-1
        return row, col



if __name__ == '__main__':
    a = Main_Sql()
    row, col, res = a._query_salesman("江燕萍")
    print(row, col)
    print(res)
    print(a._header_name())