
def binFromHex(key): 
    hex = ''

    cases = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }

    for c in key: 
        hex += cases[c]

    return hex

def countRuns(key):
    runs = [[0] * 6, [0] * 6]

    key = binFromHex(key)

    prev = ''
    runLen = 0
    for (i, b) in enumerate(key):
        if b == prev:
            runLen += 1
        # first bit 
        elif runLen == 0:
            runLen += 1
        # run end 
        else: 
            # len > 6 counts as a 6-digit len
            runs[int(prev)][min(runLen, 6) - 1] += 1
            runLen = 1

        prev = b
    
    
    # if key ended, last run ended as well
    runs[int(b)][min(runLen, 6) - 1] += 1

    return runs


def runs(key):
    intervals = [
        [2267, 2733], 
        [1079, 1421], 
        [502, 748], 
        [223, 402], 
        [90, 223], 
        [90, 223], 
    ]

    nRuns = countRuns(key)
    # print(nRuns)

    for b in [0, 1]:
        for (i, run) in enumerate(nRuns[b]):
            if run < intervals[i][0] or run > intervals[i][1]:
                return False

    return True
