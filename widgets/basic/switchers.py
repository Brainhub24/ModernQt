import os.path

from PySide6.QtWidgets import (
    QSplitter, QComboBox, QSpinBox, 
    QLineEdit, QWidget, QHBoxLayout, 
    QSpacerItem, QSizePolicy, QCheckBox,
    QRadioButton
)
from PySide6.QtCore import Qt, QSize

from src.core import Loader, FileDialog, Font

from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from PySide6.QtGui import QFont

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

        self.setObjectName("splitter")

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
            size: tuple[int, int] = (200, 30),
            font: Optional["QFont"] = None, 
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        self.setFixedSize(QSize(*size))
        self.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.__values = []

        if values is not None: self.__values = [*values]
        self.addItems(self.__values)
        self.setObjectName("drop-down-menu")
        if font is not None: self.setFont(font)

        if stylesheet is not None:
            self.setStyleSheet(
                Loader.load_file("./widgets/basic/styles/drop_down_menu.css") + "\n" 
                + stylesheet.replace("DropDownMenu", "QComboBox#drop-down-menu")
            )
        else:
            self.setStyleSheet(Loader.load_file("./widgets/basic/styles/drop_down_menu.css"))

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
            size: tuple[int, int] = (200, 30), 
            font: Optional["QFont"] = None, 
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        if placed is not None: self.setText(placed)
        if placeholder is not None: self.setPlaceholderText(placeholder)
        if font is not None: self.setFont(font)

        self.setFixedSize(QSize(*size))
        self.setObjectName("entry")
        self.setFocusPolicy(Qt.FocusPolicy.WheelFocus)

        if stylesheet is not None:
            self.setStyleSheet(
                Loader.load_file("./widgets/basic/styles/entry.css") + "\n" 
                + stylesheet.replace("Entry", "QLineEdit#entry")
            )
        else:
            self.setStyleSheet(Loader.load_file("./widgets/basic/styles/entry.css"))


class DigitalEntry(QSpinBox):
    """
    Custom QSpinBox widget for entering digital values.

    Methods:
    - __init__(__range: tuple[int, int], width: int = 30, height: int = 25, show_buttons: bool = False): None - Initializes the digital entry with a specified range, width, height, and button display.
    """

    def __init__(
            self, 
            range: tuple[int, int] = (0, 100), 
            size: tuple[int, int] = (40, 30), 
            font: Optional["QFont"] = None, 
            include_buttons: bool = False,
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        self.setFixedSize(QSize(*size))
        if not include_buttons: self.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        if font is not None: self.setFont(font)

        self.setObjectName("digital-entry")
        self.setRange(*range)

        if stylesheet is not None:
            self.setStyleSheet(
                Loader.load_file("./widgets/basic/styles/digital_entry.css") + "\n" 
                + stylesheet.replace("DigitalEntry", "QSpinBox#digital-entry")
            )
        else:
            self.setStyleSheet(Loader.load_file("./widgets/basic/styles/digital_entry.css"))


class CheckBox(QCheckBox):
    def __init__(
            self,
            text: Optional[str] = None,
            size: tuple[int, int] = (150, 30),
            is_checkable: bool = True,
            is_checked: bool = False,
            is_disabled: bool = False,
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        self.setFixedSize(QSize(*size))
        self.setChecked(is_checked)
        self.setCheckable(is_checkable)
        self.setDisabled(is_disabled)

        self.setObjectName("check-box")
        if text is not None:
            self.setText(text)
        
        if stylesheet is not None:
            self.setStyleSheet(
                Loader.load_file("./widgets/basic/styles/check_box.css") + "\n" 
                + stylesheet.replace("CheckBox", "QCheckBox#check-box")
            )
        else:
            self.setStyleSheet(Loader.load_file("./widgets/basic/styles/check_box.css"))


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
            size: tuple[int, int] = (200, 30), 
            font: Optional["QFont"] = None, 
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        self.setObjectName("path-entry")
        if font is not None: self.setFont(font)
        
        if stylesheet is not None:
            self.setStyleSheet(
                Loader.load_file("./widgets/basic/styles/entry.css") + "\n" 
                + stylesheet.replace("PathEntry", "QLineEdit#path-entry")
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
    

class RadioButton(QRadioButton):
    def __init__(
            self,
            text: Optional[str] = None,
            size: tuple[int, int] = (200, 30),
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        super().__init__(parent)

        if text is not None: self.setText(text)
        self.setFixedSize(QSize(*size))

        self.setObjectName("radio-button")
        if stylesheet is not None:
            self.setStyleSheet(
                Loader.load_file("./widgets/basic/styles/radio_button.css") + "\n" 
                + stylesheet.replace("RadioButton", "QRaidoButton#radio-button")
            )
        else:
            self.setStyleSheet(Loader.load_file("./widgets/basic/styles/radio_button.css"))
