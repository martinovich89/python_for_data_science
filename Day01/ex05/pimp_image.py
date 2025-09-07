import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.
    Uses only =, +, -, * operators.

    Args:
        array: numpy array representing an image

    Returns:
        numpy array with inverted colors
    """
    try:
        if array is None or not isinstance(array, np.ndarray):
            raise ValueError("Invalid input: expected numpy array")

        if len(array.shape) != 3 or array.shape[2] != 3:
            raise ValueError("Invalid input: expected RGB image array")

        # Invert colors: 255 - pixel_value
        inverted = 255 - array

        # Display the image
        plt.figure("Figure VIII.2")
        plt.imshow(inverted)
        plt.axis('on')
        plt.title("Invert")
        plt.show()

        print("The shape of image is:", inverted.shape)
        print(inverted)
        return inverted

    except Exception as error:
        print("Error in ft_invert:", str(error))
        return array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Applies a red filter to the image.
    Uses only = and * operators.

    Args:
        array: numpy array representing an image

    Returns:
        numpy array with red filter applied
    """
    try:
        if array is None or not isinstance(array, np.ndarray):
            raise ValueError("Invalid input: expected numpy array")

        if len(array.shape) != 3 or array.shape[2] != 3:
            raise ValueError("Invalid input: expected RGB image array")

        # Create a copy to avoid modifying original
        red_filtered = array.copy()

        # Keep only red channel, zero out green and blue
        red_filtered[:, :, 1] = 0
        red_filtered[:, :, 2] = 0

        # Display the image
        plt.figure("Figure VIII.3")
        plt.imshow(red_filtered)
        plt.axis('on')
        plt.title("Red")
        plt.show()

        print("The shape of image is:", red_filtered.shape)
        print(red_filtered)
        return red_filtered

    except Exception as error:
        print("Error in ft_red:", str(error))
        return array


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Applies a green filter to the image.
    Uses only = and - operators.

    Args:
        array: numpy array representing an image

    Returns:
        numpy array with green filter applied
    """
    try:
        if array is None or not isinstance(array, np.ndarray):
            raise ValueError("Invalid input: expected numpy array")

        if len(array.shape) != 3 or array.shape[2] != 3:
            raise ValueError("Invalid input: expected RGB image array")

        # Create a copy to avoid modifying original
        green_filtered = array.copy()

        # Keep only green channel, zero out red and blue
        green_filtered[:, :, 0] = 0
        green_filtered[:, :, 2] = 0

        # Display the image
        plt.figure("Figure VIII.4")
        plt.imshow(green_filtered)
        plt.axis('on')
        plt.title("Green")
        plt.show()

        print("The shape of image is:", green_filtered.shape)
        print(green_filtered)
        return green_filtered

    except Exception as error:
        print("Error in ft_green:", str(error))
        return array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Applies a blue filter to the image.
    Uses only = operator.

    Args:
        array: numpy array representing an image

    Returns:
        numpy array with blue filter applied
    """
    try:
        if array is None or not isinstance(array, np.ndarray):
            raise ValueError("Invalid input: expected numpy array")

        if len(array.shape) != 3 or array.shape[2] != 3:
            raise ValueError("Invalid input: expected RGB image array")

        # Create a copy to avoid modifying original
        blue_filtered = array.copy()

        # Keep only blue channel, set red and green to 0
        blue_filtered[:, :, 0] = 0
        blue_filtered[:, :, 1] = 0

        # Display the image
        plt.figure("Figure VIII.5")
        plt.imshow(blue_filtered)
        plt.axis('on')
        plt.title("Blue")
        plt.show()

        print("The shape of image is:", blue_filtered.shape)
        print(blue_filtered)
        return blue_filtered

    except Exception as error:
        print("Error in ft_blue:", str(error))
        return array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to greyscale.
    Uses only = operator.

    Args:
        array: numpy array representing an image

    Returns:
        numpy array converted to greyscale
    """
    try:
        if array is None or not isinstance(array, np.ndarray):
            raise ValueError("Invalid input: expected numpy array")

        if len(array.shape) != 3 or array.shape[2] != 3:
            raise ValueError("Invalid input: expected RGB image array")

        # Create a copy to avoid modifying original
        grey_filtered = array.copy()

        # Convert to greyscale by copying green channel to red and blue
        grey_filtered[:, :, 0] = grey_filtered[:, :, 1]  # Red = Green
        grey_filtered[:, :, 2] = grey_filtered[:, :, 1]  # Blue = Green

        # Display the image
        plt.figure("Figure VIII.6")
        plt.imshow(grey_filtered)
        plt.axis('on')
        plt.title("Grey")
        plt.show()

        print("The shape of image is:", grey_filtered.shape)
        print(grey_filtered)
        return grey_filtered

    except Exception as error:
        print("Error in ft_grey:", str(error))
        return array


def main():
    """
    Loads the image, outputs image shape and data, displays the image,
    and calls all color filter functions
    """
    try:
        array = ft_load("landscape.jpg")

        # Apply all filters
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)

        # Print docstring as requested
        print(ft_invert.__doc__)

    except Exception as error:
        print("Error in main:", str(error))


if __name__ == "__main__":
    main()
