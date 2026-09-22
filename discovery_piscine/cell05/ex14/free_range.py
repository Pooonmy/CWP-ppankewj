import sys

if len(sys.argv) != 3:
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    step = 1 if start <= end else -1

    num_array = list(range(start, end + step, step))
    print(num_array)
