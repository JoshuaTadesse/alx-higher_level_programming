#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    largv = len(argv)
    if(largv == 2):
        print("{} argument.\n".format(largv))
    else:
        print("{} arguments:\n".format(largv))
        for i in range largv:
            if largv != 1:
                print("{}: {}".format(i + 1, argv[i]))
