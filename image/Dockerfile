from ubuntu:18.04

arg CACHE=1
run apt-get update
run apt-get install -y curl gzip gawk coreutils bash

# disable graphical stuff
arg BLOCKED="libx11* libwayland* libxcb* libgtk* libgnome* libqt* libkde* xserver* x11* xwayland wayland* python* kernel* metaphlan2-data libghc-* ruby-* node-* golang-* r-* php-* gir1.2-* libjs-* gnome-* lua-* linux-*"
run apt-mark hold $BLOCKED

# generate installer scripts
copy generate_packages.sh /root
run /root/generate_packages.sh  /root/packages
copy install-list.sh /root

# merry christmas
run /root/install-list.sh < /root/packages/packages-aa
run /root/install-list.sh < /root/packages/packages-ab
run /root/install-list.sh < /root/packages/packages-ac
run /root/install-list.sh < /root/packages/packages-ad
run /root/install-list.sh < /root/packages/packages-ae
run /root/install-list.sh < /root/packages/packages-af
run /root/install-list.sh < /root/packages/packages-ag
run /root/install-list.sh < /root/packages/packages-ah
run /root/install-list.sh < /root/packages/packages-ai
run /root/install-list.sh < /root/packages/packages-aj
run /root/install-list.sh < /root/packages/packages-ak
run /root/install-list.sh < /root/packages/packages-al
run /root/install-list.sh < /root/packages/packages-am
run /root/install-list.sh < /root/packages/packages-an
run /root/install-list.sh < /root/packages/packages-ao
run /root/install-list.sh < /root/packages/packages-ap
#run /root/install-list.sh < /root/packages/packages-aq # some fucked up shit in here
run /root/install-list.sh < /root/packages/packages-ar
run /root/install-list.sh < /root/packages/packages-as
run /root/install-list.sh < /root/packages/packages-at
run /root/install-list.sh < /root/packages/packages-au
run /root/install-list.sh < /root/packages/packages-av
run /root/install-list.sh < /root/packages/packages-aw
run /root/install-list.sh < /root/packages/packages-ax
run /root/install-list.sh < /root/packages/packages-ay
run /root/install-list.sh < /root/packages/packages-az
run /root/install-list.sh < /root/packages/packages-ba
run /root/install-list.sh < /root/packages/packages-bb
run /root/install-list.sh < /root/packages/packages-bc
run /root/install-list.sh < /root/packages/packages-bd
run /root/install-list.sh < /root/packages/packages-be
run /root/install-list.sh < /root/packages/packages-bf
run /root/install-list.sh < /root/packages/packages-bg
run /root/install-list.sh < /root/packages/packages-bh
run /root/install-list.sh < /root/packages/packages-bi
run /root/install-list.sh < /root/packages/packages-bj
run /root/install-list.sh < /root/packages/packages-bk
run /root/install-list.sh < /root/packages/packages-bl
run /root/install-list.sh < /root/packages/packages-bm
run /root/install-list.sh < /root/packages/packages-bn
run /root/install-list.sh < /root/packages/packages-bo
run /root/install-list.sh < /root/packages/packages-bp
run /root/install-list.sh < /root/packages/packages-bq
run /root/install-list.sh < /root/packages/packages-br
run /root/install-list.sh < /root/packages/packages-bs
run /root/install-list.sh < /root/packages/packages-bt
run /root/install-list.sh < /root/packages/packages-bu
run /root/install-list.sh < /root/packages/packages-bv
run /root/install-list.sh < /root/packages/packages-bw
#run /root/install-list.sh < /root/packages/packages-bx # alright, that's plenty big enough
#run /root/install-list.sh < /root/packages/packages-by
#run /root/install-list.sh < /root/packages/packages-bz
#run /root/install-list.sh < /root/packages/packages-ca
#run /root/install-list.sh < /root/packages/packages-cb
#run /root/install-list.sh < /root/packages/packages-cc
#run /root/install-list.sh < /root/packages/packages-cd
#run /root/install-list.sh < /root/packages/packages-ce
#run /root/install-list.sh < /root/packages/packages-cf
#run /root/install-list.sh < /root/packages/packages-cg
#run /root/install-list.sh < /root/packages/packages-ch
#run /root/install-list.sh < /root/packages/packages-ci
#run /root/install-list.sh < /root/packages/packages-cj
#run /root/install-list.sh < /root/packages/packages-ck
#run /root/install-list.sh < /root/packages/packages-cl
#run /root/install-list.sh < /root/packages/packages-cm
#run /root/install-list.sh < /root/packages/packages-cn
#run /root/install-list.sh < /root/packages/packages-co
#run /root/install-list.sh < /root/packages/packages-cp
#run /root/install-list.sh < /root/packages/packages-cq
#run /root/install-list.sh < /root/packages/packages-cr
#run /root/install-list.sh < /root/packages/packages-cs
#run /root/install-list.sh < /root/packages/packages-ct
#run /root/install-list.sh < /root/packages/packages-cu
#run /root/install-list.sh < /root/packages/packages-cv
#run /root/install-list.sh < /root/packages/packages-cw
#run /root/install-list.sh < /root/packages/packages-cx
#run /root/install-list.sh < /root/packages/packages-cy
#run /root/install-list.sh < /root/packages/packages-cz
#run /root/install-list.sh < /root/packages/packages-da
#run /root/install-list.sh < /root/packages/packages-db
#run /root/install-list.sh < /root/packages/packages-dc
#run /root/install-list.sh < /root/packages/packages-dd
#run /root/install-list.sh < /root/packages/packages-de
#run /root/install-list.sh < /root/packages/packages-df
#run /root/install-list.sh < /root/packages/packages-dg
#run /root/install-list.sh < /root/packages/packages-dh
#run /root/install-list.sh < /root/packages/packages-di
#run /root/install-list.sh < /root/packages/packages-dj
#run /root/install-list.sh < /root/packages/packages-dk
#run /root/install-list.sh < /root/packages/packages-dl
#run /root/install-list.sh < /root/packages/packages-dm
#run /root/install-list.sh < /root/packages/packages-dn
#run /root/install-list.sh < /root/packages/packages-do
#run /root/install-list.sh < /root/packages/packages-dp
#run /root/install-list.sh < /root/packages/packages-dq
#run /root/install-list.sh < /root/packages/packages-dr
#run /root/install-list.sh < /root/packages/packages-ds
#run /root/install-list.sh < /root/packages/packages-dt
#run /root/install-list.sh < /root/packages/packages-du
#run /root/install-list.sh < /root/packages/packages-dv

# cleanup
# also need to get rid of lupin-support 

# tboot and lupin-support are also fuckers, but they break apt if you remove them
run DEBIAN_FRONTEND=noninteractive dpkg -P libpam-cgfs edb apt-show-versions maildrop courier-base biosdevname courier-ssl courier-maildrop resolvconf matlab-support courier-webadmin sqwebmail courier-mlm courier-pcp courier-ldap || echo sigh
run chmod o-r /tmp /var/tmp /dev/shm
run find / -type f -perm -4000 | xargs chmod ug-s

# service stuff
copy service.conf /service.conf
copy banner_fail /banner_fail
copy wrapper /wrapper
run DEBIAN_FRONTEND=noninteractive apt-get install -y socat xinetd rsyslog file || echo sigh
expose 5000
#cmd ["/usr/bin/socat", "tcp-l:5000,fork,max-children=1,backlog=10,reuseaddr", "exec:/bin/bash -li,pty,stderr,setsid,sigint,sane"]
#cmd ["/usr/sbin/xinetd", "-d", "-dontfork", "-f", "/service.conf"]
cmd ["/usr/sbin/xinetd", "-syslog", "local0", "-dontfork", "-f", "/service.conf"]

# and add suid!
run find /bin/ /sbin/ /usr/bin/ /usr/sbin/ /usr/games -type f -exec file \{\} \; 2>/dev/null | grep ELF | awk '{print $1}' | tr -d : | sort > /root/installed-bins.txt && wc -l /root/installed-bins.txt
copy pwn-college-solves.txt /root
copy critical-bins.txt /root
copy chown.sh /root
run /root/chown.sh < /root/installed-bins.txt
run rm -rf /root/*

# make the flags
copy make-flags.sh /root
run /root/make-flags.sh
run rm -rf /root/*
