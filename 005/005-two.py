import sys
import os

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} <file>')
    exit(1)

input_file=sys.argv[1]

if not os.path.exists(input_file):
    print(f'ERR: file {file} not found')
    exit(2)

start_file=input_file+"-start"

if not os.path.exists(start_file):
    print(f'ERR: file {file} not found')
    exit(2)

#############################

store = ['store']
def crane(num, start, end):
    if num < 1:
        print(f'ERR: crane({num},{start},{end}) - num smaller than 1, probably error - exiting')
        exit(1)
    temp = []
    for i in range(0,num):
        temp.append(store[start].pop())
    for i in range(0,len(temp)):
        store[end].append(temp[len(temp)-1-i])

counter=1
with open(start_file) as file:
    for line in file:
        line=line.rstrip()
        store.append(list(line))
        counter+=1

print(store)

with open(input_file) as file:
    for line in file:
        line=line.rstrip()
        print(line)
        args = line.split()
        num=int(args[1])
        start=int(args[3])
        end=int(args[5])
        #print(f'crane({num},{start},{end})')
        crane(num,start,end)

print(store)

result=''
for i in range(1,len(store)):
    result+=store[i].pop()

print(result)

