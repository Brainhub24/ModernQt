from PySide6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QLabel
)
from PySide6.QtCore import Qt

import sys

from widgets import PushButton, WidgetsList, Entry
from src.core import Font


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.resize(1000, 600)
        self.setStyleSheet("background-color: #fbfbfb")

        self.widgetsList = WidgetsList()

        Font.get_system_font("hello", 10)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.widgetsList)
        self.mainLayout.addWidget(Entry())
        self.mainLayout.addWidget(PushButton(text="Ok"), alignment=Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(PushButton(text="Cancel"), alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
