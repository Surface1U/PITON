
from itertools import *



#  Заводим таблицу размером n+1 строк и 100 столбцов
#Для i-го числа a[i]:   
  #копируете i-строку в следующую  
  #для каждой ячейки i-й строки:
 #    находите её сумму с a[i] (пусть t)
#     и обновляете максимум в ячейке [t%100] следующей строки


#s =0
data = []
data1 = []
f = open("9b.txt","r")
fa = open("9a.txt","r")
data = [int(i) for i in f.read().split()]
dataCop = []
data1Cop = []
data1 = [int(i) for i in fa.read().split()]

for x in data:
    dataCop.append(x)
for x in data1:
    data1Cop.append(x)

fArr = list(map(int,dataCop))
sArr = list(map(int,data1Cop))

aF = [0] * 100
bF = [0] * 100

for x in fArr:
    a1 = aF.copy()
    for i in range(100):
        if aF[i] != 0:
            a1[(i + x) % 100] = max(a1[(i + x) % 100], aF[i] + x)
    a1[x % 100] = max(a1[x % 100], x)
    aF = a1.copy()

for x in sArr:
    a1 = bF.copy()
    for i in range(100):
        if bF[i] != 0:
            a1[(i + x) % 100] = max(a1[(i + x) % 100], bF[i] + x)
    a1[x % 100] = max(a1[x % 100], x)
    bF = a1.copy()

print(aF[50])
print(bF[50])
