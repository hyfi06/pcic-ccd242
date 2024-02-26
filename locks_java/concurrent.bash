#!/bin/bash

javac -d bin src/Concurrent.java

run_and_save() {
  cores=$1
  numero=$2
  java -cp bin Concurrent $1 1000 >"conc_1k_$cores-$numero.txt"
}

export -f run_and_save

for j in $(seq 2 2 64); do
  echo $(date +%F_%T) run with $j cores start
  for i in $(seq 1 10); do
    run_and_save $j $i
  done
  cat conc_1k_$j-*.txt >conc_1k_$j.txt
  rm conc_1k_$j-*.txt
  echo $(date +%F_%T) run with $j cores finished
done

# seq 1 10 | parallel run_and_save {}

# cat serial_*.txt >serial_final.txt
# rm serial_*.txt
