import numpy.typing as npt
from PIL import Image as pil
import numpy as np


class Image:
    """Image is a source that takes in an image and converts it to a numpy array"""

    def __init__(self):
        pass

    def open(self, image) -> npt.NDArray:
        img = pil.open(image)
        imarray = np.array(img)
        return imarray
