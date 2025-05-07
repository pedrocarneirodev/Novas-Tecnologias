discs = int(input("Digite o número de discos: "))
movements = 0
def printHanoi(discs):
    count = discs-1
    while count != -1:
        print(f'[{discs - count}]\t|\t|')
        count -= 1

def hanoi(discs, origin, destination, aux):
    if discs == 1:
        print(f"Mova o disco 1 de {origin} para {destination}")
    else:
        hanoi(discs-1, origin, aux, destination)
        print(f'Mova o disco {discs} de {origin} para {destination}')
        hanoi(discs-1, aux, destination, origin)
        
print(" A\tB\tC\n")
printHanoi(discs)
print("=================")
print("\nSequência de movimentos: ")
hanoi(discs, 'A', 'C', 'B')