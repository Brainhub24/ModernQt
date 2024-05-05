import os.path

from PySide6.QtWidgets import (
    QSplitter, QComboBox, QSpinBox, 
    QLineEdit, QWidget, QHBoxLayout, 
    QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt, QSize

from src.core import Loader, FileDialog

from typing import Optional

from widgets.basic.button import PushButton


class Splitter(QSplitter):
    """
    Custom QSplitter widget for managing layout splitting.

    Methods:
    - __init__(__orientation: str, *, parent=None): None - Initializes the splitter with a specified orientation.
    - addWidget(widget): None - Adds a widget to the splitter and sets it as non-collapsible.
    """

    def __init__(
            self, 
            __orientation: str,
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        if __orientation == "horizontal": super().__init__(Qt.Orientation.Horizontal, parent)
        elif __orientation == "vertical": super().__init__(Qt.Orientation.Vertical, parent)

        if stylesheet is not None:
            self.setStyleSheet(
                Loader.load_file("scr/interface/basic/styles/splitter.css") + stylesheet
            )
        else:
            self.setStyleSheet(Loader.load_file("scr/interface/basic/styles/splitter.css"))

    def addWidget(self, widget):
        super().addWidget(widget)
        self.setCollapsible(self.indexOf(widget), False)


class DropDownMenu(QComboBox):
    """
    Custom QComboBox widget for displaying a drop-down menu.

    Methods:
    - __init__(*__values: str, width: int = 200, height: int = 25): None - Initializes the drop-down menu with specified values, width, and height.
    - set_items(*__values: str): None - Sets the items in the drop-down menu.
    """

    def __init__(
            self, 
            values: Optional[list[str]] = None, 
            size: tuple[int, int] = (200, 25),
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        self.setFixedSize(QSize(*size))
        self.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.__values = []

        if values is not None:
            self.__values = [*values]
        self.addItems(self.__values)

        if stylesheet is not None:
            self.setStyleSheet(
                Loader.load_file("scr/interface/basic/styles/splitter.css") + stylesheet
            )
        else:
            self.setStyleSheet(Loader.load_file("scr/interface/basic/styles/splitter.css"))

    def set_items(self, *__values: str) -> None:
        self.__values = [*__values]
        self.addItems(self.__values)


class Entry(QLineEdit):
    """
    Custom QLineEdit widget for text entry.

    Methods:
    - __init__(__placed: str, placeholder: str = "", width: int = 200, height: int = 25): None - Initializes the text entry with default text and placeholder.
    """

    def __init__(
            self, 
            placed: Optional[str] = None, 
            placeholder: Optional[str] = None,
            size: tuple[int, int] = (200, 25), 
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        self.setFixedSize(QSize(*size))
        if placed is not None: self.setText(placed)
        if placeholder is not None: self.setPlaceholderText(placeholder)

        if stylesheet is not None:
            self.setStyleSheet(
                Loader.load_file("scr/interface/basic/styles/splitter.css") + stylesheet
            )
        else:
            self.setStyleSheet(Loader.load_file("scr/interface/basic/styles/splitter.css"))


class DigitalEntry(QSpinBox):
    """
    Custom QSpinBox widget for entering digital values.

    Methods:
    - __init__(__range: tuple[int, int], width: int = 30, height: int = 25, show_buttons: bool = False): None - Initializes the digital entry with a specified range, width, height, and button display.
    """

    def __init__(
            self, 
            range: tuple[int, int] = (0, 100), 
            size: tuple[int, int] = (30, 25), 
            show_buttons: bool = False,
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        self.setFixedSize(QSize(*size))
        if not show_buttons: self.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)

        self.setRange(*range)

        if stylesheet is not None:
            self.setStyleSheet(
                Loader.load_file("scr/interface/basic/styles/splitter.css") + stylesheet
            )
        else:
            self.setStyleSheet(Loader.load_file("scr/interface/basic/styles/splitter.css"))


class PathEntry(QWidget):
    """
    Custom QLineEdit widget for entering path to file and directories.

    Methods:
    - __init__(self, __placed: str, placeholder: str = "", width: int = 400, height: int = 25): None - Initializes the path entry with default text and placeholder.
    - get_entry(self): Entry - returns the Entry widget.
    - set_path(self, __path: str, only_existing: bool = True): None if only_existing is True and path is not exist this path won't be pasted.

    Notes:
    - This widget includes Entry and PushButton to specify the path to your file or directory
    """

    def __init__(
            self, 
            placed: Optional[str] = None, 
            placeholder: Optional[str] = None,
            size: tuple[int, int] = (200, 25), 
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        self.setObjectName("path-entry-widget")
        if stylesheet is not None:
            self.setStyleSheet(
                Loader.load_file("scr/interface/basic/styles/splitter.css") + stylesheet
            )
        else:
            self.setStyleSheet(Loader.load_file("scr/interface/basic/styles/splitter.css"))

        self.mainLayout = QHBoxLayout()

        self.pathEntry = Entry(placed, placeholder, size)

        self.specifyPathBtn = PushButton("...")
        self.specifyPathBtn.clicked.connect(lambda: self.set_path(FileDialog.get_open_file_name()))

        self.mainLayout.addWidget(self.pathEntry)
        self.mainLayout.addWidget(self.specifyPathBtn)
        self.mainLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.setLayout(self.mainLayout)

    def set_path(self, __path: Optional[str] = None, only_existing: bool = True) -> None:
        if __path is None: return

        if only_existing and os.path.exists(__path):
            self.pathEntry.setText(__path)
            return

        self.pathEntry.setText(__path)

    def get_entry(self) -> Entry:
        return self.pathEntry