#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv1 = int(sys.argv)
    sum = 0
    i = 1
    for i in argv1:
        sum += argv1[i]
    print("{}".format(sum))
