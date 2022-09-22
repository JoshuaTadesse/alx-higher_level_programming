#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    largv = len(argv)
    if(largv == 2):
        print("{} argument.\n".format(largv - 1))
    else:
        print("{} arguments:\n".format(largv - 1))
        for i in range (largv - 1):
            if largv != 1:
                print("{}: {}".format(i + 1, argv[i + 1]))
