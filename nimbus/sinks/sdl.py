import numpy as np
from PIL import Image as pil
from nimbus import Samples
import sdl2.ext
import sdl2.ext.pixelaccess


class SDL:
    def __init__(self, width: int, height: int):
        sdl2.ext.init()
        self.window = sdl2.ext.Window("Real Time Window", size=(width, height))
        self.pixels = sdl2.ext.pixelaccess.pixels2d(self.window.get_surface())
        self.window.show()
        self.row = 0
        self.width = width
        self.height = height

    def execute(self, signal: Samples):
        if not signal.data.dtype == np.uint8:
            raise ValueError(f"SDL Sink requires np.uint8 signal: {signal.data.dtype}")

        for col in range(self.width):
            if col >= signal.data.size:
                self.pixels[col][self.row] = 0
            else:
                lum = signal.data[col]
                self.pixels[col][self.row] = lum << 16 | lum << 8 | lum

        self.row += 1
        self.row = self.row % self.height

        self.window.refresh()
