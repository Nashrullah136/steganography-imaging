import typing
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .CompressionDialog import CompressionDialog
from .CryptographDialog import CryptographDialog
from .TitleLabel import TitleLabel
from ...encoder.Encoder import Encoder
from .ErrorMessageBox import ErrorMessageBox

class ChooseEncodeMethod(QWidget):
    def __init__(self, parent: typing.Optional['QWidget'] = None) -> None:
        super().__init__(parent)
        self.encoder: list[Encoder] = []
        self.main_layout = QVBoxLayout()
        self.title = TitleLabel(title="Encode Method")
        self.main_layout.addWidget(self.title)
        self.table_layout = self.table_ui()
        self.all_button = self.controll_button_ui()
        self.table_layout.addLayout(self.all_button)
        self.main_layout.addLayout(self.table_layout)
        self.setLayout(self.main_layout)

    def get_encoder(self):
        return self.encoder

    def table_ui(self) -> QBoxLayout:
        layout = QHBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Operation", "Additional Info"])
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        layout.addWidget(self.table)
        return layout

    def controll_button_ui(self) -> QLayout:
        layout = QVBoxLayout()
        compression_button = QPushButton("Add Compression")
        compression_button.clicked.connect(self.add_compression)
        crypthograph_button = QPushButton("Add Cryptograph")
        crypthograph_button.clicked.connect(self.add_cryptograph)
        remove_button = QPushButton("Remove Item")
        remove_button.clicked.connect(self.remove_row)
        layout.addWidget(compression_button)
        layout.addWidget(crypthograph_button)
        layout.addWidget(remove_button)
        layout.addStretch()
        return layout
    
    def remove_row(self) -> None:
        removed_row = [index.row() for index in self.table.selectedIndexes()]
        removed_row.sort(reverse=True)
        for row in removed_row:
            self.table.removeRow(row)
            self.encoder.pop(row)

    def add_compression(self) -> None:
        compression_dialog = CompressionDialog(self)
        text, compression = compression_dialog.get_result()
        if text and compression:
            insert_to = self.table.rowCount()
            self.table.setRowCount(self.table.rowCount()+1)
            self.table.setItem(insert_to, 0, QTableWidgetItem(text))
            self.encoder.append(compression)

    def add_cryptograph(self) -> None:
        cryptograph_dialog = CryptographDialog(self)
        try:
            text, key, cryptograph = cryptograph_dialog.get_result()
        except ValueError as err:
            ErrorMessageBox(str(err), self).show()
            return
        if text and cryptograph:
            insert_to = self.table.rowCount()
            self.table.setRowCount(self.table.rowCount()+1)
            self.table.setItem(insert_to, 0, QTableWidgetItem(text))
            self.table.setItem(insert_to, 1, QTableWidgetItem(f'key={key}'))
            self.encoder.append(cryptograph)