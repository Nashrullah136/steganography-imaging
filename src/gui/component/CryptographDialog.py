import typing
import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from src.encoder.cryptography.CryptographyList import CryptographList
from src.encoder.cryptography.Cryptography import Cryptograph
from src.encoder.Encoder import Encoder
from .dialog_cryptograph import Ui_Cryptograph

class CryptographDialog(QDialog):
    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super(CryptographDialog, self).__init__(parent)
        self.ui = Ui_Cryptograph()
        self.ui.setupUi(self)
        self.add_cryptographs(self.ui.cryptogprah_combobox)

    def add_cryptographs(self, combo_box: QComboBox) -> None:
        cryptographs = CryptographList().get_cryptographs()
        for cryptograph in cryptographs:
            combo_box.addItem(*cryptograph)

    def get_result(self) -> typing.Tuple[str, Encoder]:
        if self.exec_():
            encoder : Cryptograph = self.ui.cryptogprah_combobox.currentData()
            text = self.ui.cryptogprah_combobox.currentText()
            key = self.ui.key.text()
            if not key:
                raise ValueError("Cryptograph key is mandatory")
            encoder.set_key(key)
            return text, key, encoder
        else:
            return None, None, None