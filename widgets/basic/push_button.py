from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize

from src.core import Loader

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class PushButton(QPushButton):
    def __init__(
            self, 
            __parent: Optional["QWidget"] = None, 
            text: Optional[str] = None,
            size: tuple[int, int] = (100, 25)
    ) -> None:
        super().__init__(__parent)

        self.setStyleSheet(Loader.load_file("./widgets/basic/styles/push_button.css"))
        self.setMinimumSize(QSize(*size))

        if text is not None:
            self.setText(text)
