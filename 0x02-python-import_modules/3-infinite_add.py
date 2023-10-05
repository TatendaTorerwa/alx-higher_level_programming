#!/usr/bin/python3
if __name__ == "___main__":
    import sys
    sum = 0
    for p in range(len(sys.argv) - 1):
        sum += int(sys.argv[p + 1])
    print("{}".format(sum))
