def suc(n):
    return n+1
def pred(n):
    return n-1
def soma(x,y):
    if x == 0:
        return y
    if y == 0:
        return x
    else:
        return soma(suc(x), pred(y))
x = int(input("\nDigite o valor de 'x': "))
y = int(input("Digite o valor de 'y': "))

results = soma(x,y)
print(f'\nx = {x}')
print(f'-> Sucessor(x) = {suc(x)}\n')
print(f'y = {y}')
print(f'-> Predecessor(y) = {pred(y)}\n')
print(f'Soma(x, y) => {suc(x)} + {pred(y)} = {results}\n')