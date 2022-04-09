from monobit import monobit as monobittest, countOnes
from testpoker import test as pokertest, countNibbles
from runs import runs as runstest, countRuns
from thelongrun import thelongrun as longruntest


def print_monobittest(key, indent, level):
    monobit_ok = monobittest(key)
    num_monobits = countOnes(key)

    print(indent * level, "monobit test:")
    level += 1
    print(indent * level, "passed:", monobit_ok)
    print(indent * level, "number of monobits:", num_monobits)

    return monobit_ok


def print_pokertest(key, indent, level):
    poker_ok = pokertest(key)
    nibbles_counts = countNibbles(key)

    print(indent * level, "poker test:")
    level += 1
    print(indent * level, "passed:", poker_ok)
    print(indent * level, "nibble counts:", nibbles_counts)

    return poker_ok


def print_runstest(key, indent, level):
    runs_ok = runstest(key)
    print(indent * level, "runs test:")
    level += 1
    print(indent * level, "passed:", runs_ok)
    print(indent * level, "runs counts:")
    level += 1
    runsCounts = countRuns(key)
    for i in [0, 1]:
        print(indent * level, str(i) + ":", runsCounts[i])

    return runs_ok
    

def print_longruntest(key, indent, level):
    longrun_ok = longruntest(key)
    print(indent * level, "long run test:")
    level += 1
    print(indent * level, "passed:", longrun_ok)

    return longrun_ok


def print_tests(key, indent, level):
    monobit_ok = print_monobittest(key, indent, level)
        
    poker_ok = print_pokertest(key, indent, level)

    runs_ok = print_runstest(key, indent, level)
    
    longrun_ok = print_longruntest(key, indent, level)

    all_ok = all([monobit_ok, poker_ok, runs_ok, longrun_ok])    
    print(indent * level, "is random:", all_ok)


def main():
    for i in range(1, 27):
        key = input()
        # remove quotes
        key = (key[1:])[:-1]
        # print(chave)
        # print(i)

        print("key", str(i) + ":")
        indent = "  "
        level = 1

        print_tests(key, indent, level)


main()
