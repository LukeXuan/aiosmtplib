'''SMTP SSL client class for use with asyncio.

Author: Cole Maclean <hi@cole.io>
        Luke Chen <me@xlk.me>
A subclass derived from SMTP client class that force ssl option to be `True`.
'''
from .smtp import SMTP

try:
    import ssl
except ImportError:
    WITH_SSL = False
else:
    WITH_SSL = True

SMTP_SSL_PORT = 465

if WITH_SSL:
    class SMTP_SSL(SMTP):
        """This is a subclass derived from SMTP client class that always
        connects SMTP server over a SSL encrypted socket.
        """
        def __init__(self, *args, **kwargs):
            # TODO: A more graceful way to enforce ssl option.
            SMTP.__init__(self, *args, **{**kwargs, 'ssl': True})
else:
    SMTP_SSL = None
