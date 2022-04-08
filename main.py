from monobit import monobit
from runs import runs
from testpoker import test

def main():
    for i in range(0, 26):
        key = input()
        # remove quotes
        key = (key[1:])[:-1]
        # print(chave)
        # print(i)

        print(i, end=": ")
        # print(key, end=": ")
        print("monobit", monobit(key), end=", ")

        print("runs", runs(key))
        
        print("poker test", test(key))

        print("thelongrun", thelongrun(key))
main()
