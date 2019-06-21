import os
import pandas as pd
import t1_sql

class rd_excel(object):

    path = os.path.join(os.getcwd(), "统计资料")

    # 返回文件夹内文件名的列表
    def file_name(self):
        res_list = []
        names = os.listdir(self.path)
        for var in names:
            a = os.path.join(self.path, var)
            res_list.append(a)
        return res_list

    def leading_file(self, file):
        res = []
        xls_tb = pd.ExcelFile(file).sheet_names
        print(file,xls_tb)
        data = pd.read_excel(file, sheet_name=u"业务员")
        header = data.columns.values.tolist()
        print(header)
        count = data["序号"].count()
        data["备注"] = data["备注"].fillna("-")
        data = data.iloc[:,[1,2,3,4,5,6,7,8,10]].fillna(0)
        for i in range(count):
            res.append(data.loc[i].tolist())
        return res



if __name__ == '__main__':
    db_list = ["10.100.0.100", "3306", "root", "test123", "test"]
    tb_name = "test8"
    my_xls = rd_excel()
    my_sql = t1_sql.MySql(db_list)
    files = my_xls.file_name()
    #my_sql.init_sql(tb_name)
    """
    for var in files:
        data = my_xls.leading_file(var)
        for i in data:
            my_sql.input_data(tb_name, i)
    """
    #input_name = input("请输入查询的人：")
    #res = my_sql.find_name(tb_name, input_name)
    #print(res)
    #res = my_sql.find_tbheader(tb_name)
    #for var in res:
        #print(var[-1])
    my_xls.leading_file(files[0])