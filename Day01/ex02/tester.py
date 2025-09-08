from load_image import ft_load


def main():
    """Main function for testing"""
    try:
        # Test with the example from the subject
        # Note: this will only work if landscape.jpg exists
        print("Testing with landscape.jpg:")
        image_data = ft_load("landscape.jpg")
        if image_data.shape==(0, 0, 0):
            raise Exception("Couldn't load the file. Quitting now")
        print(image_data)

        print("\n--- Additional tests ---")

        # Test error handling
        ft_load("nonexistent.jpg")

        ft_load("test.txt")  # Unsupported format

        ft_load(123)  # Wrong type

    except Exception as error:
        print("Unexpected error in main: ", error)


if __name__ == "__main__":
    main()
