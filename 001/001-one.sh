#!/bin/bash

if [ $# -ne 1 ]; then
  echo "usage: $0 <file>"
  exit 1
fi

if [ ! -f "$1" ]; then
  echo "ERR: file $1 not found"
  exit 2
fi

SUM=0
MAX=0
while read -r line; do 
  #echo "line: $line"; 
  if [ "$line" != "" ]; then
    SUM=$((SUM+line))
  else
    if [ "$SUM" -gt "$MAX" ]; then
      MAX=$SUM
    fi
    SUM=0
  fi
done < $1

echo $MAX
