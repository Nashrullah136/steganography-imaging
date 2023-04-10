import typing
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .TitleLabel import TitleLabel


class ChooseImage(QWidget):
    def __init__(self, parent: typing.Optional['QWidget'] = None, title: str = None, 
                 file_type: str = "*.bmp", mandatory: bool = False) -> None:
        super().__init__(parent)
        self.image = ""
        self.mandatory = mandatory
        self.file_type = file_type
        self.main_layout = QVBoxLayout()
        self.title_label = TitleLabel(title=title)
        self.main_layout.addWidget(self.title_label)
        self.image_directory_status = False
        self.all_button = self.button_ui()
        self.main_layout.addLayout(self.all_button)
        self.setLayout(self.main_layout)

    def button_ui(self) -> QLayout:
        layout = QHBoxLayout()
        choose_button = QPushButton("Choose Image")
        choose_button.clicked.connect(self.choose_image)
        layout.addWidget(choose_button)
        preview_button = QPushButton("Preview Image")
        preview_button.clicked.connect(self.preview_image)
        layout.addWidget(preview_button)
        layout.addStretch()
        return layout

    def choose_image(self) -> None:
        file_dialog = QFileDialog(self.parent())
        filename = file_dialog.getOpenFileName(
            self, "Choose Image", 'C:', f'Image File ({self.file_type})')[0]
        if filename:
            if not self.image_directory_status:
                self.image_directory = QLabel()
                self.image_directory.setWordWrap(True)
                self.main_layout.insertWidget(1, self.image_directory)
                self.image_directory_status = True
            self.image_directory.setText(filename)
            self.image = filename

    def preview_image(self) -> None:
        dialog = QDialog(self)
        image = QLabel(dialog)
        image.setPixmap(QPixmap(self.get_image()).scaled(
            400, 400, Qt.AspectRatioMode.KeepAspectRatio))
        image.adjustSize()
        dialog.exec_()

    def get_image(self) -> str:
        if self.mandatory and not self.image:
            raise ValueError(f'{self.title_label.text()} is mandatory!')
        return self.image
