import math


def insert(vetor, n):
    for i in range(2, n):
        chave = vetor[i]
        j = i - 1
        while j >= 1 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j =- 1
        vetor[j + 1] = chave


def select(vetor, n):
    for i in range(1, n-1):
        min = i
        for j in range(i+1, n):
            if vetor[j] < vetor[min]:
                min = j
        vetor[i], vetor[min] = vetor[min], vetor[i]


def merge(vetor, p, r):
    vetor2 = [0] * r
    if p < r:
        q = math.floor((p + r) / 2)
        merge(vetor, p, q)
        merge(vetor, q + 1, r)
        intercala(vetor, p, q, r, vetor2)


def intercala(vetor, p, q, r, vetor2):
    for i in range(p, q):
        vetor2[i] = vetor[i]
    for j in range(q + 1, r):
        vetor2[r + q + 1 - j] = vetor[j]
    i = p
    j = r
    for k in range(p, r):
        if vetor2[i] <= vetor2[j]:
            vetor[k] = vetor2[i]
            i += 1
        else:
            vetor[k] = vetor2[j]
            j -= 1


def quick(vetor, p, r):
    if p < r:
        q = particione(vetor, p, r)
        quick(vetor, p, q - 1)
        quick(vetor, q + 1, r)


def particione(vetor, p, r):
    x = vetor[r]
    i = p - 1
    for j in range(p, r - 1):
        if vetor[j] <= x:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    vetor[i + 1], vetor[r] = vetor[r], vetor[i + 1]
    return i + 1

