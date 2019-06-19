import os
import pandas as pd
import con_sql

class rd_excel(object):

    def file_name(self):
        res_list = []
        path = os.path.join(os.getcwd(), "统计资料")
        names = os.listdir(path)
        for var in names:
            a = os.path.join(path, var)
            res_list.append(a)
        return res_list

    def lead_file(self):
        res = []
        table_name = pd.ExcelFile(PATH).sheet_names
        #data = pd.DataFrame(pd.read_excel(PATH, sheet_name=u"业务员"))
        data = pd.read_excel(PATH, sheet_name=u"业务员")
        count = data["序号"].count()
        data["备注"] = data["备注"].fillna("-")
        data = data.iloc[:,[1,2,3,4,5,6,7,8,9,10]].fillna(0)
        #data = data.drop(["序号", "8-3月提成未发"], axis=1).fillna(0)
        for i in range(count):
            res.append(data.loc[i].tolist())
        #print(res)
        return res

if __name__ == '__main__':
    PATH = u"./统计资料/201904月提成.xls"
    con_list = ["10.100.0.100", "3306", "root", "test123", "test"]
    a = rd_excel()
    res = a.lead_file()
    b = con_sql.MySql(con_list)
    #b.init_sql()
    a.file_name()
    #print([var for var in res])
    for var in res:
        print(var)
    #for var in a.lead_file():
        #b.input_data(var)
    #for var in b.find_name('戴建龙'):
        #print(var)