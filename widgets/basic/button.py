from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize

from src.core import Loader

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget
    from PySide6.QtGui import QFont


class PushButton(QPushButton):
    def __init__(
            self, 
            text: Optional[str] = None,
            size: tuple[int, int] = (100, 25),
            font: Optional["QFont"] = None, 
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None, 
    ) -> None:
        super().__init__(parent)

        if font is not None: self.setFont(font)

        if stylesheet is not None:
            self.setStyleSheet(
                Loader.load_file("./widgets/basic/styles/button.css") + stylesheet
            )
        else:
            self.setStyleSheet(Loader.load_file("./widgets/basic/styles/button.css")) # ./widgets/basic/styles/push_button.css
        
        self.setObjectName("button")
        self.setMinimumSize(QSize(*size))

        if text is not None:
            self.setText(text)
        
        if stylesheet is not None:
            self.setStyleSheet(self.styleSheet() + stylesheet)
