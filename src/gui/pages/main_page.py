import typing
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import cv2 as cv
from ...helper.Navigation import Navigation

class MainPage(QWidget):
    def __init__(self, parent: typing.Optional['QWidget'] = None, nav: Navigation = None) -> None:
        super(MainPage, self).__init__(parent)
        self.navigation = nav
        self.main_layout = QVBoxLayout()
        self.main_layout.addStretch()
        self.title = QLabel("Steganograph Imaging")
        self.custom_font = self.create_custom_font()
        self.title.setFont(self.custom_font)
        self.main_layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.insert_form = QPushButton("Insert Form")
        self.insert_form.clicked.connect(self.go_to_insert_form)
        self.main_layout.addWidget(self.insert_form)
        self.extract_form = QPushButton("Extract Form")
        self.extract_form.clicked.connect(self.go_to_extract_form)
        self.main_layout.addWidget(self.extract_form)
        self.main_layout.addStretch()
        self.setLayout(self.main_layout)

    def go_to_insert_form(self) -> None:
        self.navigation.go_to("insert_form")

    def go_to_extract_form(self) -> None:
        self.navigation.go_to("extract_form")

    def create_custom_font(self) -> QFont:
        font = QFont()
        font.setBold(True)
        font.setPointSize(18)
        font.setCapitalization(QFont.Capitalization.AllUppercase)
        return font
        

    
