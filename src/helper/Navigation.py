import typing
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import cv2 as cv
import time

class Navigation(QStackedWidget):
    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super(Navigation, self).__init__(parent)
        self.history = list()
        self.list_page = dict()

    def addWidget(self, name: str, w: QWidget) -> int:
        if name not in self.list_page:
            self.list_page[name] = w
            return super().addWidget(w)
        else:
            print("Name already exist!")
            return -1

    def back(self) -> None:
        if self.history:
            self.setCurrentWidget(self.history.pop())
    
    def go_to(self, name: str) -> None:
        if name in self.list_page:
            self.history.append(self.currentWidget())
            widget = self.list_page.get(name)
            self.setCurrentWidget(widget)

    def get_pages(self) -> list[str]:
        return list(self.list_page.keys())