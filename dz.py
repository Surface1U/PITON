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

#10.1
n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == 'YES':
        possible_nums &= guess
    else:
        possible_nums &= all_nums - guess
 
print(' '.join([str(x) for x in sorted(possible_nums)]))

#10.2
print(len(set(input().split()) & set(input().split())))

    
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

#11.1
num_votes = {}
for _ in range(int(input())):
    candidate, votes = input().split()
    num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)
 
for candidate, votes in sorted(num_votes.items()):
    print(candidate, votes)
    
    
#11.2

def height(man):
    if man not in p_tree:
        return 0
    else:
        return 1 + height(p_tree[man])
 
p_tree = {}
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent
 
heights = {}
for man in set(p_tree.keys()).union(set(p_tree.values())):
    heights[man] = height(man)
 
for key, value in sorted(heights.items()):
    print(key, value)
