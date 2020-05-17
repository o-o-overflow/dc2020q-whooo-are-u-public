#!/bin/bash

mkdir -p $1
split -l650 <(
	curl https://popcon.ubuntu.com/all-popcon-results.txt.gz | zcat | grep Package |
	egrep -v ": (lib|linux-|python|language|xserver|gnome|firefox|openoffice|thunderbird|gir1.2|nvidia|unity|erlang|texlive|ubuntu|pidgin|nautilus|virtualbox|emodule|x11proto|plasma|kde|rhythmbox|x11|xwayland|wayland|tzdata)" |
	sort -k4 -r -n | head -n65000 | awk '{print $2}'
) $1/packages-
