from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize

from src.core import Loader

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class PushButton(QPushButton):
    def __init__(
            self, 
            text: Optional[str] = None,
            size: tuple[int, int] = (100, 25),
            stylesheet: Optional[str] = None,
            *,
            parent: Optional["QWidget"] = None, 
    ) -> None:
        super().__init__(parent)

        self.setStyleSheet(Loader.load_file("./widgets/basic/styles/push_button.css"))
        self.setMinimumSize(QSize(*size))

        if text is not None:
            self.setText(text)
        
        if stylesheet is not None:
            self.setStyleSheet(self.styleSheet() + stylesheet)