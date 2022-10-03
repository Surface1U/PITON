
N = 10
fname = input()
try:
    with open(fname,'r') as f:
        lines = list(islice(f, 0, N))
    print('\n'.join(lines))
except FileNotFoundError:
    print('File not found')

    
#частота букав 


wholeFile = open("words.txt", 'r+').read()
lowlet = wholeFile.lower()
letters= list(lowlet)
alpha = list('abcdefghijklmnopqrstuvwxyz')
n = len(letters)
f = float(n)
occurrences = {}
d = {}


    #number of letters
for x in alpha:
    occurrences[x] = letters.count(x)
    for x in occurrences:
        print (x, occurrences[x])
