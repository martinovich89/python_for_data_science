import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array, prints its shape, and returns a truncated version
    based on the provided start and end arguments using slicing method.

    Args:
        family: 2D list containing numerical values
        start: starting index for slicing
        end: ending index for slicing

    Returns:
        list: truncated version of the input array

    Raises:
        TypeError: if family is not a list or contains invalid elements
        ValueError: if the 2D array is not properly formatted
    """
    try:
        # Check if family is a list
        if not isinstance(family, list):
            raise TypeError("Input must be a list")

        # Check if all elements are lists (for 2D array)
        if not all(isinstance(row, list) for row in family):
            raise TypeError("All elements must be lists for 2D array")

        # Check if all rows have the same length
        if len(set(len(row) for row in family)) > 1:
            raise ValueError("All rows must have the same length")

        # Convert to numpy array to easily get shape
        np_array = np.array(family)
        shape = np_array.shape

        print(f"My shape is : {shape}")

        # Apply slicing
        sliced_family = family[start:end]

        # Get new shape
        np_array = np.array(sliced_family)
        new_shape = np_array.shape

        print(f"My new shape is : {new_shape}")

        return sliced_family

    except Exception as error:
        print(f"Error: {error}")
        return []
