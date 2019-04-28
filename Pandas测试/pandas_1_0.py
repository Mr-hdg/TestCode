import pandas as pd
import os


def func():
    # 判断文件夹是否存在
    if not os.path.exists(csvpath):
        print("文件夹不存在")
        return
    new_file = os.path.join(csvpath, new_xls)
    #new_file = os.path.join(csvpath, new_csv)
    # 返回文件夹下所有文件
    file_n = os.listdir(csvpath)
    result = pd.DataFrame()
    for var in file_n:
        file = os.path.join(csvpath, var)
        if os.path.isdir(file):
            file_n.remove(var)
        val_name = var.split("_")[-1].split(".")[0]
        if var.split(".")[-1] == "xlsx":
            pass
        else:
            d = pd.read_csv(file, engine="python", encoding="utf-8", header=None)
            result = result.append(d.T)
    result.to_excel(new_xls)


def pd_merge(file1, file2, val):
    # csv中文路径处理
    print(file1)
    d1 = pd.read_csv(file1,engine="python", encoding="utf-8", header=None)

    #rf_2 = pd.read_excel(file2)
    #result = pd.concat([d1,d2],axis=1)





if __name__ == '__main__':
    csvpath = u"D:\\STUDY\\机器学习\\12号机组\\齿轮箱低速级径向"
    #csvpath = u"D:\\STUDY\\机器学习\\12号机组\\abc"
    new_xls = "new_xlsx.xlsx"
    new_csv = "new.csv"
    #func()


