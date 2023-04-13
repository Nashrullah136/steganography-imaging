import numpy as np
from ..helper.BinaryDigitArray import BinaryDigitArray

class SteganoMethod:
    def hide(self, vessel_pixel: np.ndarray, secret_data: BinaryDigitArray) -> np.ndarray:
        pass

    def reveal(self, vessel_pixel: np.ndarray) -> BinaryDigitArray:
        pass