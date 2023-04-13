from .BPCS import BPCS
from .LSB import LSB


class SteganoMethodList():
    def __init__(self) -> None:
        self.stegano_methods = \
        [
            {
                'name': 'LSB',
                'stegano_method': LSB,
                'label': 'Bit',
                'bottom': 1,
                'top': 8,
                'singleStep': 1
            },
            {
                'name': 'BPCS',
                'stegano_method': BPCS,
                'label': 'Bit',
                'bottom': 0,
                'top': 1,
                'singleStep': 0.1
            }
        ]

    def get_stegano_methods(self) -> list[dict]:
        return self.stegano_methods
