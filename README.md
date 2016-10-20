# I have abandoned this

The main problem is that OpenSMTPD will only relay email to this filter
server once it has been already received. This makes it impossible to 
check whether a recipient is valid with qmail's dashext syntax and still
being able to deny the email in the ongoing SMTP session. So this approach
only works if you're willing to accept all email and bounce/drop it later.

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
