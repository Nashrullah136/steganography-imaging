import typing
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ErrorMessageBox(QMessageBox):
    def __init__(self, msg: str, parent: typing.Optional['QWidget'] = None):
        super().__init__(QMessageBox.Icon.Critical, "Error", msg, parent=parent)