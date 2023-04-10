import numpy as np
from src.stegano_method.SteganoMethod import SteganoMethod
from src.encoder.Encoder import Encoder
from src.assembler.Assembler import Assembler
import cv2 as cv
import typing
from ..helper.BinaryDigitArray import BinaryDigitArray
from ..gui.component.WorkerSignal import WorkerSignal
from ..gui.component.Runnable import Runnable
import time 
import os

class Insertor(Runnable):
    def __init__(self):
        super().__init__()
        self.encoders: list[Encoder] = list()

    def set_vessel_file(self, vessel_file: str) -> None:
        self.stegano_method.set_vessel_pixel(cv.imread(vessel_file))

    def set_secret_file(self, secret_file: str) -> None:
        self.secret_file = secret_file

    def add_encoder(self, encoder: Encoder) -> None:
        self.encoders.append(encoder)

    def set_stegano_method(self, stegano_method: SteganoMethod) -> None:
        self.stegano_method = stegano_method

    def set_assembler(self, assembler: Assembler) -> None:
        self.assembler = assembler

    def set_folder(self, folder: str) -> None:
        self.folder = folder

    def number_of_progress(self) -> int:
        return len(self.encoders)+3
    
    def set_signal(self, signals: WorkerSignal) -> None:
        self.signals = signals

    def save_image(self, vessel_pixel: np.ndarray) -> str:
        default_name = f'{int(time.time())}_insert.bmp'
        result_path = os.path.join(self.folder, default_name)
        cv.imwrite(result_path, vessel_pixel)
        return result_path
        
    def create_operations(self) -> list[typing.Callable[[BinaryDigitArray], BinaryDigitArray]]:
        operations = [self.assembler.disassemble]
        for encoder in self.encoders:
            operations.append(encoder.encode)
        operations.append(self.stegano_method.hide)
        operations.append(self.save_image)
        return operations

    def stop(self) -> None:
        self.stop_status = True

    def run(self) -> None:
        self.stop_status = False
        operations = self.create_operations()
        i = 0
        result = self.secret_file
        try:
            while i < len(operations) and not self.stop_status:
                print(operations[i])
                result = operations[i](result)
                self.signals.progress.emit()
                i = i+1
            if self.stop_status:
                return
        except RuntimeError as err:
            print(str(err))
            self.signals.error.emit(str(err))
            return
        self.signals.finished.emit(result)