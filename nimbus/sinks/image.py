import numpy as np
import numpy.typing as npt
from PIL import Image as pil
from nimbus import Samples


class Image:
    """Image is a sink that saves a signal to a .png image file"""

    def __init__(self, filename: str = "output.png"):
        self.filename = filename
        self.buffer = []

    def execute(self, signal: Samples):
        """Writes signal to a .png file"""
        self.buffer.append(signal.data)

    def close(self):
        image = pil.fromarray(np.uint8((np.array(self.buffer[:-1]))))

        image.save(self.filename)
