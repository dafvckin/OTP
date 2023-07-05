import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import openai

openai.api_key = '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'


def generate_response(input_text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=input_text,
        max_tokens=300,
        temperature=0.7,
        n=1,
        stop=None,
        echo=False
    )

    if 'choices' in response:
        choices = response['choices']
        if choices and 'text' in choices[0]:
            return choices[0]['text'].strip()

    return "I'm sorry, I don't have a response at the moment."


currdir = os.getcwd()


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(637, 481)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.forma_gpt = QtWidgets.QLabel(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap((QtGui.QPixmap(os.path.join(currdir, 'ico', "icons8-chatgpt-100.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.forma_gpt.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.forma_gpt.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.forma_gpt.setText("")
        self.forma_gpt.setObjectName("forma_gpt")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 400, 637, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border: 2px solid red;\n"
                                    "font: 75 9pt \"MS Shell Dlg 2\";\n"
                                    "background-color: black;\n"
                                    "color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.text_gpt = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_gpt.setGeometry(QtCore.QRect(0, 0, 641, 400))
        self.text_gpt.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "color: rgb(170, 255, 127);")
        self.text_gpt.setObjectName("text_gpt")
        self.do_resp_bt = QtWidgets.QPushButton(self.centralwidget)
        self.do_resp_bt.setGeometry(QtCore.QRect(585, 370, 51, 29))
        self.do_resp_bt.setStyleSheet("background-color: rgb(0, 255, 127);\n"
                                      "color: rgb(255, 255, 255);")
        self.do_resp_bt.setObjectName("do_resp_bt")
        self.exit_resp = QtWidgets.QPushButton(self.centralwidget)
        self.exit_resp.setGeometry(QtCore.QRect(585, 340, 51, 29))
        self.exit_resp.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                     "color: rgb(255, 255, 255);")
        self.exit_resp.setObjectName("exit_resp")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("GPT", "GPT"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:72; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_gpt.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">It`s ChatGPT Helper! Text Me your Question.</span></p></body></html>"))
        self.do_resp_bt.setText(_translate("MainWindow", ">"))
        self.exit_resp.setText(_translate("MainWindow", "X"))
        self.do_resp_bt.clicked.connect(self.alclickedD)
        self.exit_resp.clicked.connect(self.alclickedE)

    def alclickedD(self):
        text = self.textEdit.toPlainText()
        b = generate_response(text)
        self.text_gpt.setText(b)

    def alclickedE(self):
        MainWindow.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
