import typing
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from src.stegano_method.SteganoMethodList import SteganoMethodList
from .TitleLabel import TitleLabel
from ...stegano_method.SteganoMethod import SteganoMethod

class ChooseSteganoMethod(QWidget):
    def __init__(self, parent: typing.Optional['QWidget'] = None) -> None:
        super().__init__(parent)
        self.main_layout = QVBoxLayout()
        self.title = TitleLabel(title="Steganography")
        self.main_layout.addWidget(self.title)
        self.horizontal_layout = QHBoxLayout()
        self.method_widget = self.method_ui()
        self.horizontal_layout.addWidget(self.method_widget, 1)
        self.all_parameter_ui = self.generate_parameter_ui()
        self.last_index = 0
        self.horizontal_layout.addWidget(self.all_parameter_ui, 1)
        self.main_layout.addLayout(self.horizontal_layout, 1)
        self.setLayout(self.main_layout)

    def method_ui(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout()
        title = QLabel("Method")
        title.adjustSize()
        layout.addWidget(title)
        self.combo_box = self.combo_box_ui()
        layout.addWidget(self.combo_box)
        widget.setLayout(layout)
        return widget

    def combo_box_ui(self) -> QComboBox:
        combo_box = QComboBox()
        stegano_methods = SteganoMethodList().get_stegano_methods()
        for stegano in stegano_methods:
            combo_box.addItem(stegano['name'], stegano['stegano_method'])
        combo_box.currentIndexChanged.connect(self.on_indexChanged)
        return combo_box

    def generate_parameter_ui(self) -> QStackedWidget:
        parameter_ui = QStackedWidget()
        stegano_methods = SteganoMethodList().get_stegano_methods()
        for pam in stegano_methods:
            parameter_ui.addWidget(self.create_parameter_ui(pam['label'], pam['bottom'], 
                                                   pam['top'], pam['singleStep']))
        return parameter_ui

    def create_parameter_ui(self, label: str, bottom: float, top: float, step: float) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout()
        title = QLabel(text=label)
        layout.addWidget(title)
        spinBox = QDoubleSpinBox()
        spinBox.setRange(bottom, top)
        spinBox.setSingleStep(step)
        layout.addWidget(spinBox)
        layout.addStretch()
        widget.setLayout(layout)
        return widget

    def on_indexChanged(self) -> None:
        index = self.combo_box.currentIndex()
        self.all_parameter_ui.setCurrentIndex(index)

    def get_stegano_method(self) -> SteganoMethod:
        stegano_method_type = self.combo_box.currentData()
        parameter_widget : QDoubleSpinBox = self.all_parameter_ui.currentWidget().findChild(QDoubleSpinBox)
        stegano_method = stegano_method_type(parameter_widget.value())
        return stegano_method