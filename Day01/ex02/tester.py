from load_image import ft_load
from typing import cast

def main():
    """Main function for testing"""
    try:
        # Test with the example from the subject
        # Note: this will only work if landscape.jpg exists
        try:
            print("Testing with landscape.jpg:")
            image_data = ft_load("landscape.jpg")
            print(image_data)
            print("Image loaded successfully with shape:", image_data.shape)
        except FileNotFoundError:
            print("landscape.jpg not found, skipping this test")

        print("\n--- Additional tests ---")

        # Test error handling
        try:
            ft_load("nonexistent.jpg")
        except FileNotFoundError:
            print("FileNotFoundError handled correctly")

        try:
            ft_load("test.txt")  # Unsupported format
        except ValueError:
            print("Unsupported format error handled correctly")

        try:
            # Use cast here to satisfy type-checkers (for example I'm using
            # and it removes the red squigles), it doesn't do anything
            # else at runtime.
            ft_load(cast(str, 123))  # Wrong type
        except TypeError:
            print("TypeError handled correctly")

    except Exception as error:
        print("Unexpected error in main: ", error)


if __name__ == "__main__":
    main()
