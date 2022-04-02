import numpy as np
from PIL import Image as pil
from nimbus import Samples


class Image:
    """
    Image is a sink class that saves a signal to a .png image file

    Attributes
    ----------
    filename: str
        Filename to save .png file as

    """

    def __init__(self, filename: str = "output.png"):
        """
        Constructs new Image Sink
        Parameters
        ----------
        filename: str
            Filename to save .png file as

        """
        self.filename = filename
        self.buffer = []

    def execute(self, signal: Samples):
        """
        Writes signal to a .png file

        Parameters
        ----------
        signal: Samples
            Input signal to save into .png file

        Raises
        ------
        ValueError
            Signal is not of type uint8
        """
        if not signal.data.dtype == np.uint8:
            raise ValueError(
                f"Image Sink requires np.uint8 signal: {signal.data.dtype}"
            )
        self.buffer.append(signal.data)

    def close(self):
        """
        Closes .png file after pading if necessary.
        """
        max_size = max(map(lambda arr: arr.size, self.buffer))

        # Pad every image buffer to largest size
        tmp = map(
            lambda arr: np.concatenate((arr, np.zeros(max_size - arr.size))),
            self.buffer,
        )
        img_buffer = np.stack(tmp)

        image = pil.fromarray(np.uint8(img_buffer[:, :2080]))

        image.save(self.filename)
