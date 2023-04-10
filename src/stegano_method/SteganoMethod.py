import io
import numpy as np
from ..helper.BinaryDigitArray import BinaryDigitArray

class SteganoMethod:
    def set_parameter(self, parameter) -> None:
        pass

    def set_vessel_pixel(self, vessel_pixel: np.ndarray) -> None:
        self.vessel_pixel = vessel_pixel

    def hide(self, vessel_pixel: np.ndarray, secret_data: BinaryDigitArray) -> np.ndarray:
        pass

    def reveal(self, vessel_pixel: np.ndarray) -> BinaryDigitArray:
        pass