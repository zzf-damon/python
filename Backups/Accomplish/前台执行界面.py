import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from .Interface import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paqu)
        self.pushButton_2.clicked.connect(self.cunku)
        self.textEdit.setPlaceholderText("在此输入查找关键词")

    def paqu(self):
        keys_word = self.textEdit.toPlainText()
        print(keys_word)

    def cunku(self):
        print("存库按钮被点下")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
