import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def manual_transpose(img: np.ndarray) -> np.ndarray:
    """
    Manually transposes a 3D numpy array by swapping the first two dimensions.
    This function performs the transpose operation without using any library
    transpose method, implementing the operation with nested loops.

    Args:
        img: 3D numpy array representing an image (height, width, channels)

    Returns:
        np.ndarray: transposed array with dimensions (width, height, channels)

    Raises:
        TypeError: if img is not a numpy array
        ValueError: if img is not a 3D array
    """
    try:
        # Check if input is a numpy array
        if not isinstance(img, np.ndarray):
            raise TypeError("Input must be a numpy array")

        # Check if input is 3D
        if len(img.shape) != 3:
            raise ValueError("Input array must be 3-dimensional")

        # Get image dimensions
        h, w, c = img.shape

        # Init destination array dimensions for transpose.
        trans = np.empty((w, h, c), dtype=img.dtype)

        # Manual transpose by swapping indices
        for i in range(h):
            for j in range(w):
                trans[j, i] = img[i, j]

        return trans

    except (TypeError, ValueError) as error:
        print("Error in transpose: ", error)
        raise error
    except Exception as error:
        print("Unexpected error in transpose: ", error)
        raise error


def main():
    """
    Main function that loads an image, crops on a square section,
    transposes it manually, and displays the result.
    """
    try:
        # Load the image
        img = ft_load("animal.jpeg")

        # Add this check for the modified ft_load (same as previous exercise).
        if not img:
            print("An error occured during image loading, stopping now")
            return

        # Get image dimensions
        h, w, _ = img.shape

        # You can remove this check for the same reasons as previous exercise.

        # Calculate crop area
        crop_size = 400

        # Calculate crop coordinates (same as ex03)
        center_y, center_x = int(h * 0.42), int(w * 0.64)

        # Calculate slice boundaries to center the 400x400 crop
        half_crop = crop_size // 2
        start_y = center_y - half_crop
        end_y = center_y + half_crop
        start_x = center_x - half_crop
        end_x = center_x + half_crop

        # Ensure we don't go out of bounds
        start_y = max(0, start_y)
        end_y = min(h, end_y)
        start_x = max(0, start_x)
        end_x = min(w, end_x)

        # Slice the image to get the crop area
        cropped_img = img[start_y:end_y, start_x:end_x]

        # Convert to grayscale by taking only one channel (green channel)
        if len(cropped_img.shape) == 3:
            # Take green channel and keep dimension for consistency
            cropped_gray = cropped_img[:, :, 1:2]  # Keep as (height, width, 1)
        else:
            cropped_gray = cropped_img

        print("The shape of the image is:", cropped_gray.shape)
        print(cropped_gray)

        # Manually transpose the cropped image
        rotated = manual_transpose(cropped_gray)

        print("New shape after Transpose: ", rotated.shape[:2])
        print(rotated)

        # Display the transposed image
        plt.imshow(rotated.squeeze(), cmap="gray")
        plt.xlabel("X axis (pixels)")
        plt.ylabel("Y axis (pixels)")
        plt.title("Transposed 400x400 R channel")
        plt.show()

    except FileNotFoundError as error:
        print("Error: Image file not found - ", error)
    except ValueError as error:
        # To keep the same messages as previous exercise
        print("Error: Invalid image data - ", error)
    except Exception as error:
        print("Error: ", error)


if __name__ == "__main__":
    main()
