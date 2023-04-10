import typing
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .TitleLabel import TitleLabel

class ChooseFolderDestination(QWidget):
    def __init__(self, parent: typing.Optional['QWidget'] = None, mandatory: bool = False) -> None:
        super().__init__(parent)
        self.mandatory = mandatory
        self.folder = ""
        self.main_layout = QVBoxLayout()
        self.title = TitleLabel(title="Folder Destination")
        self.main_layout.addWidget(self.title)
        self.folder_status = False
        self.choose_button = QPushButton("Choose Folder")
        self.choose_button.clicked.connect(self.choose_image)
        self.main_layout.addWidget(self.choose_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.setLayout(self.main_layout)

    def choose_image(self) -> None:
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        if not self.folder_status and folder:
            self.folder_label = QLabel()
            self.folder_label.setWordWrap(True)
            self.main_layout.insertWidget(1, self.folder_label)
            self.folder_status = True
        self.folder = folder
        self.folder_label.setText(self.folder)

    def get_folder(self) -> str:
        if self.mandatory and not self.folder:
            raise ValueError(f"{self.title.text()} is mandatory!")
        return self.folder
