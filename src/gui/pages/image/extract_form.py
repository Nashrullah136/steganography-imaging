import typing
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ...component.ChooseImage import ChooseImage
from ...component.ChooseAssembler import ChooseAssembler
from ...component.ChooseEncodeMethod import ChooseEncodeMethod
from ...component.ChooseSteganoMethod import ChooseSteganoMethod
from ...component.ChooseFolderDestination import ChooseFolderDestination
from ....image.extractor import Extractor
from ....helper.Navigation import Navigation
from ...component.ErrorMessageBox import ErrorMessageBox
from ...component.LongTask import LongTask
import os

class ExtractForm(QWidget):
    def __init__(self, parent: typing.Optional['QWidget'] = None, nav: Navigation = None) -> None:
        super(ExtractForm, self).__init__(parent)
        self.navigation = nav
        self.main_layout = QVBoxLayout(self)
        self.choose_vessel_image = ChooseImage(self, "Vessel Image", mandatory=True)
        self.main_layout.addWidget(self.choose_vessel_image)
        self.choose_assembler = ChooseAssembler(self)
        self.main_layout.addWidget(self.choose_assembler)
        self.choose_decoder = ChooseEncodeMethod(self)
        self.main_layout.addWidget(self.choose_decoder, 1)
        self.choose_stegano_method = ChooseSteganoMethod(self)
        self.main_layout.addWidget(self.choose_stegano_method)
        self.choose_folder_destination = ChooseFolderDestination(self, mandatory=True)
        self.main_layout.addWidget(self.choose_folder_destination)
        self.buttons = self.create_buttons()
        self.main_layout.addLayout(self.buttons)
        self.setLayout(self.main_layout)
        self.main_thread = LongTask("Extracting Message...", self)      
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
        self.extractor = self.create_extractor()
        self.main_thread.set_worker(self.extractor)
        self.main_thread.start()

    def get_inputs(self) -> None:
        self.vessel_image = self.choose_vessel_image.get_image()
        self.assembler = self.choose_assembler.get_assembler()
        self.decoders = self.choose_decoder.get_encoder()
        self.stegano_method = self.choose_stegano_method.get_stegano_method()
        self.folder_destination = self.choose_folder_destination.get_folder()

    def create_extractor(self) -> Extractor:
        #TODO: maybe create extractor factory?
        extractor = Extractor()
        extractor.set_vessel_file(self.vessel_image)
        extractor.set_assembler(self.assembler)
        for decoder in self.decoders:
            extractor.add_encoder(decoder)
        extractor.set_stegano_method(self.stegano_method)
        extractor.set_folder(self.folder_destination)
        return extractor