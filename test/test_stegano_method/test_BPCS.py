import unittest
from src.helper.BinaryDigitArray import BinaryDigitArray
from src.stegano_method.BPCS import BPCS
from src.assembler.ImageAssembler import ImageAssembler
import cv2 as cv
import numpy as np

class TestBPCS(unittest.TestCase):

    def test_conjugate(self):
        bpcs = BPCS(0.3)
        data = np.arange(64).reshape((8,8))
        result = bpcs._conjugate(bpcs._conjugate(data))
        ass = (data == result).all()
        self.assertTrue(ass)

    def test_compatible(self):
        img = cv.imread('test\\test_sample\\lenna.png')
        msg = BinaryDigitArray.from_bytes("apa, siapa, dimana".encode())
        bpcs = BPCS(0.5)
        inserted = bpcs.hide(img, msg)
        extracted = bpcs.reveal(inserted)
        self.assertEqual("apa, siapa, dimana".encode(), extracted.read_all_bytes())

    def test_from_image(self):
        assembler =  ImageAssembler()
        secret_msg = assembler.disassemble('test\\test_sample\\secret_img.png')
        vessel_img = cv.imread('test\\test_sample\\vessel_img.bmp')
        bpcs = BPCS(0.3)
        vessel_result = bpcs.hide(vessel_img, BinaryDigitArray(secret_msg.data.copy()))
        secret_msg_result = bpcs.reveal(vessel_result)
        self.assertTrue(secret_msg.read_all_bytes() == secret_msg_result.read_all_bytes())

if __name__ == '__main__':
    unittest.main()