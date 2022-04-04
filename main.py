from monobit import monobit


def main():
    for i in range(0, 26):
        key = input()
        # remove quotes
        key = (key[1:])[:-1]
        # print(chave)
        # print(i)

        print(i, end=": ")
        # print(key, end=": ")
        print(monobit(key))


main()
