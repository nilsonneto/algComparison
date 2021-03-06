__author__ = 'Nilson Perboni Neto'

import math
import random
import datetime
from random import choice
import matplotlib.pyplot as plt
import timeit

'''
def insert(vetor):
    n = len(vetor)
    interac = 2
    for i in range(2, n):
        chave = vetor[i]
        j = i - 1
        while j >= 1 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j =- 1
            interac += 4
        vetor[j + 1] = chave
        interac += 4
    return interac, vetor
'''

def insert(alist):
    interac = 1
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
            interac += 4

        alist[position]=currentvalue
        interac += 5
    return interac, alist


'''
def select(vetor, n):
    n = len(vetor)
    interac = 2
    for i in range(1, n-1):
        min = int(i)
        for j in range(i+1, n):
            if vetor[j] < vetor[min]:
                min = (j)
                interac += 2
            interac += 3
        vetor[i], vetor[min] = vetor[min], vetor[i]
        interac += 4
    print (vetor)
    return interac, vetor
'''

def select(alist):
    interac = 1
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
                interac += 2
            interac += 2
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
        interac += 6
    return interac, alist

'''
def merge(vetor):
    return merge(vetor, 0, len(vetor) - 1)


def merge(vetor, p, r):
    interac = 3
    vetor2 = [0] * r
    if p < r:
        q = math.floor((p + r) / 2)
        interac += merge(vetor, p, q)[0]
        interac += merge(vetor, q + 1, r)[0]
        interac += intercala(vetor, p, q, r, vetor2)
        interac += 5
    return interac, vetor, vetor2


def intercala(vetor, p, q, r, vetor2):
    interac = 3
    for i in range(p, q):
        vetor2[i] = vetor[i]
        interac += 3
    for j in range(q + 1, r):
        vetor2[r + q + 1 - j] = vetor[j]
        interac += 3
    i = p
    j = r
    for k in range(p, r):
        if vetor2[i] <= vetor2[j]:
            vetor[k] = vetor2[i]
            i += 1
            interac += 5
        else:
            vetor[k] = vetor2[j]
            j -= 1
            interac += 5
    return interac, vetor, vetor2
'''

def merge(alist):
    return mergeSort(alist), alist

def mergeSort(alist):
    '''print("Splitting ",alist)'''
    interac = 4
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        interac += 10

        interac += mergeSort(lefthalf)
        interac += mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
                interac += 3
            else:
                alist[k]=righthalf[j]
                j=j+1
                interac += 3
            k=k+1
            interac += 5

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
            interac += 5

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            interac += 5
    '''print("Merging ",alist)'''
    return interac


def heap(lst):
    interac = 1
    ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''

    # in pseudo-code, heapify only called once, so inline it here
    for start in range((len(lst)-2)/2, -1, -1):
        interac += siftdown(lst, start, len(lst)-1)
        interac += 3

    for end in range(len(lst)-1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        interac += siftdown(lst, 0, end - 1)
        interac += 4

    return interac, lst


def siftdown(lst, start, end):
    root = start
    interac = 2
    while True:
        child = root * 2 + 1
        interac += 2
        if child > end:
            interac += 2
            break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
            interac += 2
        interac += 5
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
            interac += 3
        else:
            interac += 2
            break
    return interac

'''
def quick(vetor):
    quick(vetor, 0, len(vetor) - 1)


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
'''

def quick(a):
    interac = 2
    if len(a) <= 1:
        interac +=2
        return interac, a
    else:
        q = choice(a)
        interac += 5
        intnovo, res = quick([elem for elem in a if elem < q])
        interac += intnovo
        intnovo, res2 = quick([elem for elem in a if elem > q])
        interac += intnovo
        return interac, res + [q] * a.count(q) + res2


def createVector(size):
    inOrder = range(size)
    inReverse = range(size - 1, -1, -1)
    return inOrder, inReverse


def createRandom(size):
    return random.sample(range(1, size + 1), size)

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def test():
    baseVetor = 3
    numIter = 4
    numRdmIter = 1
    resSimples0 = []
    resSimples1 = []
    resSimples2 = []
    resSimples3 = []
    resSimples4 = []
    resSimples5 = []
    resSimples6 = []
    resSimples7 = []
    resSimples8 = []
    resSimples9 = []
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

    for i in range(1, numIter + 1):
        insertRdom = []
        selectRdom = []
        mergeRdom = []
        quickRdom = []
        heapRdom = []
        insertTime = []
        selectTime = []
        mergeTime = []
        quickTime = []
        heapTime = []

        ord, rev = createVector(pow(baseVetor, i))

        resSimples, _ = insert(list(ord))
        resSimples0.append(resSimples)
        wrapped = wrapper(insert, list(ord))
        tmpSimples0.append(timeit.timeit(wrapped, number=10000))

        resSimples, _ = select(list(ord))
        resSimples1.append(resSimples)
        wrapped = wrapper(select, list(ord))
        tmpSimples1.append(timeit.timeit(wrapped, number=10000))

        resSimples, _ = merge(list(ord))
        resSimples2.append(resSimples)
        wrapped = wrapper(merge, list(ord))
        tmpSimples2.append(timeit.timeit(wrapped, number=1000))

        resSimples, _ = quick(list(ord))
        resSimples3.append(resSimples)
        wrapped = wrapper(quick, list(ord))
        tmpSimples3.append(timeit.timeit(wrapped, number=10000))

        resSimples, _ = heap(list(ord))
        resSimples4.append(resSimples)
        wrapped = wrapper(heap, list(ord))
        tmpSimples4.append(timeit.timeit(wrapped, number=10000))

        resSimples, _ = insert(list(rev))
        resSimples5.append(resSimples)
        wrapped = wrapper(insert, list(rev))
        tmpSimples5.append(timeit.timeit(wrapped, number=10000))

        resSimples, _ = select(list(rev))
        resSimples6.append(resSimples)
        wrapped = wrapper(select, list(rev))
        tmpSimples6.append(timeit.timeit(wrapped, number=10000))

        resSimples, _ = merge(list(rev))
        resSimples7.append(resSimples)
        wrapped = wrapper(merge, list(rev))
        tmpSimples7.append(timeit.timeit(wrapped, number=10000))

        resSimples, _ = quick(list(rev))
        resSimples8.append(resSimples)
        wrapped = wrapper(quick, list(rev))
        tmpSimples8.append(timeit.timeit(wrapped, number=10000))

        resSimples, _ = heap(list(rev))
        resSimples9.append(resSimples)
        wrapped = wrapper(heap, list(rev))
        tmpSimples9.append(timeit.timeit(wrapped, number=10000))

        for j in range(numRdmIter):
            rdmVec = createRandom(pow(baseVetor, i))

            numInt, _ = insert(list(rdmVec))
            insertRdom.append(numInt)
            wrapped = wrapper(insert, list(rdmVec))
            insertTime.append(timeit.timeit(wrapped, number=10000))

            numInt, _ = select(list(rdmVec))
            selectRdom.append(numInt)
            wrapped = wrapper(select, list(rdmVec))
            selectTime.append(timeit.timeit(wrapped, number=10000))

            numInt, _ = merge(list(rdmVec))
            mergeRdom.append(numInt)
            wrapped = wrapper(merge, list(rdmVec))
            mergeTime.append(timeit.timeit(wrapped, number=10000))

            numInt, _ = quick(list(rdmVec))
            quickRdom.append(numInt)
            wrapped = wrapper(quick, list(rdmVec))
            quickTime.append(timeit.timeit(wrapped, number=10000))

            numInt, _ = heap(list(rdmVec))
            heapRdom.append(numInt)
            wrapped = wrapper(heap, list(rdmVec))
            heapTime.append(timeit.timeit(wrapped, number=10000))

        rdm.append(insertRdom)
        rdm.append(selectRdom)
        rdm.append(mergeRdom)
        rdm.append(quickRdom)
        rdm.append(heapRdom)
        rdmTim.append(insertRdom)
        rdmTim.append(selectRdom)
        rdmTim.append(mergeRdom)
        rdmTim.append(quickRdom)
        rdmTim.append(heapRdom)


    rng = range(numIter)
    plt.figure(1)
    plt.plot(rng, resSimples0, "b", linewidth=2)
    plt.plot(rng, resSimples1, "r", linewidth=2)
    plt.plot(rng, resSimples2, "g", linewidth=2)
    plt.plot(rng, resSimples3, "c", linewidth=2)
    plt.plot(rng, resSimples4, "k", linewidth=2)

    plt.figure(2)
    plt.plot(rng, resSimples5, "b", linewidth=2)
    plt.plot(rng, resSimples6, "r", linewidth=2)
    plt.plot(rng, resSimples7, "g", linewidth=2)
    plt.plot(rng, resSimples8, "c", linewidth=2)
    plt.plot(rng, resSimples9, "k", linewidth=2)

    plt.figure(3)
    plt.plot(range(numIter), rdm[0:numIter*5:5], "b", linewidth=2)
    plt.plot(range(numIter), rdm[1:numIter*5:5], "r", linewidth=2)
    plt.plot(range(numIter), rdm[2:numIter*5:5], "g", linewidth=2)
    plt.plot(range(numIter), rdm[3:numIter*5:5], "c", linewidth=2)
    plt.plot(range(numIter), rdm[4:numIter*5:5], "k", linewidth=2)

    plt.figure(4)
    plt.plot(rng, tmpSimples0, "b", linewidth=2)
    plt.plot(rng, tmpSimples1, "r", linewidth=2)
    plt.plot(rng, tmpSimples2, "g", linewidth=2)
    plt.plot(rng, tmpSimples3, "c", linewidth=2)
    plt.plot(rng, tmpSimples4, "k", linewidth=2)

    plt.figure(5)
    plt.plot(rng, tmpSimples5, "b", linewidth=2)
    plt.plot(rng, tmpSimples6, "r", linewidth=2)
    plt.plot(rng, tmpSimples7, "g", linewidth=2)
    plt.plot(rng, tmpSimples8, "c", linewidth=2)
    plt.plot(rng, tmpSimples9, "k", linewidth=2)

    plt.figure(6)
    plt.plot(range(numIter), rdmTim[0:numIter*5:5], "b", linewidth=2)
    plt.plot(range(numIter), rdmTim[1:numIter*5:5], "r", linewidth=2)
    plt.plot(range(numIter), rdmTim[2:numIter*5:5], "g", linewidth=2)
    plt.plot(range(numIter), rdmTim[3:numIter*5:5], "c", linewidth=2)
    plt.plot(range(numIter), rdmTim[4:numIter*5:5], "k", linewidth=2)
    '''
    1 - 3: Medicao de numero de comandos executados
    4 - 6: Tempo de execucao de cada algoritmo
    1 - 4: Vetor ordenado
    2 - 5: Vetor revertido
    3 - 6: Vetor Aleatorio
    '''
    plt.show()

if __name__ == "__main__":
    test()