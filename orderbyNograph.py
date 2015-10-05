__author__ = 'Nilson Perboni Neto'

import time
import random
from random import choice

def insert(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue
    return alist


def select(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    return alist


def merge(alist):
    mergeSort(alist)
    return alist

def mergeSort(alist):
    '''print("Splitting ",alist)'''
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
    '''print("Merging ",alist)'''


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


def quick(a):
    if len(a) <= 1:
        return a
    else:
        q = choice(a)
        res = quick([elem for elem in a if elem < q])
        res2 = quick([elem for elem in a if elem > q])
        return res + [q] * a.count(q) + res2


def createVector(size):
    inOrder = range(size)
    inReverse = range(size - 1, -1, -1)
    return inOrder, inReverse


def createRandom(size):
    return random.sample(range(1, size + 1), size)


def test():
    baseVetor = 10
    numIter = 4
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

    for i in range(1, numIter + 1):
        insertTime = []
        selectTime = []
        mergeTime = []
        quickTime = []
        heapTime = []

        ord, rev = createVector(pow(baseVetor, i))

        tempo = time.process_time()
        insert(list(ord))
        tmpSimples0.append(time.process_time() - tempo)

        tempo = time.process_time()
        select(list(ord))
        tmpSimples1.append(time.process_time() - tempo)

        tempo = time.process_time()
        merge(list(ord))
        tmpSimples2.append(time.process_time() - tempo)

        tempo = time.process_time()
        quick(list(ord))
        tmpSimples3.append(time.process_time() - tempo)

        tempo = time.process_time()
        heap(list(ord))
        tmpSimples4.append(time.process_time() - tempo)

        tempo = time.process_time()
        insert(list(rev))
        tmpSimples5.append(time.process_time() - tempo)

        tempo = time.process_time()
        select(list(rev))
        tmpSimples6.append(time.process_time() - tempo)

        tempo = time.process_time()
        merge(list(rev))
        tmpSimples7.append(time.process_time() - tempo)

        tempo = time.process_time()
        quick(list(rev))
        tmpSimples8.append(time.process_time() - tempo)

        tempo = time.process_time()
        heap(list(rev))
        tmpSimples9.append(time.process_time() - tempo)

        for j in range(numRdmIter):
            rdmVec = createRandom(pow(baseVetor, i))

            tempo = time.process_time()
            insert(list(rdmVec))
            insertTime.append(time.process_time() - tempo)

            tempo = time.process_time()
            select(list(rdmVec))
            selectTime.append(time.process_time() - tempo)

            tempo = time.process_time()
            merge(list(rdmVec))
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