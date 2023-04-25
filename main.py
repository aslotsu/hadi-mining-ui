import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from ui_hadi import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.information.setChecked(True)
        self.ui.rpc_menu_1_1.hide()
        self.ui.rpg_side_menu.hide()

        # page changing methods
        self.ui.information.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.info_small.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.rpc.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.rpc_small.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.rpg.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.rpg_small.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.rrg.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.rrg_small.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.results.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.result_small.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))

        # rpc page changers
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.rpc_stack.setCurrentIndex(0))
        self.ui.pushButton_11.clicked.connect(lambda: self.ui.rpc_stack.setCurrentIndex(1))
        self.ui.pushButton_12.clicked.connect(lambda: self.ui.rpc_stack.setCurrentIndex(2))
        self.ui.pushButton_10.clicked.connect(lambda: self.ui.rpc_stack.setCurrentIndex(3))
        self.ui.pushButton_8.clicked.connect(lambda: self.ui.rpc_stack.setCurrentIndex(4))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.rpc_stack.setCurrentIndex(5))
        self.ui.pushButton.clicked.connect(lambda: self.ui.rpc_stack.setCurrentIndex(6))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.rpc_stack.setCurrentIndex(7))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.rpc_stack.setCurrentIndex(8))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.rpc_stack.setCurrentIndex(9))

        # rpg page changers
        self.ui.pushButton_17.clicked.connect(lambda: self.ui.rpg_stack.setCurrentIndex(0))
        self.ui.pushButton_15.clicked.connect(lambda: self.ui.rpg_stack.setCurrentIndex(1))
        self.ui.pushButton_18.clicked.connect(lambda: self.ui.rpg_stack.setCurrentIndex(2))
        self.ui.pushButton_21.clicked.connect(lambda: self.ui.rpg_stack.setCurrentIndex(3))
        self.ui.pushButton_22.clicked.connect(lambda: self.ui.rpg_stack.setCurrentIndex(4))
        self.ui.pushButton_24.clicked.connect(lambda: self.ui.rpg_stack.setCurrentIndex(5))
        self.ui.pushButton_25.clicked.connect(lambda: self.ui.rpg_stack.setCurrentIndex(6))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss", "r") as style_file:
        style_str = style_file.read()

    app.setStyleSheet(style_str)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
