from monobit import monobit
from runs import runs
from thelongrun import thelongrun

def main():
    for i in range(0, 26):
        key = input()
        # remove quotes
        key = (key[1:])[:-1]
        # print("len", len(key))
        # print(chave)
        # print(i)

        print(i, end=": ")
        # print(key, end=": ")
        print("monobit", monobit(key), end=", ")

        print("runs", runs(key), end=", ")
        
        print("thelongrun", thelongrun(key))
        

main()
