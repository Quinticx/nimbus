import numpy.typing as npt
from PIL import Image as pil
import numpy as np
from nimbus import Samples


class Image:
    """Image is a source that takes in an image and converts it to a numpy array"""

    def __init__(self, image: str):
        self.image = image
        img = pil.open(self.image)
        self.imarray = np.array(img)
        self.index = 0

    def read(self) -> npt.NDArray:
        """Returns Image row by row"""
        self.index += 1
        return Samples(self.imarray[self.index - 1, :])
