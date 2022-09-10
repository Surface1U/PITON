#1
sutki = int(1440)
n = int(input('n='))%sutki
print(n//60,n%60,sep=':')

#2
a = int(input())
b = int(input())
if a < b:
    print(a)
else:
    print(b)



#3
hours = int(input('hours='))
minutes = int(input('minutes='))
seconds = int(input('seconds ='))

hours2 = int(input('hours2='))
minutes2 = int(input('minutes2='))
seconds2 = int(input('seconds2='))

allsec = int(hours*360+minutes*60+seconds)
allsec2 = int(hours2*360+minutes2*60+seconds2)

print(allsec2 - allsec)

#4

n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
for i in range(n - 1):
    sum -= int(input())
print(sum)

#5
s = input()
a = s[:s.find('h')]
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)

#6
n = int(input('n='))
s = 0
while n!=0:
    s = s+n
    n= int(input())
else:
    print('end')
    print(s)

#7
a = [int(i) for i in input().split()]
num_distinct = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        num_distinct += 1
print(num_distinct)

#8
def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)


reverse()

#9
n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'
    a[i][n - i - 1] = '*'
for row in a:
    print(' '.join(row))
    
# #10
 students = [{input() for j in range(int(input()))} for i in range(int(input()))]
 known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
 print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
 print(len(known_by_someone), *sorted(known_by_someone), sep='\n')
    
#11
Action_Permissions = {'read':'R','write':'W','execute':'X'}
file_permissions = {}
for i in range(int(input())):
    file,*permissons = input().split()
    file_permissions[file] = set(permissons)

for i in range (int(input())):
    action,file = input().split()
    if Action_Permissions[action] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')

