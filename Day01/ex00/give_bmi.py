import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    """
    Calcule l'indice de masse corporelle (IMC) pour chaque paire (taille, poids).
    Les tailles doivent être en mètres et les poids en kilogrammes.
    Retourne une liste des IMC, ou une liste vide en cas d'erreur.
    """
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
    """
    Compare chaque IMC à une limite donnée.
    Retourne une liste de booléens indiquant si l’IMC dépasse la limite.
    Retourne une liste vide en cas d’erreur de type ou de valeur.
    """
    try:
        if not isinstance(bmi, list) or not isinstance(limit, int):
            raise TypeError("types for arguments must be (list, int)")
        if not all(isinstance(b, (int, float)) for b in bmi):
            raise ValueError("bmi must be int/float")
        if any(b <= 0 for b in bmi) or limit <= 0:
            raise ValueError("heights and weights must be strictly positive")

        bmi_array = np.array(bmi, dtype=float)

        return (bmi_array > limit).tolist()
    except Exception as error:
        print("Error:", error)
        return []
