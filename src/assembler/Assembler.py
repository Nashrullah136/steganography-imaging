from src.helper.BinaryDigitArray import BinaryDigitArray
import numpy as np

class Assembler:
    def set_folder(self, folder: str) -> None:
        pass
    def set_filename(self, filename: str) -> None:
        pass
    def disassemble(self, filepath: str) -> BinaryDigitArray:
        pass
    def assemble(self, msg: BinaryDigitArray) -> tuple[np.ndarray, str]:
        pass