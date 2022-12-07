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
lines = []
counter=0
with open(file) as file:
    for line in file:
        line=line.rstrip()
        lines.append(line)
        counter+=1
        print(line)
        if counter == 3:
            result=set(lines[0]) & set(lines[1]) & set(lines[2])
            value=ord(list(result)[0])-96
            value = value if value > 0 else value + 58
            print(str(result) + " " + str(value))
            sum+=value
            counter=0
            lines=[]
print(sum)

