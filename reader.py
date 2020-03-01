import globale as g
import verbose as v


def checkArg(argv):
    nb_arg = len(argv)
    if nb_arg > 1: 
        if argv[1] == "-h" :
            v.ft_usage()
        if nb_arg == 3 and argv[2] == "-v":
            g.verbose = 1
        equation = argv[1]
    else :
        v.ft_usage()
    return equation

def reader(argv):
    result = checkArg(argv)
    # equation = checkSynthax()
    return result
