from .LZWEncoder import LZWEncoder
from .DeflateEncoder import DeflateEncoder
from ..Encoder import Encoder

class CompressionList():
    def __init__(self):
        self.compressions = [
            ("LZW Compression", LZWEncoder()),
            ("Deflate Compression", DeflateEncoder())
        ]

    def get_compressions(self) -> list[tuple[str, Encoder]]:
        return self.compressions