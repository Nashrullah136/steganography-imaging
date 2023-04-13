from src.stegano_method.SteganoMethod import SteganoMethod
import numpy as np
from src.helper.BinaryDigitArray import BinaryDigitArray

#TODO: improve performance
class LSB(SteganoMethod):
    _metadata_length = 64

    def __init__(self, bit_size: int = 1) -> None:
        super().__init__()
        self.bit_size = bit_size

    def hide(self, vessel_pixel: np.ndarray, secret_data: BinaryDigitArray) -> np.ndarray:
        real_shape = vessel_pixel.shape
        vessel_pixel_flatten = vessel_pixel.flatten()
        secret_data.insert_front(
            BinaryDigitArray.from_int(secret_data.len(), 64))
        if secret_data.len() > len(vessel_pixel_flatten) * self.bit_size:
            raise RuntimeError("Vessel size is too small")
        for pixel_pos in range(secret_data.len()//self.bit_size):
            chunk_of_secret_data = secret_data.read_int(self.bit_size)
            vessel_pixel_flatten[pixel_pos] = (
                vessel_pixel_flatten[pixel_pos] & (255 << self.bit_size)) | chunk_of_secret_data
        vessel_pixel = vessel_pixel_flatten.reshape(real_shape)
        return vessel_pixel

    def reveal(self, vessel_pixel: np.ndarray) -> BinaryDigitArray:
        vessel_pixel.astype('uint64')
        vessel_pixel_flatten = vessel_pixel.flatten()
        bit_mask = 2**self.bit_size - 1
        all_result = np.bitwise_and(vessel_pixel_flatten, np.full(
            vessel_pixel_flatten.shape, bit_mask))
        all_result = BinaryDigitArray.from_ndarray(all_result, self.bit_size)
        len_data = all_result.read_int(64)
        return BinaryDigitArray(all_result.read(len_data))
