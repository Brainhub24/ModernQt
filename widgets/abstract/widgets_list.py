from typing import Optional, TYPE_CHECKING

from PySide6.QtWidgets import QListWidget, QListWidgetItem

from src.core import Loader

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class WidgetsList(QListWidget):
    def __init__(
            self, 
            __parent: Optional["QWidget"] = None, 
            size: tuple[int, int] = (600, 400)
    ) -> None:
        super().__init__()

        self.setStyleSheet(Loader.load_file("./widgets/abstract/styles/widgets_list.css"))
        self.setSpacing(5)

    def add_widget(self, widget) -> None:
        item = QListWidgetItem()
        item.setSizeHint(widget.sizeHint())
        self.addItem(item)
        self.setItemWidget(item, widget)