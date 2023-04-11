import unittest
from src.helper.BinaryDigitArray import BinaryDigitArray
from src.stegano_method.LSB import LSB
import cv2 as cv
import numpy as np

class TestLSB(unittest.TestCase):

    def test_compatible(self):
        img = cv.imread('test\\test_sample\\lenna.png')
        msg = BinaryDigitArray.from_bytes("apa, siapa, dimana".encode())
        bpcs = LSB(1)
        inserted = bpcs.hide(img, msg)
        extracted = bpcs.reveal(inserted)
        self.assertEqual("apa, siapa, dimana".encode(), extracted.read_all_bytes())

if __name__ == '__main__':
    unittest.main()