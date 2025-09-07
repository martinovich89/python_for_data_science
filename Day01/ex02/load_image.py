import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its shape, and returns its pixel content
    in RGB format as a numpy array.

    Args:
        path: string path to the image file

    Returns:
        np.ndarray: image data in RGB format

    Raises:
        FileNotFoundError: if the image file doesn't exist
        ValueError: if the file format is not supported
        Exception: for other loading errors
    """
    try:
        # Check if path is a string
        if not isinstance(path, str):
            raise TypeError("Path must be a string")

        # You don't need to check if the file exists here because Image.open
        # already throws FileNotFoundError in that case and you already
        # caught the FileNotFoundError exception bellow.

        # Get file extension to check format
        _, extension = os.path.splitext(path.lower())
        supported_formats = ['.jpg', '.jpeg']

        if extension not in supported_formats:
            raise ValueError("Unsupported file format: " + extension + ". " +
                             "Supported formats: " +
                             ", ".join(supported_formats))

        # Load the image
        with Image.open(path) as img:
            # Convert to RGB if not already (handles RGBA, grayscale, etc.)
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Convert to numpy array
            image_array = np.array(img, dtype=np.int8)

            # Print the shape
            print("The shape of image is: ", image_array.shape)
            return image_array

    # I removed the two previous except statements because you are doing the same
    # thing
    except Exception as error:
        print("Error: ", error)
        # Same here, don't re-raise errors
        return np.array([])
