import win32com.client

xlApp = win32com.client.Dispatch("Excel.Application")
filename,password = "D:\\STUDY\\TestCode\\提成查询\\data\\all_data2.xls", '456'
xlwb = xlApp.Workbooks.Open(filename, False, True, None, password)

xlwb.SaveAs("D:\\STUDY\\TestCode\\提成查询\\data\\demo1.xls", None, "", "")
xlApp.Quit()