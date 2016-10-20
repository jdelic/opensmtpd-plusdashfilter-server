# I have abandoned this

Since I will need to rewrite SMTP envelope data (`RCPT TO`) as well and 
OpenSMTPD does not allow that currently.

You probably want to use [opensmtpd-extras-plusdash](https://github.com/jdelic/opensmtpd-plusdashfilter) 
instead if OpenSMTPD extends its filter API to allow filters to rewrite
envelope data.

# OpenSMTPD-plusdashfilter

So it turns out that OpenSMTPD, for boneheaded reasons, does not support
`-` as a email *mailext* separator, but only supports `+`. For
compatibility with *qmail*, for example, this project provides a
SMTP filter daemon which can be used through OpenSMTPD's tagging
mechanism to replace all dashes in an email address with pluses.

This way "user-ext@example.com" becomes "user+ext@example.com" creating
compatibility with other MTAs.

## How do I use this?

TODO: write this part :)
