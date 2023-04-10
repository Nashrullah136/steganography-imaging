from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import typing
import numpy as np

class WorkerSignal(QObject):
    finished = pyqtSignal(str)
    progress = pyqtSignal()
    error = pyqtSignal(str)
    def __init__(self, parent: typing.Optional['QObject'] = None) -> None:
        super().__init__(parent)