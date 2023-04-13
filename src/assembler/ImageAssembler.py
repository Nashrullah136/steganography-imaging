from src.assembler.Assembler import Assembler
from src.helper.BinaryDigitArray import BinaryDigitArray
import cv2 as cv
import numpy as np
from os import path

class ImageAssembler(Assembler):
    def __init__(self) -> None:
        super().__init__()

    def disassemble(self, filepath: str) -> BinaryDigitArray:
        image_pixel = cv.imread(filepath)
        ext = path.splitext(filepath)[1].removeprefix(".")
        if len(ext) < 4:
            ext = " "*(4-len(ext)) + ext
        result = BinaryDigitArray.from_bytes(ext.encode())
        result.insert(BinaryDigitArray.from_int(len(image_pixel.shape), 8))
        for shape in image_pixel.shape:
            result.insert(BinaryDigitArray.from_int(shape, 32))
        result.insert(BinaryDigitArray.from_ndarray(image_pixel))
        return result

    def assemble(self, msg: BinaryDigitArray, dir: str, filename: str) -> str:
        ext = msg.read_bytes(4).decode().strip()
        len_shape = msg.read_int(8)
        shape = []
        for i in range(len_shape):
            shape.append(msg.read_int(32))
        pixel = msg.read_all_bytes()
        pixel = np.asarray(list(pixel))
        pixel = pixel.reshape(shape)
        full_path = path.join(dir, filename + '.' + ext)
        cv.imwrite(full_path, pixel)
        return full_path