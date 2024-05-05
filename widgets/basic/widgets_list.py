from typing import Optional, TYPE_CHECKING

from PySide6.QtWidgets import (
    QListWidget, QListWidgetItem, QFrame,
    QHBoxLayout, QLabel
)
from PySide6.QtCore import Qt

from src.core import Loader

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class WidgetsList(QFrame):
    def __init__(
            self, 
            __parent: Optional["QWidget"] = None, 
            size: tuple[int, int] = (600, 400),
            title: Optional[str] = None,
            stylesheet: Optional[str] = None
    ) -> None:
        super().__init__(__parent)

        self.mainLayout = QHBoxLayout()
        self.listWidget = QListWidget()

        self.setStyleSheet(Loader.load_file("./widgets/basic/styles/widgets_list.css"))
        self.setObjectName("widget-list")
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        if stylesheet is not None:
            self.setStyleSheet(self.styleSheet() + stylesheet)

    def add_widget(self, widget) -> None:
        item = QListWidgetItem()
        item.setSizeHint(widget.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, widget)