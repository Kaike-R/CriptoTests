
def countOnes(key): 
    count = 0

    cases = {
        '0': 0, # 0000
        '1': 1, # 0001
        '2': 1, # 0010
        '3': 2, # 0011
        '4': 1, # 0100
        '5': 2, # 0101
        '6': 2, # 0110
        '7': 3, # 0111
        '8': 1, # 1000
        '9': 2, # 1001
        'A': 2, # 1010
        'B': 3, # 1011
        'C': 2, # 1100
        'D': 3, # 1101
        'E': 3, # 1110
        'F': 4, # 1111
    }

    for c in key: 
        count += cases[c]

    return count


def monobit(key):
    nOnes = countOnes(key)
    # print(nOnes, end=" -> ")
    return nOnes > 9654 and nOnes < 10346 
