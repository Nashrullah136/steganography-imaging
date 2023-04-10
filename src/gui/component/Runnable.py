from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import typing
from .WorkerSignal import WorkerSignal

class Runnable(QRunnable):
    def __init__(self):
        super().__init__()
    def number_of_progress(self) -> int:
        pass
    def stop(self) -> None:
        pass
    def set_signal(self, signals: WorkerSignal) -> None:
        pass
