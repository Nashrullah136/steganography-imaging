import unittest
from src.helper.BinaryDigitArray import BinaryDigitArray
from src.encoder.compression.LZWEncoder import LZWEncoder
from src.assembler.ImageAssembler import ImageAssembler
import cv2 as cv

class TestLZWEncoder(unittest.TestCase):

    def test_compatible(self):
        msg = BinaryDigitArray.from_bytes("apa, siapa, dimana".encode())
        lzw = LZWEncoder()
        encoded = lzw.encode(msg)
        decoded = lzw.decode(encoded)
        self.assertEqual(b'apa, siapa, dimana', decoded.read_all_bytes())

    def test_image(self):
        assembler =  ImageAssembler()
        secret_msg = assembler.disassemble('test\\test_sample\\secret_img.png')
        lzw = LZWEncoder()
        compressed = lzw.encode(BinaryDigitArray(secret_msg.data.copy()))
        decompressed = lzw.decode(compressed)
        self.assertTrue(secret_msg.read_all_bytes() == decompressed.read_all_bytes())

if __name__ == '__main__':
    unittest.main()
