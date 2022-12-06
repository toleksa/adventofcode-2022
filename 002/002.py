import sys
import os

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} <file>')
    exit(1)

file=sys.argv[1]

if not os.path.exists(file):
    print(f'ERR: file {file} not found')
    exit(2)

values = {'X':1, 'Y': 2, 'Z': 3}

def battle(opponent, me):
    #TODO: should be better way than hardcoding everything with ifs
    if opponent == 'A':
        if me == 'X':
            return 3
        if me == 'Y':
            return 6
        if me == 'Z':
            return 0
    if opponent == 'B':
        if me == 'X':
            return 0
        if me == 'Y':
            return 3
        if me == 'Z':
            return 6
    if opponent == 'C':
        if me == 'X':
            return 6
        if me == 'Y':
            return 0
        if me == 'Z':
            return 3
    print(f"ERR: sum ting wong for params: {opponent}:{me}")
    exit(3)

sum=0
with open(file) as file:
    for line in file:
        line=line.rstrip()
        print(line)
        args = line.split()
        print(args[0])
        print(args[1])
        score=battle(args[0],args[1]) + values[args[1]]
        print(score)
        sum+=score
print(sum)

