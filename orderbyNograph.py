import array

__author__ = 'Nilson Perboni Neto'

import time
import random
import math
from random import choice

def insert(A):
    for j in range(1, len(A)):
        chave = A[j]
        i = j - 1
        while (i >= 0) and (A[i] > chave):
            A[i + 1] = A[i]
            i -= 1
        A[i+1] = chave


def select(A):
    for i in range(0, len(A) - 1, 1):
        min = i
        for j in range(i + 1, len(A), 1):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]


def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


def heap(lst):
    ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''

    # in pseudo-code, heapify only called once, so inline it here
    for start in range(int((len(lst)-2)/2), -1, -1):
        siftdown(lst, start, len(lst)-1)

    for end in range(len(lst)-1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        siftdown(lst, 0, end - 1)

    return lst


def siftdown(lst, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break

'''
def quick(vetor):
    quick2(vetor, 0, len(vetor) - 1)


def quick2(vetor, p, r):
    if p <= r:
        q = particione(vetor, p, r)
        quick2(vetor, p, q - 1)
        quick2(vetor, q + 1, r)


def particione(vetor, p, r):
    x = int(vetor[r])
    i = p - 1
    for j in range(p, r):
        if vetor[j] <= x:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    vetor[i + 1], vetor[r] = vetor[r], vetor[i + 1]
    return i + 1
'''

def quick(A):
    quickSort(A, len(A))

def quickSort(arr, elements):
    i = 0
    beg = [0] * (elements + 1)
    end = [0] * (elements + 1)
    beg[0] = 0
    end[0] = elements
    while i >= 0:
        L = beg[i]
        R = end[i] - 1
        if L < R:
            piv = arr[L]
            if (i == elements):
                return 0
            while L < R:
                while arr[R] >= piv and L < R:
                    R -= 1
                if L < R:
                    arr[L] = arr[R]
                    L += 1
                while arr[L] <= piv and L < R:
                    L += 1
                if L < R:
                    arr[R] = arr[L]
                    R -= 1
            arr[L] = piv
            beg[i+1] = L + 1
            end[i+1] = end[i]
            end[i] = L
            i += 1
        else:
            i -= 1


def createVector(size):
    inOrder = range(size)
    inReverse = range(size - 1, -1, -1)
    return inOrder, inReverse


def createRandom(size):
    return random.sample(range(1, size + 1), size)


def test():
    count = 0
    baseVetor = 10
    numIter = 1
    numRdmIter = 1
    tmpSimples0 = []
    tmpSimples1 = []
    tmpSimples2 = []
    tmpSimples3 = []
    tmpSimples4 = []
    tmpSimples5 = []
    tmpSimples6 = []
    tmpSimples7 = []
    tmpSimples8 = []
    tmpSimples9 = []
    rdm = []
    rdmTim = []

    def check(count):
        count += 1
        if not goList == list(ord):
            print (False, count)

    def go(vect, func, save, count):
        goList = list(vect)
        tempo = time.process_time()
        func(goList)
        save.append(time.process_time() - tempo)
        count += 1
        if not goList == list(ord):
            print (False, count)

    for i in range(1, numIter + 1):
        insertTime = []
        selectTime = []
        mergeTime = []
        quickTime = []
        heapTime = []

        ord, rev = createVector(pow(baseVetor, i))

        go(ord, insert, tmpSimples0, count)
        go(ord, select, tmpSimples1, count)
        go(ord, mergeSort, tmpSimples2, count)
        go(ord, quick, tmpSimples3, count)
        go(ord, heap, tmpSimples4, count)

        go(rev, insert, tmpSimples5, count)
        go(rev, select, tmpSimples6, count)
        go(rev, mergeSort, tmpSimples7, count)
        go(rev, quick, tmpSimples8, count)
        go(rev, heap, tmpSimples9, count)

        for j in range(numRdmIter):
            rdmVec = createRandom(pow(baseVetor, i))

            tempo = time.process_time()
            insert(list(rdmVec))
            insertTime.append(time.process_time() - tempo)

            tempo = time.process_time()
            select(list(rdmVec))
            selectTime.append(time.process_time() - tempo)

            tempo = time.process_time()
            mergeSort(list(rdmVec))
            mergeTime.append(time.process_time() - tempo)

            tempo = time.process_time()
            quick(list(rdmVec))
            quickTime.append(time.process_time() - tempo)

            tempo = time.process_time()
            heap(list(rdmVec))
            heapTime.append(time.process_time() - tempo)

        rdmTim.append(insertTime)
        rdmTim.append(selectTime)
        rdmTim.append(mergeTime)
        rdmTim.append(quickTime)
        rdmTim.append(heapTime)

    rng = range(numIter)

    '''
    1 - 3: Medicao de numero de comandos executados
    4 - 6: Tempo de execucao de cada algoritmo
    1 - 4: Vetor ordenado
    2 - 5: Vetor revertido
    3 - 6: Vetor Aleatorio
    '''
    tmp = [tmpSimples0, tmpSimples1, tmpSimples2, tmpSimples3, tmpSimples4, tmpSimples5, tmpSimples6, tmpSimples7,
           tmpSimples8, tmpSimples9]

    print(tmp)
    print(rdm)
    print(rdmTim)

if __name__ == "__main__":
    test()