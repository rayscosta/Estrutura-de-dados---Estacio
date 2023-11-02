def trocar(seq,i):
    aux = seq[i]
    seq[i] = seq[i + 1]
    seq[i + 1] = aux

seq = [1, 15, 6, 22, 30, 17, 4, 8, 3]
troca = 1

while troca:
    troca = 0
    i = 0
    for i in range(len(seq) - 1):
        if seq[i] > seq[i + 1]:
            trocar(seq,i)
            troca = 1

print(seq)    