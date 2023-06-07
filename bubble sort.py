#Algoritm - Bubble sort:
n = []
cont = 1
for k in range(3):
    t = int(input(f'Digite o tempo do jogador {k+1}: '))
    n.append([cont, t])
    cont += 1
print('\nOrdenando do menor tempo para o maior tempo:')
for _ in range(2):
    for i in range(2):
        if n[i][1] > n[i+1][1]:
            new = n[i+1]
            n[i+1] = n[i]
            n[i] = new
            print(n)
for m in range(3):
    print(n[m][0])
