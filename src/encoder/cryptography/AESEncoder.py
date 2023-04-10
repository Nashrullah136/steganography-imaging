from Cryptodome.Cipher import AES
from ..Encoder import Encoder
from ...helper.BinaryDigitArray import BinaryDigitArray
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from .Cryptography import Cryptograph

class AESEncoder(Encoder, Cryptograph):
    def __init__(self, key: str = '') -> None:
        super().__init__()
        self.key = key.encode()

    def set_key(self, key: str) -> None:
        self.key = key.encode()

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