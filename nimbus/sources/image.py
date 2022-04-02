import numpy.typing as npt
from PIL import Image as pil
import numpy as np
from nimbus import Samples
import pathlib


class Image:
    """
    Image is a source class that takes in an image and converts it to a numpy array

    Attributes
    ----------
    image: pathlib.Path
        Path of image file to open

    """

    def __init__(self, image: pathlib.Path):
        """
        Constructs a new Image Source
        Parameters
        ----------
        image: pathlib.Path
            Path of image file to open
        """
        self.image = str(image)
        img = pil.open(self.image)
        self.imarray = np.array(img)
        self.index = 0

    def read(self) -> npt.NDArray:
        """
        Reads image row by row

        Returns
        -------
        Samples
            New Samples data class object where data is imgarray and no sample_rate is set

        Raises
        ------
        EOFError
            Reached end of file

        """
        self.index += 1
        if self.index > len(self.imarray):
            raise EOFError()
        return Samples(self.imarray[self.index - 1, :])
