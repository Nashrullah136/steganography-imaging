import numpy as np
from src.stegano_method.SteganoMethod import SteganoMethod
from src.helper.BinaryDigitArray import BinaryDigitArray
from src.encoder.Encoder import Encoder
from src.assembler.Assembler import Assembler
import cv2 as cv
import typing
from PyQt5.QtCore import *
from ..gui.component.Runnable import Runnable
from ..gui.component.WorkerSignal import WorkerSignal
import time

class Extractor(Runnable):
    def __init__(self):
        super().__init__()
        self.encoders: list[Encoder] = list()

    def add_encoder(self, encoder: Encoder) -> None:
        self.encoders.append(encoder)

    def set_vessel_file(self, vessel_file: str) -> None:
        self.vessel_pixel = cv.imread(vessel_file)

    def set_stegano_method(self, stegano_method: SteganoMethod) -> None:
        self.stegano_method = stegano_method

    def set_assembler(self, assembler: Assembler) -> None:
        self.assembler = assembler
        name = f'{int(time.time())}_extract'
        self.assembler.set_filename(name)

    def set_folder(self, folder: str) -> None:
        self.assembler.set_folder(folder)

    def set_signal(self, signals: WorkerSignal) -> None:
        self.signals = signals
        
    def create_operations(self) -> list[typing.Callable[[BinaryDigitArray], BinaryDigitArray]]:
        operations = [self.assembler.assemble]
        for encoder in self.encoders:
            operations.append(encoder.decode)
        operations.append(self.stegano_method.reveal)
        operations.reverse()
        return operations

    def number_of_progress(self) -> int:
        return len(self.encoders)+2

    def stop(self) -> None:
        self.stop_status = True

    def run(self) -> None:
        self.stop_status = False
        operations = self.create_operations()
        i = 0
        result = self.vessel_pixel
        try:
            while i < len(operations) and not self.stop_status:
                self.signals.progress.emit()
                print(operations[i])
                result = operations[i](result)
                i = i+1
            if self.stop_status:
                return
        except RuntimeError as err:
            print(str(err))
            self.signals.error.emit(str(err))
            return
        self.signals.finished.emit(result)
    