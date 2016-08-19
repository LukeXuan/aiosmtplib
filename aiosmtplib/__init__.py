import asyncio

from .smtp import SMTP
from .smtp_ssl import SMTP_SSL
from .errors import (
    SMTPException, SMTPServerDisconnected, SMTPConnectError,
    SMTPRecipientsRefused, SMTPResponseException, SMTPNotSupported,
    SMTPHeloError, SMTPDataError, SMTPAuthenticationError,
    SMTPSenderRefused, SMTPRecipientRefused,
)


__all__ = (
    'SMTP', 'SMTP_SSL',
    'SMTPException', 'SMTPServerDisconnected', 'SMTPConnectError',
    'SMTPResponseException', 'SMTPNotSupported', 'SMTPHeloError',
    'SMTPDataError', 'SMTPAuthenticationError', 'SMTPSenderRefused',
    'SMTPRecipientRefused', 'SMTPRecipientsRefused',
)


def main():
    import sys

    def prompt(prompt):
        sys.stdout.write(prompt + ": ")
        sys.stdout.flush()
        return sys.stdin.readline().strip()

    sender = prompt("From")
    recipients = prompt("To").split(',')
    print("Enter message, end with ^D:")
    message = []
    while True:
        line = sys.stdin.readline()
        if line:
            message.append(line)
        else:
            break

    message = '\n'.join(message)
    print("Message length is %d" % len(message))

    loop = asyncio.get_event_loop()
    smtp = SMTP(hostname='localhost', port=25, loop=loop)
    send_message = asyncio.async(smtp.sendmail(sender, recipients, message))
    loop.run_until_complete(send_message)


# Test the sendmail method, which tests most of the others.
# Note: This always sends to localhost.
if __name__ == '__main__':
    main()
