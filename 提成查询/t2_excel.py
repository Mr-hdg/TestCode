import xlrd, xlwt, os
import pandas as pd

data_path = u"./data/all_data.xls"


class ExcelFunc(object):

    def __init__(self, *args, **kw):
        path = args[0]
        self.yw_tb_data, self.yw_tb_rows, self.yw_tb_cols, \
        self.cz_tb_data, self.cz_tb_rows, self.cz_tb_cols = self._all_data(path)
        self.ayw_tb_data, self.ayw_tb_rows, self.ayw_tb_cols, \
        self.acz_tb_data, self.acz_tb_rows, self.acz_tb_cols = self._all_data(data_path)

    def _all_data(self, path):
        data = xlrd.open_workbook(path)
        tb_name = ["业务员", "操作员"]
        yw_table_data = data.sheet_by_name(tb_name[0])
        yw_rows = yw_table_data.nrows
        yw_cols = yw_table_data.ncols
        cz_table_data = data.sheet_by_name(tb_name[1])
        cz_rows = cz_table_data.nrows
        cz_cols = cz_table_data.ncols

        return yw_table_data, yw_rows, yw_cols, cz_table_data, cz_rows, cz_cols

    def _rd_value(self, table_data, rows, cols, start=1):
        res_list = []
        for i in range(start, rows):
            num = table_data.cell(i, 0).value
            if isinstance(num, float):
                res_value = table_data.row_values(i, start_colx=1)
                res_list.append(res_value)
        return res_list

    def _wt_value(self):
        workbook = xlwt.Workbook(encoding="utf-8")
        yw_res = self._rd_value(self.yw_tb_data, self.yw_tb_rows, self.yw_tb_cols)
        ayw_res = self._rd_value(self.ayw_tb_data, self.ayw_tb_rows, self.ayw_tb_cols)
        cz_res = self._rd_value(self.cz_tb_data, self.cz_tb_rows, self.cz_tb_cols)
        acz_res = self._rd_value(self.acz_tb_data, self.acz_tb_rows, self.acz_tb_cols)
        header_list = [['id', '姓名', '月份', '利润', '人数', '个人业务', '公司业务', '应发提成', '实发提成', '未发提成', '备注'],
                       ['id', '姓名', '月份', '利润', '提成', '上月未发', '实发提成', "备注"]]
        for var in yw_res:
            for a_var in ayw_res:
                print(var[:2], a_var[:2], var[:2] == a_var[:2])
                if var[:2] == a_var[:2]:
                    return "数据已经存在"

        for var in yw_res:
            ayw_res.append(var)
        for var in cz_res:
            acz_res.append(var)
        all_data = [ayw_res, acz_res]
        tb_name = ["业务员", "操作员"]

        for i in range(len(tb_name)):
            worksheet = workbook.add_sheet(tb_name[i])
            self._wt_func(worksheet, header_list[i], all_data[i])
            print(all_data[i])
        workbook.save(data_path)
        return  "数据添加成功"

    def _wt_func(self, worksheet, header_list, data):
        for i in range(len(header_list)):
            worksheet.write(0, i, header_list[i])
        for i in range(len(data)):
            for j in range(len(data[0])):
                if j == 0:
                    worksheet.write(i + 1, 0, i + 1)
                worksheet.write(i + 1, j + 1, data[i][j])


class ShowExcel(object):

    def show_data(self, sheet_name, query_name):
        data = pd.read_excel(data_path, sheet_name=sheet_name)
        if sheet_name == "业务员":
            val_col = 9
            val = 0
        else:
            val_col = 0
            val = 0
        all_data = []
        rows = data["id"].count()
        header = data.columns.values.tolist()
        header.remove("id")
        cols = len(header)
        data["备注"] = data["备注"].fillna("-")
        data = data.fillna(0)
        for i in range(rows):
            if query_name in data.loc[i][1]:
                all_data.append(data.loc[i].tolist())
                if val_col == 9:
                    val += data.loc[i][val_col]
        return header, rows, cols, all_data, val


if __name__ == '__main__':
    PATH = u"./统计资料/201904月提成.xls"
    con_list = ["10.100.0.100", "3306", "root", "test123", "test"]
    #a = ExcelFunc(PATH)
    #res = a._wt_value()
    #print(res.__next__())
    b = ShowExcel()
    b.show_data("业务员", "江燕萍")

