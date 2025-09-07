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

        # Check if file exists
        if not os.path.exists(path):
            raise FileNotFoundError(f"File '{path}' not found")

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
            image_array = np.array(img)

            return image_array

    except FileNotFoundError as error:
        print("Error: ", error)
        raise error
    except ValueError as error:
        print("Error: ", error)
        raise error
    except Exception as error:
        print("Error loading image: ", error)
        raise error
