from PySide6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QLabel
)
from PySide6.QtCore import Qt

import sys

from widgets import PushButton, WidgetsList


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.resize(1000, 600)
        self.setStyleSheet("background-color: #fbfbfb")

        self.widgetsList = WidgetsList()
        self.widgetsList.addItem("Breakfast")
        self.widgetsList.addItem("Breakfast")
        self.widgetsList.addItem("Breakfast")
        # self.widgetsList.add_widget(QLabel("Breakfast"))


        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.widgetsList)
        self.mainLayout.addWidget(PushButton(text="Button"), alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
