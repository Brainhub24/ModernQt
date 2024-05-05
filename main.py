from PySide6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QLabel
)
from PySide6.QtCore import Qt

import sys

from widgets import PushButton, WidgetsList, Entry, DropDownMenu
from src.core import Font


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.resize(1000, 600)
        self.setStyleSheet("background-color: #fbfbfb")

        self.widgetsList = WidgetsList()

        self.mainLayout = QHBoxLayout()
        # self.mainLayout.addWidget(self.widgetsList)
        self.mainLayout.addWidget(Entry())
        self.mainLayout.addWidget(DropDownMenu(["std", "hello", "world"]))
        self.mainLayout.addWidget(PushButton(text="Ok"), alignment=Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(PushButton(text="Cancel"), alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
