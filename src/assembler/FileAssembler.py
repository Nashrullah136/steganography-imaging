from src.helper.BinaryDigitArray import BinaryDigitArray
from os import path
from src.assembler.Assembler import Assembler

class FileAssembler(Assembler):
    def __init__(self) -> None:
        super().__init__()

    def _get_file_extension(self, filepath: str) -> str:
        return path.splitext(filepath)[1]

    def disassemble(self, filepath: str) -> BinaryDigitArray:
        ext = self._get_file_extension(filepath).removeprefix(".")
        if len(ext) < 4:
            ext = " "*(4-len(ext)) + ext
        result = BinaryDigitArray.from_string(ext)
        file = open(filepath, 'rb')
        for byte in file.read():
            result.insert(BinaryDigitArray.from_int(byte))
        file.close()
        return result

    def assemble(self, msg: BinaryDigitArray, dir: str, filename: str) -> str:
        ext = msg.read_bytes(4).decode().strip()
        file_destiny = path.join(dir, f'{filename}.{ext}')
        with open(file_destiny, "wb") as file:
            file.write(msg.read_all_bytes())
        return file_destiny