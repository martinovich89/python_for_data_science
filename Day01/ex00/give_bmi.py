import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:

    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("arguments must be lists")
        if len(height) != len(weight):
            raise ValueError("lists must have the same length")
        if not all(isinstance(h, (int, float)) for h in height):
            raise ValueError("heights must be int/float")
        if not all(isinstance(w, (int, float)) for w in weight):
            raise ValueError("weights must be int/float")
        if any(h <= 0 for h in height) or any(w <= 0 for w in weight):
            raise ValueError("heights and weights must be strictly positive")

        height_array = np.array(height, dtype=float)
        weight_array = np.array(weight, dtype=float)

        return (weight_array / (height_array ** 2)).tolist()
    except Exception as error:
        print("Error:", error)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        # You don't need the second check because you are checking for the same
        # thing just below.
        if not isinstance(bmi, list):
            raise ValueError("bmi argument must be a list")
        if not all(isinstance(b, (int, float)) for b in bmi):
            # I changed the message according to the fact that bmi is an array of value,
            # not a number value itself, so it wasn't clear
            raise ValueError("bmi values must be ints/floats")
        if not isinstance(limit, int):
            # You removed the infinity check but you forgot to remove its mention in the
            # error message, plus limit should only be integer, not float.
            raise ValueError("limit must be int/float")
        if any(b <= 0 for b in bmi) or limit <= 0:
            # The message was not correct here.
            raise ValueError("bmi values and limit must be strictly positive values")

        bmi_array = np.array(bmi, dtype=float)

        return (bmi_array > limit).tolist()
    except Exception as error:
        print("Error:", error)
        return []
