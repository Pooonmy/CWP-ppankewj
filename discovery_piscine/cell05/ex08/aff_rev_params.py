import sys

if len(sys.argv) < 3:
    print("none")
else:
    reversed_args = sys.argv[:0:-1]
    print(" ".join(reversed_args))
