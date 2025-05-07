num = int(input("\nInsira um número com 5 dígitos: "))

num5 = num % 10
num4 = int((num%100)/10)
num3 = int((num%1000)/100)
num2 = int((num%10000)/1000)
num1 = int((num%100000)/10000)

print(f'\nEntrada --> {num}')
print(f'Saída ----> {num1} {num2} {num3} {num4} {num5}\n')