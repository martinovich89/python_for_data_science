from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    if not path.lower().endswith(('.jpg', '.jpeg')):
        raise ValueError("Only JPG/JPEG are supported")

    try:
        img = Image.open(path)
    except Exception as e:
        raise ValueError(f"Cannot open image: {e}") from e

    # Conversion en RGB si ce n’est pas déjà le cas
    img = img.convert("RGB")
    arr = np.array(img)

    print(f"The shape of image is: {arr.shape}")
    return arr
