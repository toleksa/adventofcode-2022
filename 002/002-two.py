import sys
import os

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} <file>')
    exit(1)

file=sys.argv[1]

if not os.path.exists(file):
    print(f'ERR: file {file} not found')
    exit(2)

results = {'AX':3,'AY':4,'AZ':8,
           'BX':1,'BY':5,'BZ':9,
           'CX':2,'CY':6,'CZ':7}
sum=0
with open(file) as file:
    for line in file:
        line=line.rstrip()
        print(line)
        args = line.split()
        score=results[args[0]+args[1]]
        print(score)
        sum+=score
print(sum)

