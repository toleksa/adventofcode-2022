import sys
import os

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} <file>')
    exit(1)

file=sys.argv[1]

if not os.path.exists(file):
    print(f'ERR: file {file} not found')
    exit(2)

#############################

counter=0
with open(file) as file:
    for line in file:
        line=line.rstrip()
        print(line)
        first, second = line.split(",")
        print(first)
        print(second)
        first_min, first_max = first.split("-")
        second_min, second_max = second.split("-")
        if (int(first_min) <= int(second_min) and int(first_max) >= int(second_max)) or (int(second_min) <= int (first_min) and int(second_max) >= int(first_max)):
            counter+=1

print(counter)
