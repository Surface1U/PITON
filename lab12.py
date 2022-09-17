
N = 10
fname = input()
try:
    with open(fname,'r') as f:
        lines = list(islice(f, 0, N))
    print('\n'.join(lines))
except FileNotFoundError:
    print('File not found')
