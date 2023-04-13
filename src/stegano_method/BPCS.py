from src.helper.BinaryDigitArray import BinaryDigitArray
from src.stegano_method.SteganoMethod import SteganoMethod
import numpy as np
from math import inf


class BPCS(SteganoMethod):
    #TODO increase Efficiency : try parallel or run it on gpu 
    Wc: np.ndarray = np.indices((8, 8)).sum(axis=0) % 2

    def __init__(self, alpha: float = 0.3) -> None:
        super().__init__()
        self.alpha = alpha
        
    def pbc_to_cgc(self, pixel: np.ndarray) -> np.ndarray:
        temp = pixel.copy()
        result = temp >> 7
        for i in range(7, 0, -1):
            result <<= 1
            result |= ((temp >> i) & 1) ^ ((temp >> (i - 1)) & 1)
        return result

    def cgc_to_pbc(self, pixel: np.ndarray) -> np.ndarray:
        temp = pixel.copy()
        result = temp >> 7
        for i in range(7, 0, -1):
            b_before = result.copy()
            result <<= 1
            result |= (b_before & 1) ^ ((temp >> (i - 1)) & 1)
        return result

    def _complexity(self, data: list) -> float:
        matrix = np.asarray(data).reshape((8, 8))
        maxim = ((matrix.shape[0] - 1) * matrix.shape[1]) + \
            ((matrix.shape[1] - 1) * matrix.shape[0])
        curr = 0.0
        first = matrix[0, 0]
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if (first != matrix[i, j]):
                    curr = curr + 1
                    first = matrix[i, j]
        first = matrix[0, 0]
        for i in range(matrix.shape[1]):
            for j in range(matrix.shape[0]):
                if (first != matrix[j, i]):
                    curr = curr + 1
                    first = matrix[j, i]
        return curr/maxim

    def _conjugate(self, data: np.ndarray) -> np.ndarray:
        return self.Wc ^ data

    def _conjugate_block(self, block: list[int]) -> np.ndarray:
        block = list(block)
        block.insert(1, 0)
        block = np.asarray(block).reshape((8, 8))
        if self._complexity(block) <= self.alpha:
            block = self._conjugate(block)
        return block

    def _process_secret_data(self, secret_data: BinaryDigitArray) -> list[np.ndarray]:
        data = secret_data.read_all(63)
        return list(map(self._conjugate_block, data))

    def _convert_to_block(self, data: np.ndarray) -> np.ndarray:
        data_shape = data.shape
        result = data[:data_shape[0]//8*8, :data_shape[1]//8*8]
        result = result.reshape(result.shape[0]//8 * result.shape[1]//8, 8, 8)
        return result

    def _extract_all_color(self, vessel_pixel: np.ndarray) -> np.ndarray:
        shape = vessel_pixel.shape
        if len(shape) < 3:
            return vessel_pixel.reshape((1, *vessel_pixel.shape))
        else:
            return np.rollaxis(vessel_pixel, 2, 0)

    def _get_all_available_block(self, vessel_pixel: np.ndarray) -> np.ndarray:
        vessel_pixel = self._extract_all_color(vessel_pixel)
        vessel_block = None
        for color in range(vessel_pixel.shape[0]):
            vessel_pixel_color = vessel_pixel[color]
            vessel_block_color = self._convert_to_block(vessel_pixel_color)
            if type(vessel_block) != type(None):
                vessel_block = np.append(vessel_block, vessel_block_color, axis=0)
            else:
                vessel_block = vessel_block_color.copy()
        return vessel_block

    def _return_all_available_block(self, vessel_pixel: np.ndarray, vessel_block: np.ndarray) -> np.ndarray:
        r = vessel_pixel.shape[0]//8*8
        c = vessel_pixel.shape[1]//8*8
        shape = vessel_pixel.shape
        if len(shape) < 3:
            shape = (*shape, 1)
        for color in range(shape[2]):
            vessel_pixel[:r, :c, color] = vessel_block[:r//8*c//8].flatten().reshape((r, c))
            vessel_block = vessel_block[r//8*c//8:]
        return vessel_pixel

    def _extract_bitplane_from_block(self, block: np.ndarray, bit: int) -> np.ndarray:
        bit_plane = (block & np.full((8, 8), 2**bit)) >> bit
        return bit_plane

    def _embed_msg_to_block(self, block: np.ndarray, msg: np.ndarray, bit: int) -> np.ndarray:
        removed_bit = block & (255 - 1 << bit)
        msg = msg << bit
        return removed_bit + msg

    def hide(self, vessel_pixel: np.ndarray, secret_data: BinaryDigitArray) -> np.ndarray:
        secret_data.insert_front(BinaryDigitArray.from_int(secret_data.len(), 63))
        processed_secret_data = self._process_secret_data(secret_data)
        vessel_cgc = self.pbc_to_cgc(vessel_pixel)
        vessel_block = self._get_all_available_block(vessel_cgc)
        for bit in range(8):
            i = 0
            while len(processed_secret_data) and i < vessel_block.shape[0]:
                bitplane = self._extract_bitplane_from_block(vessel_block[i], bit)
                if self._complexity(bitplane) > self.alpha:
                    if len(processed_secret_data) == 0:
                        break
                    msg = processed_secret_data.pop(0)
                    vessel_block[i] = self._embed_msg_to_block(vessel_block[i], msg, bit)
                i = i+1
            if i >= vessel_block.shape[0]:
                break
        if len(processed_secret_data):
            raise RuntimeError("Vessel is too small")
        vessel_pixel = self._return_all_available_block(vessel_pixel, vessel_block)
        vessel_pixel = self.cgc_to_pbc(vessel_pixel)
        return vessel_pixel

    def reveal(self, vessel_pixel: np.ndarray) -> BinaryDigitArray:
        result = BinaryDigitArray()
        vessel_cgc = self.pbc_to_cgc(vessel_pixel)
        vessel_block = self._get_all_available_block(vessel_cgc)
        size = inf
        for bit in range(8):
            i = 0
            while result.len() < size and i < vessel_block.shape[0]:
                bit_plane = self._extract_bitplane_from_block(vessel_block[i], bit)
                if self._complexity(bit_plane) > self.alpha:
                    msg = bit_plane
                    if msg[0][1] == 1:
                        msg = self._conjugate(msg)
                    msg : list = msg.flatten().tolist()
                    msg.pop(1)
                    result.insert(BinaryDigitArray(msg))
                    if size == inf:
                        size = result.read_int(63)
                i = i+1
            if i >= vessel_block.shape[0]:
                    break
        if result.len() < size:
            raise RuntimeError("Can't extract message")
        return BinaryDigitArray(result.read(size))
