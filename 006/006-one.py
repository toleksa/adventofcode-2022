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

temp = []
counter=4

def shift(c):
    temp.pop(0)
    temp.append(c)

def check():
    if len(temp) == len(set(temp)):
        print(counter)
        #exit(0)
        return True

answer=0
with open(file) as file:
    for line in file:
        temp = []
        counter=4
        line=line.rstrip()
        for i in range(0,4):
            temp.append(line[i])
        check()

        for i in range(4,len(line)):
            counter+=1
            shift(line[i])
            print(temp)
            if check():
                break

