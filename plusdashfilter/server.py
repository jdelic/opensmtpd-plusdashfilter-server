#!/usr/bin/env python3

import argparse
import asyncore
import daemonize
import email.utils
import smtplib
from smtpd import SMTPServer


_args = None


class PlusDashFilterServer(SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        rewritten_rcptros = []

        # replace all "-" in email user parts with "+" for OpenSMTPD
        for recipient in rcpttos:
            name_address = email.utils.parseaddr(recipient)
            if name_address[1].count('@') == 1 and name_address[1].split('@')[0].count('-') > 0:
                new_address = '%s@%s' % (name_address[1].split('@')[0].replace('-', '+'),
                                         name_address[1].split('@')[1])
                name_address = (name_address[0], new_address)
                rewritten_rcptros.append(email.utils.formataddr(name_address))
            else:
                rewritten_rcptros.append(recipient)

        # now send the mail back to be processed
        with smtplib.SMTP(_args.output_ip, _args.output_port) as smtp:
            smtp.sendmail(mailfrom, rewritten_rcptros, data)


def run():
    server = PlusDashFilterServer((_args.input_ip, _args.input_port), None)
    asyncore.loop()


def main():
    global _args
    parser = argparse.ArgumentParser(
                description='This is a SMTP daemon that is used through OpenSMTPD configuration '
                            'to filter email and replace "-" with "+" thereby making OpenSMTPD '
                            'compatible with more widely deployed MTAs like qmail.'
             )

    grp_daemon = parser.add_argument_group('Daemon options')
    grp_daemon.add_argument('-p', '--pidfile', dest='pidfile', default='./opensmtpd-plusdashfilter.pid',
                            help="Path to a pidfile")
    grp_daemon.add_argument('-u', '--user', dest='user', default=None, help='Drop privileges and switch to this user')
    grp_daemon.add_argument('-g', '--group', dest='group', default=None,
                            help='Drop privileges and switch to this group')
    grp_daemon.add_argument('-f', '--foreground', dest='foreground', default=False, action='store_true',
                            help='Stay in foreground, do not fork')
    grp_daemon.add_argument('-v', '--verbose', dest='verbose', default=False, action='store_true',
                            help='Output extra logging (not implemented right now)')
    grp_daemon.add_argument('-C', '--chdir', dest='chdir', default='.',
                            help='Change working directory to the provided value')

    grp_network = parser.add_argument_group('Network options')
    grp_network.add_argument('--input-ip', dest='input_ip', default='127.0.0.1', help='The network address to bind to')
    grp_network.add_argument('--input-port', dest='input_port', metavar='PORT', type=int, default=14001,
                             help='The port to bind to')
    grp_network.add_argument('--output-ip', dest='output_ip', default='127.0.0.1',
                             help='The OpenSMTPD instance IP to return processed email to')
    grp_network.add_argument('--output-port', dest='output_port', metavar='PORT', type=int, default=14000,
                             help='THe port where OpenSMTPD listens for processed email')

    _args = parser.parse_args()

    d = daemonize.Daemonize(
            'plusdashfilterserver',
            pid=_args.pidfile,
            action=run,
            user=_args.user,
            group=_args.group,
            verbose=_args.verbose,
            foreground=_args.foreground,
        )

    d.start()


if __name__ == '__main__':
    main()
