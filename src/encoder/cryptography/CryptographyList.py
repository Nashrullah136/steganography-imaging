from .AESEncoder import AESEncoder
from ..Encoder import Encoder

class CryptographList():
    def __init__(self):
        self.cryptographs = [
            ("AES Cryptograph", AESEncoder())
        ]

    def get_cryptographs(self) -> list[tuple[str, Encoder]]:
        return self.cryptographs