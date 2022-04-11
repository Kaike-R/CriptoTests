from monobit import monobit as monobittest, countOnes
from testpoker import test as pokertest, countNibbles
from runs import runs as runstest, countRuns
from thelongrun import thelongrun as longruntest


def print_monobittest(key, indent, level):
    monobit_ok = monobittest(key)
    print("monobit=" + str(monobit_ok))

    return monobit_ok


def print_pokertest(key, indent, level):
    poker_ok = pokertest(key)
    print("poker_test=" + str(poker_ok))

    return poker_ok


def print_runstest(key, indent, level):
    runs_ok = runstest(key)
    print("runs=" + str(runs_ok))

    return runs_ok
    

def print_longruntest(key, indent, level):
    longrun_ok = longruntest(key)
    print("long_run=" + str(longrun_ok))

    return longrun_ok


def print_tests(key, indent, level):
    monobit_ok = print_monobittest(key, indent, level)
        
    poker_ok = print_pokertest(key, indent, level)

    runs_ok = print_runstest(key, indent, level)
    
    longrun_ok = print_longruntest(key, indent, level)

    all_ok = all([monobit_ok, poker_ok, runs_ok, longrun_ok])    

    return all_ok


def main():
    tests_results = []
    for i in range(1, 27):
        key = input()

        # remove quotes
        key = (key[1:])[:-1]

        print("chave=" + str(i))
        indent = "  "
        level = 1

        print_tests(key, indent, level)
        print("----------------")


main()
