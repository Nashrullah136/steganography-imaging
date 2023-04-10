from src.encoder.Encoder import Encoder
from src.helper.BinaryDigitArray import BinaryDigitArray
import numpy as np

class LZWEncoder(Encoder):
    def encode(self, msg: BinaryDigitArray) -> BinaryDigitArray:
        image_data = msg.read_all_bytes()
        dictionary = {bytes([i]): i for i in range(256)}
        current_string = b''
        compressed = []
        for byte in image_data:
            new_string = current_string + bytes([byte])
            if new_string in dictionary:
                current_string = new_string
            else:
                compressed.append(dictionary[current_string])
                dictionary[new_string] = len(dictionary)
                current_string = bytes([byte])
        if current_string:
            compressed.append(dictionary[current_string])
        return BinaryDigitArray.from_ndarray(np.asarray(compressed), 24)

    def decode(self, msg: BinaryDigitArray) -> BinaryDigitArray:
        compressed_data = msg.read_all_int(24)
        dictionary = {i: bytes([i]) for i in range(256)}
        current_string = bytes([compressed_data[0]])
        decompressed = bytearray(current_string)
        for byte_code in compressed_data[1:]:
            if byte_code in dictionary:
                new_string = dictionary[byte_code]
            elif byte_code == len(dictionary):
                new_string = current_string + bytes([current_string[0]])
            else:
                raise ValueError('Bad compressed byte: %s' % byte_code)
            decompressed += new_string
            dictionary[len(dictionary)] = current_string + bytes([new_string[0]])
            current_string = new_string
        result = BinaryDigitArray.from_bytes(decompressed)
        return result