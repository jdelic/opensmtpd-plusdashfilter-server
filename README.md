You probably want to use [opensmtpd-plusdashfilter](https://github.com/jdelic/opensmtpd-plusdashfilter) instead.

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
