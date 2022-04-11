def countNibbles(key):
    counts = []
    for n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']:
        counts.append(key.count(n))

    return counts


def test(chave):
    fs = countNibbles(chave)

    # X = (16/5000) * sum(from=0, to=15, fs, f_i => f_i ** 2) - 5000
    sum_f = 0  
    for f in fs:
        sum_f += f ** 2
    
    X = ((16/5000) * sum_f) - 5000
    if 1.03 < X < 57.4:
        return True
    
    return False
