import typing
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ...component.ChooseImage import ChooseImage
from ...component.ChooseAssembler import ChooseAssembler
from ...component.ChooseEncodeMethod import ChooseEncodeMethod
from ...component.ChooseSteganoMethod import ChooseSteganoMethod
from ...component.ChooseFolderDestination import ChooseFolderDestination
from ....image.insertor import Insertor
import os
from ....helper.Navigation import Navigation
from ...component.ErrorMessageBox import ErrorMessageBox
from ...component.LongTask import LongTask

#TODO: Add Progress Bar

class InsertForm(QWidget):
    def __init__(self, parent: typing.Optional['QWidget'] = None, nav: Navigation = None) -> None:
        super(InsertForm, self).__init__(parent)
        self.navigation = nav
        self.main_layout = QVBoxLayout()
        self.choose_secret_image = ChooseImage(self, "Secret Image", "*.bmp *.png *.jpg", mandatory=True)
        self.main_layout.addWidget(self.choose_secret_image)
        self.choose_vessel_image = ChooseImage(self, "Vessel Image", mandatory=True)
        self.main_layout.addWidget(self.choose_vessel_image)
        self.choose_assembler = ChooseAssembler(self)
        self.main_layout.addWidget(self.choose_assembler)
        self.choose_encoder = ChooseEncodeMethod(self)
        self.main_layout.addWidget(self.choose_encoder, 2)
        self.choose_stegano_method = ChooseSteganoMethod(self)
        self.main_layout.addWidget(self.choose_stegano_method)
        self.choose_folder_destination = ChooseFolderDestination(self, mandatory=True)
        self.main_layout.addWidget(self.choose_folder_destination)
        self.buttons = self.create_buttons()
        self.main_layout.addLayout(self.buttons)
        self.setLayout(self.main_layout)
        self.main_thread = LongTask("Inserting Message...", self)      
        self.main_thread.signals.finished.connect(os.startfile)

    def create_buttons(self) -> QBoxLayout:
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        execute_button = QPushButton("Execute")
        execute_button.clicked.connect(self.execute)
        button_layout.addWidget(execute_button, alignment=Qt.AlignmentFlag.AlignCenter)
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.back)
        button_layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignCenter)
        button_layout.addStretch()
        return button_layout

    def back(self) -> None:
        if self.navigation:
            self.navigation.back()

    def execute(self) -> None:
        try:
            self.get_inputs()
        except ValueError as err:
            ErrorMessageBox(str(err), self).show()
            return
        self.insertor = Insertor(self.vessel_image, self.secret_image, self.assembler,
                                 self.stegano_method, self.folder_destination, self.encoders)
        self.main_thread.set_worker(self.insertor)
        self.main_thread.start()

    def get_inputs(self) -> None:
        self.secret_image = self.choose_secret_image.get_image()
        self.vessel_image = self.choose_vessel_image.get_image()
        self.assembler = self.choose_assembler.get_assembler()
        self.encoders = self.choose_encoder.get_encoder()
        self.stegano_method = self.choose_stegano_method.get_stegano_method()
        self.folder_destination = self.choose_folder_destination.get_folder()