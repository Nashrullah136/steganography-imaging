import typing
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class TitleLabel(QLabel):
    def __init__(self, parent: typing.Optional['QWidget'] = None, title: str = None) -> None:
        super(TitleLabel, self).__init__(title, parent)
        self.custom_font = QFont()
        self.custom_font.setBold(True)
        self.setFont(self.custom_font)
