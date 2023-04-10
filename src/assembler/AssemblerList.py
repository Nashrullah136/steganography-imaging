from .FileAssembler import FileAssembler
from .ImageAssembler import ImageAssembler
from .Assembler import Assembler

class AssemblerList():
    def __init__(self) -> None:
        self.assemblers : list[tuple[str, Assembler]] = list()
        self.assemblers.append(("Raw Bit", FileAssembler()))
        self.assemblers.append(("Pixel", ImageAssembler()))

    def get_assemblers(self) -> list[tuple[str, Assembler]]:
        return self.assemblers