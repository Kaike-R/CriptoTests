def test(chave):
    lista = [chave.count('0'), chave.count('1'), chave.count('2'), chave.count('3'),chave.count('4'),chave.count('5'),
         chave.count('6'),chave.count('7'),chave.count('8'),chave.count('9'),chave.count('A'),chave.count('B'),
         chave.count('C'),chave.count('D'),chave.count('E'),chave.count('F')]
    
    freq = 0  
    for i in range(len(lista)):
        freq = freq + (lista[i] * lista[i])
        X = ((16/5000) * freq) - 5000
    
        if 1.03 < X < 57.4:
            return True
        else:
            return False
        