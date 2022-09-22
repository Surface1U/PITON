#использование алгоритма Кадане(в первый раз слышу, честно) в действии

from itertools import *

def maxsum(iterable):
    maxsofar = maxendinghere = 0
    for x in iterable:
        if((maxendinghere + x)%100 == 50):
            maxendinghere = max(maxendinghere+x,0)
        maxsofar = max(maxsofar,maxendinghere)
    return maxsofar

def justsum(iterable):
    maxsofar = maxendinghere = 0
    for x in iterable:
        maxendinghere = max(maxendinghere+x,0)
        maxsofar = max(maxsofar,maxendinghere)
    return maxsofar


#s =0
data = []
data1 = []
f = open("C:/Users/Alexander/Desktop/9b.txt","r")
y = int(f.readline())
fa = open("C:/Users/Alexander/Desktop/9a.txt","r")
y1 = int(fa.readline())
data = [int(i) for i in f.read().split()]
data1 = [int(i) for i in fa.read().split()]

print("Для файла b:",maxsum(data),":","Максимальная сумма",justsum(data))
print("Для файла a:",maxsum(data1),":","\tМаксимальная сумма",justsum(data1))





