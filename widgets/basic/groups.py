from typing import Optional, TYPE_CHECKING

from PySide6.QtWidgets import (
    QGroupBox, QButtonGroup
)

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class GroupBox(QGroupBox):
    def __init__(
            self,
            title: Optional[str] = None,
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        if title is not None: self.setTitle(title)
