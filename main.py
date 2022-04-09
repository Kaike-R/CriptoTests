from monobit import monobit
from runs import runs
from thelongrun import thelongrun
from testpoker import test


def main():
    for i in range(1, 27):
        key = input()
        # remove quotes
        key = (key[1:])[:-1]
        # print(chave)
        # print(i)

        print("key", str(i) + ":")
        indent = "  "

        # print(key, end=": ")
        print(indent, "monobit:", monobit(key))

        print(indent, "runs:", runs(key))
        
        print(indent, "poker test:", test(key))
        
        print(indent, "the long run:", thelongrun(key))


main()
