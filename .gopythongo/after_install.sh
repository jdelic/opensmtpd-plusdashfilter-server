#!/bin/sh

test -e /etc/systemd/system/plusdashfilter.service || exit 1;

if ! grep -q plusdashfilter /etc/group; then
    groupadd plusdashfilter
fi

if ! grep -q plusdashfilter /etc/passwd; then
    useradd -g plusdashfitler -s /bin/false -d /usr/local/plusdashfilter plusdashfilter
fi

systemctl --system daemon-reload
systemctl start plusdashfilter

