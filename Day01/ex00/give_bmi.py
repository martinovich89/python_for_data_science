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
        if not isinstance(bmi, list) or not isinstance(limit, int):
            raise TypeError("types for arguments must be (list, int)")
        if not all(isinstance(b, (int, float)) for b in bmi):
            raise ValueError("bmi must be int/float")
        if not isinstance(limit, (int, float)):
            raise ValueError("limit must be finite int/float")
        if any(b <= 0 for b in bmi) or limit <= 0:
            raise ValueError("heights and weights must be strictly positive")

        bmi_array = np.array(bmi, dtype=float)

        return (bmi_array > limit).tolist()
    except Exception as error:
        print("Error:", error)
        return []


def main() -> None:
    from give_bmi import give_bmi, apply_limit
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
