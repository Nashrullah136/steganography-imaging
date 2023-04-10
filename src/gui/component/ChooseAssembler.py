import typing
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ...assembler.AssemblerList import AssemblerList
from .TitleLabel import TitleLabel


class ChooseAssembler(QWidget):
    def __init__(self, parent: typing.Optional['QWidget'] = None, mandatory: bool = False) -> None:
        super().__init__(parent)
        self.mandatory = mandatory
        self.form_layout = QVBoxLayout()
        self.file_op = TitleLabel(title="File Opening")
        self.combo_box = self.create_combobox()
        self.form_layout.addWidget(self.file_op)
        self.form_layout.addWidget(self.combo_box)
        self.setLayout(self.form_layout)

    def create_combobox(self) -> QComboBox:
        combo_box = QComboBox()
        assembler_list = AssemblerList().get_assemblers()
        for name, assembler in assembler_list:
            combo_box.addItem(name, assembler)
        return combo_box

    def get_assembler(self) -> str:
        if self.mandatory and self.combo_box.currentData():
            raise ValueError("File opening is mandatory!")
        return self.combo_box.currentData()
