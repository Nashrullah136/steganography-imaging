import unittest
from src.assembler.ImageAssembler import ImageAssembler
import cv2 as cv

class TestImageAssembler(unittest.TestCase):

    def test_compatible(self):
        assembler = ImageAssembler()
        result = assembler.disassemble('test\\test_sample\\lenna.png')
        extracted_ori = assembler.assemble(result, 'test\\test_sample', 'result')
        img = cv.imread('test\\test_sample\\lenna.png')
        result_img = cv.imread('test\\test_sample\\result.png')
        self.assertTrue((img == result_img).all())

if __name__ == "__main__":
    unittest.main()