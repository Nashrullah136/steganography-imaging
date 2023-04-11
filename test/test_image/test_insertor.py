import unittest
from src.helper.BinaryDigitArray import BinaryDigitArray
from src.assembler.ImageAssembler import ImageAssembler
from src.encoder.compression.DeflateEncoder import DeflateEncoder
from src.encoder.compression.LZWEncoder import LZWEncoder
from src.image.insertor import Insertor
from src.image.extractor import Extractor
from src.stegano_method.BPCS import BPCS
import cv2 as cv

class TestInsertor(unittest.TestCase):

    def test_lzw_with_bpcs(self):
        vessel_img = cv.imread('test\\test_sample\\vessel_img.bmp')
        insertor = Insertor(BPCS(), ImageAssembler())
        insertor.add_encoder(LZWEncoder())
        vessel_img_result = insertor.run(vessel_img, 'test\\test_sample\\secret_img.png')
        cv.imwrite('test\\test_sample\\secret_result_lzw.bmp', vessel_img_result)
        self.assertTrue(True)

    def test_deflate_with_bpcs(self):
        vessel_img = cv.imread('test\\test_sample\\vessel_img.bmp')
        insertor = Insertor(BPCS(), ImageAssembler())
        insertor.add_encoder(DeflateEncoder())
        vessel_img_result = insertor.run(vessel_img, 'test\\test_sample\\secret_img.png')
        cv.imwrite('test\\test_sample\\secret_result_bpcs.bmp', vessel_img_result)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()