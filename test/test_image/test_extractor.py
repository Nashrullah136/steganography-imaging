import unittest
from src.helper.BinaryDigitArray import BinaryDigitArray
from src.assembler.ImageAssembler import ImageAssembler
from src.encoder.compression.DeflateEncoder import DeflateEncoder
from src.encoder.compression.LZWEncoder import LZWEncoder
from src.image.extractor import Extractor
from src.stegano_method.BPCS import BPCS
import cv2 as cv

class TestExtractor(unittest.TestCase):

    def test_lzw_with_bpcs(self):
        vessel_img_result = cv.imread('test\\test_sample\\secret_result_lzw.bmp')
        extractor = Extractor(BPCS(), ImageAssembler())
        extractor.add_encoder(LZWEncoder())
        extractor.extract(vessel_img_result, 'test\\test_sample', 'extract_result')
        secret_img_ori = cv.imread('test\\test_sample\\secret_img.png')
        secret_img_extracted = cv.imread('test\\test_sample\\extract_result.png')
        self.assertTrue((secret_img_extracted == secret_img_ori).all())

    def test_deflate_with_bpcs(self):
        vessel_img_result = cv.imread('test\\test_sample\\secret_result_bpcs.bmp')
        extractor = Extractor(BPCS(), ImageAssembler())
        extractor.add_encoder(DeflateEncoder())
        extractor.extract(vessel_img_result, 'test\\test_sample', 'extract_result')
        secret_img_ori = cv.imread('test\\test_sample\\secret_img.png')
        secret_img_extracted = cv.imread('test\\test_sample\\extract_result.png')
        self.assertTrue((secret_img_extracted == secret_img_ori).all())

if __name__ == '__main__':
    unittest.main()