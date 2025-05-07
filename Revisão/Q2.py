num = int(input("\nInsira um número para calcular seu quadrado: "))

if num == 0 or num == 1: 
    print(f'\nEntrada --> {num}')
    print(f'Saída ----> {num}^2 = {num}\n')
else:
    numOdd = 1
    result = 0
    terms = []
    count = 0
    
    while count < num:
        terms.append(str(numOdd))
        result += numOdd
        numOdd += 2
        count += 1
    
    expressions = ' + '.join(terms)
    print(f'\nEntrada --> {num}')
    print(f'Saída ----> {num}^2 => {expressions} = {result}\n')