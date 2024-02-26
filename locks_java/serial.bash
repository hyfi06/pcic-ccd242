#!/bin/bash

javac -d bin src/Serial.java

run_and_save() {
  numero=$1
  java -cp bin Serial 1000 >"serial_$numero.txt"
}

export -f run_and_save

for i in $(seq 1 10); do
  run_and_save $i &
done

# seq 1 10 | parallel run_and_save {}

# cat serial_*.txt >serial_final.txt
# rm serial_*.txt
