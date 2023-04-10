import unittest
from src.helper.BinaryDigitArray import BinaryDigitArray
from src.encoder.compression.DeflateEncoder import DeflateEncoder

class TestDeflateEncoder(unittest.TestCase):

    def test_compatible(self):
        msg = BinaryDigitArray.from_bytes("apa, siapa, dimana".encode())
        deflate = DeflateEncoder()
        encoded = deflate.encode(msg)
        decoded = deflate.decode(encoded)
        self.assertEqual(b'apa, siapa, dimana', decoded.read_all_bytes())


if __name__ == '__main__':
    unittest.main()
