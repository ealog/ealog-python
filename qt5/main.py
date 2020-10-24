#coding: utf-8

import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc
import serialui
from tool import Tool


class myMainWindow(qw.QMainWindow,serialui.Ui_MainWindow):
    signal_recv_data = qc.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #初始化窗口
        self.statusbar.showMessage("Status:OK")

        #加载配置文件
        self.settings = qc.QSettings("config.ini",qc.QSettings.IniFormat)
        self.settings.setIniCodec("UTF-8")
        self.config_uart_baud = self.settings.value("SETUP/UART_BAUD",0,type=int)
        print("Uart baud(int) %d "% self.config_uart_baud)
        self.uart_port = "/dev/pts/3"

        #初始化界面
        self.radioButton_recv_ascii.setChecked(True)
        self.radioButton_send_ascii.setChecked(True)
        self.spinBox.setRange(100,30000)
        self.spinBox.setValue(1000)
        self.spinBox.setSingleStep(100)
        self.spinBox.setWrapping(True)

        self.comboBox_baud.setCurrentText(str(self.config_uart_baud))


        #绑定信号与槽
        self.comboBox_baud.currentIndexChanged.connect(self.comboBox_baud_cb)
        self.btn_send.clicked.connect(self.btn_send_cb)
        self.actionStart.triggered.connect(self.actionStart_cb)
        self.actionPause.triggered.connect(self.actionPause_cb)
        self.actionStop.triggered.connect(self.actionStop_cb)
        self.actionClear.triggered.connect(self.actionClear_cb)
        self.radioButton_recv_ascii.toggled.connect(self.radioButton_recv_ascii_cb)
        self.radioButton_send_ascii.toggled.connect(self.radioButton_send_ascii_cb)
        self.radioButton_recv_hex.toggled.connect(self.radioButton_recv_hex_cb)
        self.radioButton_send_hex.toggled.connect(self.radioButton_send_hex_cb)
        self.checkBox_wrap.toggled.connect(self.checkBox_wrap_cb)
        self.checkBox_show_send.toggled.connect(self.checkBox_show_send_cb)
        self.checkBox_show_time.toggled.connect(self.checkBox_show_time_cb)
        self.checkBox_repeat_send.toggled.connect(self.checkBox_repeat_send_cb)
        self.spinBox.valueChanged.connect(self.spinBox_cb)

        # 自定义信号

        self.signal_recv_data.connect(self.textBrowser_show_data_cb)
 

        # 实例化Tool

        self.tool = Tool(self)

    def textBrowser_show_data_cb(self,data):
        # print("signal data is %s" % data)

        self.textBrowser.insertPlainText(data)
        cursor = self.textBrowser.textCursor().End
        self.textBrowser.moveCursor(cursor)

 



    def comboBox_baud_cb(self):
        content = self.comboBox_baud.currentText()
        print("Combox's value is ,",content)
        text = "Your choice %s" % content
        qw.QMessageBox.information(self,"Notice",text,qw.QMessageBox.Ok | qw.QMessageBox.Cancel)

    def btn_send_cb(self):
        print("Your clicked Send Button!")
        send_data = self.textEdit_get.toPlainText()
        self.tool.uart.send_uart_data(send_data)

        # # text = self.textEdit_get.toPlainText()
        # # print("Text value is ,",text)

        # # #增加Combox_uart的选项，选项指的是COM口实例。
        # # self.comboBox_uart.addItem(text)

        # # 测试Qsettings写入功能
        # uart_baud = self.comboBox_baud.currentText()
        # print("Current uart baud is ",uart_baud)
        # self.settings.setValue("SETUP/UART_BAUD",int(uart_baud))

    def actionStart_cb(self):
        print("You clicked actionStart.")

    def actionPause_cb(self):
        print("You clicked actionPause.")

    def actionStop_cb(self):
        print("You clicked actionStop.")

    def actionClear_cb(self):
        print("You clicked actionClear.")

    def radioButton_recv_ascii_cb(self):
        print("You select radioButton_recv_ascii.")
    
    def radioButton_recv_hex_cb(self):
        print("You select radioButton_recv_hex.")

    def radioButton_send_ascii_cb(self):
        print("You select radioButton_send_ascii.")

    def radioButton_send_hex_cb(self):
        print("You select radioButton_send_hex.")

    def checkBox_wrap_cb(self):
        print("You selected checkBox_wrap.")
        
        res_wrap = self.checkBox_wrap.isChecked()
        print("res_wrap is ",res_wrap)
        res_show_send = self.checkBox_show_send.isChecked()
        print("res_show_send is ",res_show_send)
        res_show_time = self.checkBox_show_time.isChecked()
        print("res_show_time is ",res_show_time)
        res_repeat_send = self.checkBox_repeat_send.isChecked()
        print("res_repeat_send is ",res_repeat_send)



    def checkBox_show_send_cb(self):
        print("You selected checkBox_show_send.")

    def checkBox_show_time_cb(self):
        print("You selected checkBox_show_time.")

    def checkBox_repeat_send_cb(self):
        print("You selected checkBox_repeat_send.")        

    def spinBox_cb(self,value):
        print("Current value is %d" %value)

if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    w = myMainWindow()
    w.show()
    sys.exit(app.exec_())


