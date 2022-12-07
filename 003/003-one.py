import sys
import os
import string

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} <file>')
    exit(1)

file=sys.argv[1]

if not os.path.exists(file):
    print(f'ERR: file {file} not found')
    exit(2)

#############################

sum=0
with open(file) as file:
    for line in file:
        line=line.rstrip()
        print(line)
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        firstset = set()
        for c in firstpart:
            firstset.update(c)
        secondset = set()
        for c in secondpart:
            secondset.update(c)

        value=ord( list(set(firstset).intersection(secondset)) [0]   )-96
        value = value if value > 0 else value + 58
        print(value)
        sum+=value

print(sum)

