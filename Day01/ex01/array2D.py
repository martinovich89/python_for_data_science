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

        # Check if family is empty
        if len(family) == 0:
            raise ValueError("Input list cannot be empty")

        # Check if all elements are lists (for 2D array)
        if not all(isinstance(row, list) for row in family):
            raise TypeError("All elements must be lists for 2D array")

        # Check if all rows have the same length
        if len(set(len(row) for row in family)) > 1:
            raise ValueError("All rows must have the same length")

        # Check if all elements are numbers (int or float)
        for row in family:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise TypeError("All elements must be int or float")

        # Convert to numpy array to easily get shape
        np_array = np.array(family)
        shape = np_array.shape

        print(f"My shape is : {shape}")

        # Apply slicing
        sliced_family = family[start:end]

        # Get new shape
        if len(sliced_family) > 0:
            new_shape = (len(sliced_family), len(sliced_family[0]))
        else:
            new_shape = (0, 0)

        print(f"My new shape is : {new_shape}")

        return sliced_family

    except Exception as e:
        raise e


def main():
    """Main function for testing"""
    try:
        # Test case from the subject
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]

        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))

        # Additional test cases
        print("\n--- Additional tests ---")

        # Test with different ranges
        test_family = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [10, 11, 12]]
        print(slice_me(test_family, 1, 3))

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
