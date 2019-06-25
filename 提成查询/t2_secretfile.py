import os
import pythoncom
import win32com.client as wct


class SecretFile(object):

    filename = os.path.join(os.getcwd(), "data\\all_data.xls")
    tmpfile = os.path.join(os.getcwd(), "data\\tmp_data.xls")

    def _save_tmpfile(self, passwd):
        pythoncom.CoInitialize()
        xlApp = wct.DispatchEx("Excel.Application")
        xlApp.DisplayAlerts = False
        xlwb = xlApp.Workbooks.Open(self.filename, False, True, None, passwd)
        # 保存excel设置访问密码
        xlwb.SaveAs(self.tmpfile, None, "")
        xlwb.Close()
        xlApp.Quit()
        del(xlApp)

    def _save_file(self, passwd):
        pythoncom.CoInitialize()
        xlApp = wct.DispatchEx("Excel.Application")
        xlApp.DisplayAlerts = False
        xlwb = xlApp.Workbooks.Open(self.tmpfile, False, True, None)
        xlwb.SaveAs(self.filename, None, passwd)
        xlwb.Close()
        xlApp.Quit()
        del (xlApp)

    def _del_file(self):
        os.remove(self.tmpfile)


if __name__ == '__main__':
    a = SecretFile()
    a._save_tmpfile("456")
    a._save_file()
    #a._save_file()
    a._del_file()

    #test()