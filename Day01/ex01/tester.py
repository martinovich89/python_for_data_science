from array2D import slice_me

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
