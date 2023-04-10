import typing
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtTest import QTest

class ProgressDialog(QProgressDialog):
    def __init__(self, label: str, max: int, parent: typing.Optional['QWidget'] = None) -> None:
        self.__init__(label, parent)
        self.setMaximum(max)

    def __init__(self, label: str, parent: typing.Optional['QWidget'] = None) -> None:
        super(ProgressDialog, self).__init__(parent)
        self.label = label
        self.setLabelText(label)
        self.setMinimum(0)
        self.cancel_procedure = None
        self.setAutoClose(True)
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.cancelButton: QPushButton = self.findChild(QPushButton)
        self.canceled.disconnect()
        self.canceled.connect(self.cancel)

    def show(self) -> None:
        self.setLabelText(self.label)
        self.cancelButton.setEnabled(True)
        self.setValue(0)
        return super().show()

    def set_cancel_procedure(self, procedure: typing.Callable[[], None]) -> None:
        self.cancel_procedure = procedure

    def closeEvent(self, a0: QCloseEvent) -> None:
        if a0.spontaneous():
            self.cancel()
            a0.accept()
        else:
            super().closeEvent(a0)

    def cancel(self) -> None:
        self.cancelButton.setEnabled(False)
        self.setLabelText("Cancelling...")
        QTest.qWait(100)
        if self.cancel_procedure != None:
            self.cancel_procedure()
        self.reset()
        return super().cancel()