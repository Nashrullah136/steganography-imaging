import typing
import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from src.encoder.compression.CompressionList import CompressionList
from src.encoder.Encoder import Encoder
from .dialog_compression import Ui_Dialog

class CompressionDialog(QDialog):
    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super(CompressionDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.add_compressions(self.ui.compression_combobox)

    def add_compressions(self, combo_box: QComboBox) -> None:
        compressions = CompressionList().get_compressions()
        for compression in compressions:
            combo_box.addItem(*compression)

    def get_result(self) -> typing.Tuple[str, Encoder]:
        if self.exec_():
            encoder : Encoder = self.ui.compression_combobox.currentData()
            text = self.ui.compression_combobox.currentText()
            return text, encoder
        else:
            return None, None