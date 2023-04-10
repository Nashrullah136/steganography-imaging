from src.helper.BinaryDigitArray import BinaryDigitArray
from os import path
from src.assembler.Assembler import Assembler

class FileAssembler(Assembler):
    def __init__(self) -> None:
        super().__init__()

    def _get_file_extension(self, filepath: str) -> str:
        return path.splitext(filepath)[1]
    
    def set_folder(self, folder: str) -> None:
        self.folder = folder

    def set_filename(self, filename: str) -> None:
        self.filename = filename

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

    def assemble(self, msg: BinaryDigitArray) -> str:
        ext = msg.read_bytes(4).decode().strip()
        file_destiny = path.join(self.folder, f'{self.filename}.{ext}')
        with open(file_destiny, "wb") as file:
            file.write(msg.read_all_bytes())
        return file_destiny