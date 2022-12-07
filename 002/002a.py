import sys
import os

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} <file>')
    exit(1)

file=sys.argv[1]

if not os.path.exists(file):
    print(f'ERR: file {file} not found')
    exit(2)

values = {'A':1, 'B': 2, 'C': 3,
          'X':1, 'Y': 2, 'Z': 3}

results = {-2:0, -1:6, 0:3, 1:0, 2:6}

sum=0
with open(file) as file:
    for line in file:
        line=line.rstrip()
        print(line)
        args = line.split()
        score=results[values[args[0]]-values[args[1]]]+values[args[1]]
        print(score)
        sum+=score
print(sum)

