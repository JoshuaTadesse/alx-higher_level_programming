#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv1 = sys.argv
    largv = len(argv1)
    if(largv == 2):
        print("{} argument.".format(largv - 1))
    else:
        print("{} arguments:".format(largv - 1))
        for i in range (largv - 1):
            if largv != 1:
                print("{}: {}".format(i + 1, argv1[i + 1]))
