#!/bin/sh

if ! grep -q plusdashfilter /etc/group; then
    groupadd plusdashfilter
fi

if ! grep -q plusdashfilter /etc/passwd; then
    useradd -g plusdashfilter -s /bin/false -d /usr/local/plusdashfilter plusdashfilter
fi

