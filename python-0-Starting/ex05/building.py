import sys


def ispunct(c: chr) -> bool:
    """
    Return 1 if character is a punctuation mark.
    Return 0 otherwise.
    """

    if (c in "~.,:;!?\"\'()[]{}<>-_@#$%^&*+=\\|/"):
        return True


def count_and_print(s: str):
    """
    Takes a single string argument and displays the sums of :
    - all its characters
    - its upper-case characters
    - lower-case characters
    - punctuation characters
    - spaces
    - digits
    """

    all_characters = len(s)
    uppercase_characters = sum(1 for c in s if c.isupper())
    lowercase_characters = sum(1 for c in s if c.islower())
    punctuation_characters = sum(1 for c in s if ispunct(c))
    spaces = sum(1 for c in s if c.isspace())
    digits = sum(1 for c in s if c.isdigit())

    print(f"The text contains {all_characters} characters:")
    print(f"{uppercase_characters} upper letters")
    print(f"{lowercase_characters} lower letters")
    print(f"{punctuation_characters} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
    Parse args, call main functions and handle errors
    """

    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if (len(sys.argv) < 2):
            try:
                input_string = input("What is the text to count?\n")
                input_string += "\n"
            except EOFError:
                pass
        else:
            input_string = sys.argv[1]
        count_and_print(input_string)

    except AssertionError as msg:
        print("AssertionError: ", msg)


if __name__ == "__main__":
    main()
