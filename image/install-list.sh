#!/bin/bash

while read PKG
do
	echo ""
	echo "============================================================================="
	echo ""
	echo "[<]"
	echo "[<] INSTALLING PACKAGE $PKG"
	echo "[<]"
	# for some fucking reason this fucking setting gets fucking lost
	eval apt-mark hold $BLOCKED >/dev/null
	su -c 'DEBIAN_FRONTEND=noninteractive apt-get install -y --no-remove '$PKG || echo -e "[!]\n[!] ERROR INSTALLING $PKG\n[!]"
	echo "[>]"
	echo "[>] DONE INSTALLING PACKAGE $PKG"
	echo "[>]"
done

echo "[*]"
echo "[*] DONE WITH PACKAGE LIST"
echo "[*]"
