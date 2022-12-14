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

cycles = [[0,0,0,"start"]]
cpu=1

with open(file) as file:
    for line in file:
        line=line.rstrip()
        print(line)
        if line.startswith('noop'):
            cycles.append([len(cycles),cpu,len(cycles)*cpu,'noop'])
            
        elif line.startswith('addx'):
            args = line.split()
            cycles.append([len(cycles),cpu,len(cycles)*cpu,line])
            cycles.append([len(cycles),cpu,len(cycles)*cpu,""])
            cpu+=int(args[1])
        else:
            print(f"ERR: unrecognized command: {line}")
            exit(1)

cycles.append([len(cycles),cpu,len(cycles)*cpu,"end"])
for cycle in cycles:
    print(cycle)

if len(cycles)>=220:
    result=0
    for i in [ 20, 60, 100, 140, 180, 220 ]:
        res=int(cycles[i][2])
        print(f'{i}: {res}')
        result+=res

print(result)

