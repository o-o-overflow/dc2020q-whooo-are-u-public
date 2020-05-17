#!/bin/bash

N=2000
while read BIN
do
	grep -q "^$(basename $BIN)$" /root/pwn-college-solves.txt && echo "[ ] SKIPPING $BIN" && continue
	grep -q "^$(basename $BIN)$" /root/critical-bins.txt && echo "[ ] SKIPPING $BIN" && continue
	echo "[*] CHOWNING $BIN to $N"

	N=$(($N+1))
	chown $N.$N $BIN
	chmod ug+s $BIN
done
