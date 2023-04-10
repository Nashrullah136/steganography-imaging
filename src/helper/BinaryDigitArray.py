import numpy as np
import math

class BinaryDigitArray:
    def __init__(self, data: list = []) -> None:
        data = list(map(int, data))
        if len(data) != 0 and (max(data) > 1 or min(data) < 0):
            raise RuntimeError("Data must be 0 or 1")
        self.data = data
        self.padding = True

    @classmethod
    def from_string(cls, binary_string: str, encoding: str = "utf-8"):
        return cls(cls._from_string(binary_string, encoding))

    @classmethod
    def from_ndarray(cls, int_matrix: np.ndarray, bit_length: int = 8):
        return cls(cls._from_ndarray(int_matrix, bit_length))

    @classmethod
    def from_int(cls, data: int, bit_length: int = 8):
        return cls(cls._from_int(data, bit_length))

    @classmethod
    def from_bytes(cls, data: bytes):
        return cls(cls._from_bytes(data))
    
    @classmethod
    def _from_bytes(cls, data: bytes):
        result = []
        for byte in data:
            result.extend(cls._from_int(byte))
        return result

    @classmethod
    def _from_string(cls, string: str, encoding: str) -> list:
        result = []
        encoded = string.encode(encoding)
        for data in encoded:
            result.extend(cls._from_int(data))
        return result

    @classmethod
    def _from_int(self, data: int, bit_length: int = 8) -> list:
        bin_str = format(data, '0'+str(bit_length) +'b')
        if len(bin_str) > bit_length:
            raise RuntimeError("Insufficient bit length")
        return [int(i) for i in bin_str]

    @classmethod
    def _from_ndarray(self, data: np.ndarray, bit_length: int) -> list:
        data = data.astype(np.int64)
        data = data.flatten()
        result = []
        for bit in data:
            binary_digit = self._from_int(bit, bit_length)
            result.extend(binary_digit)
        return result

    @classmethod
    def _to_int(self, binary_digit: list) -> int:
        bin_str = "".join(map(str, binary_digit))
        return int(bin_str, 2)

    def _pad_data(self, multiple_of: int) -> None:
        if self.len() % multiple_of != 0:
            remain = multiple_of - (self.len()%multiple_of)
            self.data.extend([0] * remain)

    def len(self) -> int:
        return len(self.data)

    def insert_front(self, data: 'BinaryDigitArray') -> None:
        data.data.extend(self.data)
        self.data = data.data

    def insert(self, data: 'BinaryDigitArray') -> None:
        self.data.extend(data.data)

    def set_padding(self, padding_stat: bool) -> None:
        self.padding = padding_stat

    def read(self, size: int) -> list[int]:
        result = self.data[:size]
        self.data = self.data[size:]
        if self.padding and len(result) > 0 and len(result) < size:
            result.extend([0] * (size-len(result)))
        return result

    def read_all(self, bit_length: int = 1) -> list[int]:
        self._pad_data(bit_length)
        mat = np.asarray(self.data).reshape((len(self.data)//bit_length, bit_length))
        self.data.clear()
        if (bit_length == 1):
            mat = mat.flatten()
        return mat.tolist()
    
    def read_all_bytes(self) -> bytes:
        return bytes(self.read_all_int(8))
    
    def read_all_int(self, bit_length: int = 8) -> list[int]:
        mat = self.read_all(bit_length)
        return list(map(self._to_int, mat))

    def read_int(self, bit: int) -> int:
        result = self.read(bit)
        return self._to_int(result)

    def read_bytes(self, byte: int = 1) -> bytes:
        available_byte = len(self.data)//8
        processed_byte = min(byte, available_byte)
        mat = np.asarray(self.data[:processed_byte*8]).reshape((processed_byte, 8))
        self.data = self.data[processed_byte*8:]
        result = list(map(self._to_int, mat))
        if processed_byte < byte and len(self.data) != 0:
            result.append(self.read_int(8))
        return bytes(result)