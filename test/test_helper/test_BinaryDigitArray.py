import unittest
from src.helper.BinaryDigitArray import BinaryDigitArray
from src.stegano_method.BPCS import BPCS
import cv2 as cv
import numpy as np

class TestBDA(unittest.TestCase):

    def test_conjugate(self):
        bpcs = BPCS(0.3)
        data = np.arange(64).reshape((8,8))
        result = bpcs._conjugate(bpcs._conjugate(data))
        ass = (data == result).all()
        self.assertTrue(ass)

    def test_compatible(self):
        img = cv.imread('C:\\Users\\T3lk0m53l\\Documents\\Code\\Stegano\\sample\\picture\\0266554465.jpeg')
        msg = BinaryDigitArray.from_bytes("apa, siapa, dimana".encode())
        bpcs = BPCS(0.5)
        inserted = bpcs.hide(img, msg)
        extracted = bpcs.reveal(inserted)
        self.assertEqual("apa, siapa, dimana".encode(), extracted.read_all_bytes())


if __name__ == '__main__':
    unittest.main()