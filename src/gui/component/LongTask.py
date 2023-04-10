import typing
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .ProgressDialog import ProgressDialog
from .Runnable import Runnable
import numpy as np
from .WorkerSignal import WorkerSignal
from .ErrorMessageBox import ErrorMessageBox

class LongTask(QThreadPool):
    def __init__(self, label: str, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.label = label
        self.signals = WorkerSignal()
        self.signals.progress.connect(self.update_progress)
        self.signals.error.connect(self.error_worker)

    def set_worker(self, worker: Runnable):
        self.worker = worker
        self.worker.set_signal(self.signals)

    def cancel_procedure(self):
        self.worker.stop()
        # self.waitForDone()

    def update_progress(self) -> None:
        self.progress_dialog.setValue(self.progress_dialog.value()+1)

    def error_worker(self, msg: str) -> None:
        ErrorMessageBox(msg, self.parent()).exec_()
        self.progress_dialog.cancel()

    def start(self):
        self.progress_dialog = ProgressDialog(self.label, self.parent())
        self.progress_dialog.set_cancel_procedure(self.cancel_procedure)
        self.progress_dialog.setMaximum(self.worker.number_of_progress())
        self.progress_dialog.show()
        super().start(self.worker)