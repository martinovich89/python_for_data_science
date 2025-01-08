import sys


try:
    assert len(sys.argv) <= 2, "more than one argument is provided"

    if (len(sys.argv) < 2):
	    exit()
    n = int(sys.argv[1])
    s = ""
    if ((n % 2) == 0):
        s = "Even."
    else:
        s = "Odd."
    print(f"I'm {s}\n")
except AssertionError as msg:
    print("AssertionError:", msg)
    print("\n")
except ValueError:
    print("AssertionError: argument is not an integer\n")
