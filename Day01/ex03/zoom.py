import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    """
    Main function that loads an image, performs zoom operation and displays it.
    Handles errors by sending clear messages.
    """
    try:
        # Load the image
        img = ft_load("animal.jpeg")

        # Check img
        if img.shape==(0, 0, 0):
            print("An error occured during image loading, stopping now")
            return

        # Print original img data
        print(img)

        # Get image dimensions
        h, w, _ = img.shape

        # Calculate zoom area (center 400x400 pixels)
        zoom_size = 400

        # Calculate center coordinates
        center_y = int(h * 0.42)
        center_x = int(w * 0.64)

        # Calculate slice boundaries to center the 400x400 crop
        half_zoom = zoom_size // 2
        start_y = center_y - half_zoom
        end_y = center_y + half_zoom
        start_x = center_x - half_zoom
        end_x = center_x + half_zoom

        # Ensure we don't go out of bounds
        start_y = max(0, start_y)
        end_y = min(h, end_y)
        start_x = max(0, start_x)
        end_x = min(w, end_x)

        # Slice the image to get the zoom area
        zoomed_img = img[start_y:end_y, start_x:end_x]

        # Convert to grayscale by taking only one channel (green channel)
        if len(zoomed_img.shape) == 3:
            # Take green channel and keep dimension for consistency
            zoomed_gray = zoomed_img[:, :, 1:2]  # Keep as (h, w, 1)
        else:
            zoomed_gray = zoomed_img

        # Print new shape and data
        print("New shape after slicing:", zoomed_gray.shape)
        print(zoomed_gray)

        # Display the zoomed image
        plt.figure(figsize=(8, 8))

        # Display as grayscale
        if len(zoomed_gray.shape) == 3 and zoomed_gray.shape[2] == 1:
            # Remove the channel dimension for display
            display_img = zoomed_gray[:, :, 0]
        else:
            display_img = zoomed_gray

        # Frame settings
        plt.imshow(display_img, cmap='gray')
        plt.title('Zoomed Image')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')

        # Add scale ticks
        plt.xticks(range(0, display_img.shape[1], 50))
        plt.yticks(range(0, display_img.shape[0], 50))

        plt.show()

    except Exception as error:
        print("Error: ", error)
        return


if __name__ == "__main__":
    main()
