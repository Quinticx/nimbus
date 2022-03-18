import numpy as np
import numpy.typing as npt
from PIL import Image as pil


class Image:
    """Image is a sink that saves a signal to a .png image file"""

    def __init__(self, filename: str = "output.png"):
        self.filename = filename

    def execute(self, signal: npt.NDArray):
        """Writes signal to a .png file"""
        image = pil.fromarray(np.uint8(signal))
        image.save(self.filename)
        return
