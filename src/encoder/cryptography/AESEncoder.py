from Cryptodome.Cipher import AES
from ..Encoder import Encoder
from ...helper.BinaryDigitArray import BinaryDigitArray
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes

class AESEncoder(Encoder):
    def __init__(self, key: str) -> None:
        super().__init__()
        self.key = key.encode()
        if len(self.key) <= 16:
            self.key = pad(self.key, 16)
        elif len(self.key) <= 24:
            self.key = pad(self.key, 24)
        elif len(self.key) <= 32:
            self.key = pad(self.key, 32)
        else:
            self.key = self.key[:32]

    def encode(self, msg: BinaryDigitArray) -> BinaryDigitArray:
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ct_bytes = cipher.encrypt(pad(msg.read_all_bytes(), AES.block_size))
        result = BinaryDigitArray.from_bytes(b''.join([iv, ct_bytes]))
        return result

    def decode(self, msg: BinaryDigitArray) -> BinaryDigitArray:
        iv = msg.read_bytes(AES.block_size)
        ct = msg.read_all_bytes()
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return BinaryDigitArray.from_bytes(pt)