import sys
from ft_filter import ft_filter


def main():
    """
    A program that accepts two arguments : a string(S) and an integer(N).
    The program should output a list of words from S \
    that have a length greater than N.
    """

    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        S = sys.argv[1]
        N = sys.argv[2]
        N = int(N)
        assert isinstance(S, str) \
            and isinstance(N, int), \
            "the arguments are bad"

        input_list = S.split(" ")
        if (N % 2 == 0):
            gen = ft_filter(lambda x: len(x) > N, input_list)
            output_list = list(gen)
        else:
            output_list = [word for word in input_list if len(word) > N]

        print(output_list)

    except ValueError:
        print("AssertionError: the arguments are bad")
    except AssertionError as msg:
        print("AssertionError:", msg)


if __name__ == "__main__":
    main()
