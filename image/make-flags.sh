#!/bin/bash

mkdir -p /flags
for N in $(seq 2000 15000)
do
	echo "OOO RULES THE SHELL!!!!8ysadhgvuasdbf7a $N HAHAH123" | sha256sum | awk '{print $1}' > /flags/$N
	chown $N.$N /flags/$N
	chmod 440 /flags/$N
done
