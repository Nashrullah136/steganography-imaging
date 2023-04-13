from src.encoder.Encoder import Encoder
from src.helper.BinaryDigitArray import BinaryDigitArray
import zlib

class DeflateEncoder(Encoder):
    def encode(self, msg: BinaryDigitArray) -> BinaryDigitArray:
        compress_obj = zlib.compressobj()
        result = compress_obj.compress(msg.read_all_bytes())
        result += compress_obj.flush()
        return BinaryDigitArray.from_bytes(result)

    def decode(self, msg: BinaryDigitArray) -> BinaryDigitArray:
        decompress_obj = zlib.decompressobj()
        result = decompress_obj.decompress(msg.read_all_bytes())
        result += decompress_obj.flush()
        return BinaryDigitArray.from_bytes(result)