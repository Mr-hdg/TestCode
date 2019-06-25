import sys, cgitb
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QLabel,
                             QDateEdit, QPushButton, QDialog, QTableWidget, QAbstractItemView,
                             QFileDialog, QTableWidgetItem,QHeaderView, QComboBox, QMessageBox, QVBoxLayout)
from PyQt5.QtCore import Qt, QDate, QCoreApplication, QRect, pyqtSignal, QMetaObject
import qtawesome
from t2_excel import ExcelFunc, ShowExcel
from t2_secretfile import SecretFile
from Mythreading import MyThread



class Qt_Frame(QMainWindow):

    def __init__(self, *args, **kw):
        super(Qt_Frame, self).__init__(*args, **kw)
        self.secret_f = SecretFile()
        #self.secret_f._save_file("456")
        thread = MyThread(target=self.secret_f._save_tmpfile, args=("456",))
        thread.start()
        self._initUI()

    def _initUI(self):
        self.resize(400,250)
        self.setWindowTitle("查询系统 v1.01")

        self.main_widget = QWidget()
        self.main_layout = QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        self.left_widget = QWidget()
        self.left_widget.setObjectName("left_widget")
        self.left_layout = QGridLayout()
        self.left_widget.setLayout(self.left_layout)

        self.center_widget = QWidget()
        self.center_widget.setObjectName("center_widget")
        self.center_layout = QGridLayout()
        self.center_widget.setLayout(self.center_layout)

        self.right_widget = QWidget()
        self.right_widget.setObjectName("right_widget")
        self.right_layout = QGridLayout()
        self.right_widget.setLayout(self.right_layout)

        self.main_layout.addWidget(self.left_widget, 0, 0, 10, 1)
        self.main_layout.addWidget(self.center_widget, 0, 1, 10, 4)
        self.main_layout.addWidget(self.right_widget, 0, 5, 10, 1)

        self._leftUI()
        self._centerUI()
        #self._rightUI()

        self.left_layout.setAlignment(Qt.AlignBottom)
        self.center_layout.setAlignment(Qt.AlignCenter)
        self.right_layout.setAlignment(Qt.AlignTop)
        self.setCentralWidget(self.main_widget)

    def _leftUI(self):
        self.left_soft = QPushButton(qtawesome.icon('fa.folder-open', color='green'), "")
        self.left_soft.clicked.connect(self._leadialog)
        self.left_layout.addWidget(self.left_soft, 0, 1, 2, 1)

    def _centerUI(self):
        self.query_name = QLineEdit()
        self.query_name.setPlaceholderText("请输入要查询的名字")
        self.query_secret = QLineEdit()
        self.query_secret.setPlaceholderText("请输入密码")
        self.query_secret.setEchoMode(QLineEdit.Password)
        self.date1 = QDateEdit(QDate.currentDate())
        self.date1.setCalendarPopup(True)
        self.date2 = QDateEdit(QDate.currentDate())
        self.date2.setCalendarPopup(True)
        self.job_combox = QComboBox(minimumWidth=100)
        self.job_combox.addItems(["业务员", "操作员"])
        self.button = QPushButton("运行")
        self.button.clicked.connect(self._opendialog)

        self.center_layout.addWidget(QLabel("姓名:"), 0, 0, 2, 1)
        self.center_layout.addWidget(self.query_name, 0, 1, 2, 3)
        self.center_layout.addWidget(QLabel("密码:"), 3, 0, 2, 1)
        self.center_layout.addWidget(self.query_secret, 3, 1, 2, 3)
        self.center_layout.addWidget(QLabel("类型:"), 6, 0, 2, 1)
        self.center_layout.addWidget(self.job_combox, 6, 1, 2, 3)
        self.center_layout.addWidget(self.button, 9, 1, 1, 3)

    def _rightUI(self):
        self.right_mini = QPushButton("")  # 最小化
        self.right_visit = QPushButton("")  # 空白按钮
        self.right_close = QPushButton("")  # 关闭
        self.right_layout.addWidget(self.right_mini, 0, 0, 1, 1)
        self.right_layout.addWidget(self.right_visit, 0, 1, 1, 1)
        self.right_layout.addWidget(self.right_close, 0, 2, 1, 1)

    def _opendialog(self):
        name = self.query_name.text()
        pwd = self.query_secret.text()
        job = self.job_combox.currentText()
        my = New_Dialog(self)
        if name and pwd:
            if my._name_and_pwd(name, pwd):
                QMessageBox.warning(self,
                                    "消息框标题",
                                    "请确帐号或密码不正确",
                                    QMessageBox.Ok)
                return
            else:
                my._creat_table_show(name, job)
                my.exec_()
        else:
            QMessageBox.warning(self,
                                "消息框标题",
                                "请确定帐号或密码是否输入正确",
                                QMessageBox.Ok)

    def _leadialog(self):
        my = Lead_Data()
        my.exec_()

    def __del__(self):
        self.secret_f._del_file()


class Lead_Data(QDialog):

    def __init__(self, *args, **kw):
        super(Lead_Data, self).__init__(*args, **kw)
        self.secret_f = SecretFile()
        self._initUI(self)

    def _initUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400,100)
        self.centralwidget = QWidget(MainWindow)
        self.g_layout = QGridLayout(self.centralwidget)
        self.filt_edit = QLineEdit()
        self.filt_edit.setPlaceholderText("文件路径")
        self.open_button = QPushButton("打开")
        self.open_button.clicked.connect(self._openfile)
        self.lead_button = QPushButton("导入")
        self.lead_button.clicked.connect(self._leading)

        self.g_layout.addWidget(self.filt_edit, 0, 1)
        self.g_layout.addWidget(self.open_button, 0, 2)
        self.g_layout.addWidget(self.lead_button, 0, 3)

    def _openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self, "选择文件", "", "Excel files(*.xlsx , *.xls)")
        self.file_path = openfile_name[0]
        self.filt_edit.setText(self.file_path.split("/")[-1])

    def _leading(self):
        a = ExcelFunc(self.file_path, self.secret_f.tmpfile)
        try:
            self.res = a._wt_value()
        except IndexError:
            QMessageBox.warning(self,
                                 "消息框标题",
                                 "导入失败<%s>"%("excel列数少于模板列数"),
                                 QMessageBox.Ok)
        else:
            QMessageBox.warning(self,
                                "消息框标题",
                                "%s"%self.res,
                                QMessageBox.Ok)
            self.close()
            self.secret_f._save_file("456")

class New_Dialog(QDialog):

    def __init__(self, *args, **kw):
        super(New_Dialog, self).__init__(*args, **kw)
        self.secret = SecretFile()
        self.data = ShowExcel(self.secret.tmpfile)
        self._initUI(self)

    def _initUI(self, MainWindow):
        #self.dialog_widget = QWidget()
        self.vlayout = QVBoxLayout()

        self.wf_label = QLabel("未发提成：0")
        #self.wf_label.setGeometry(QRect(10, 0, 100, 100))
        self.wf_label.setObjectName("wf_label")

        self.tableWidget = QTableWidget(11, 10)
        #self.tableWidget.setGeometry(QRect(10, 60, 1060, 380))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)  # 设置列宽
        self.tableWidget.setRowCount(0)  # 设置行高
        self.tableWidget.setStyleSheet("selection-background-color:pink")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.raise_()

        self.vlayout.addWidget(self.wf_label)
        self.vlayout.addWidget(self.tableWidget)

        self.setLayout(self.vlayout)

    def _creat_table_show(self, name, job):
        mylist, row, col, data, res_val = self.data.show_data(job, name)
        self.tableWidget.setColumnCount(col)
        self.tableWidget.setRowCount(row)
        col_line = 150+col*125
        self.tableWidget.setHorizontalHeaderLabels(mylist)
        for i in range(len(data)):
            var = list(data[i])
            var.pop(0)
            for j in range(len(var)):
                newItem = QTableWidgetItem(str(var[j]))
                newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                self.tableWidget.setItem(i, j, newItem)
        #self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(len(mylist)-1, QHeaderView.ResizeToContents)

        self.wf_label.setText("未发提成：%d"%(res_val))
        self.resize(col_line,355)

    def _name_and_pwd(self, name, pwd):
        return self.data._name_pwd(name, pwd)


def main():
    cgitb.enable(format="text")
    app = QApplication(sys.argv)
    win = Qt_Frame()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()