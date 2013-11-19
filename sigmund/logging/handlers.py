from django.conf import settings
from logging import Handler
import requests, urlparse

class SigmundHandler(Handler):

    def __init__(self):
        super(SigmundHandler, self).__init__()

    def emit(self, record):
        if not hasattr(settings, 'SIGMUND_URL') or not hasattr(
                       settings, 'SIGMUND_USERNAME') or not hasattr(
                       settings, 'SIGMUND_API_KEY'):
            return

        url = urlparse.urljoin(settings.SIGMUND_URL,
                               '/api/v1/sigmund/?username=%s&api_key=%s' % (
                                    settings.SIGMUND_USERNAME,
                                    settings.SIGMUND_API_KEY)
                               )

        params = {
            'message': record.message,
            'level': record.levelname,
            'filename': record.filename,
            'line': record.lineno,
            'user_agent': '',
            'ip_address': '',
            'timestamp': record.asctime,
        }

        requests.post(url, params)

if __name__ == '__main__':
    print SigmundHandler()
