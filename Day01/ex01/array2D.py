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

        # I removed this check because it should work with empty lists

        # Check if all elements are lists (for 2D array)
        if not all(isinstance(row, list) for row in family):
            raise TypeError("All elements must be lists for 2D array")

        # Check if all rows have the same length
        if len(set(len(row) for row in family)) > 1:
            raise ValueError("All rows must have the same length")

        # I also removed this check because nothing is said in the subject is
        # told about the types of the individual elements, so this implies that
        # those can be elements of any type

        # Convert to numpy array to easily get shape
        np_array = np.array(family)
        shape = np_array.shape

        print(f"My shape is : {shape}")

        # Apply slicing
        sliced_family = family[start:end]

        # Get new shape
        # It's better and more readable to just also convert the result to a
        # ndarray to directly get its shape.
        np_array = np.array(sliced_family)
        new_shape = np_array.shape

        print(f"My new shape is : {new_shape}")

        return sliced_family

        # Never re-raise an exception, either transform it to another
        # exception, or return a default error value instead
    except Exception as e:
        print(f"Error: {e}")
        return []
