from datetime import datetime
from django.conf import settings
from logging import Handler
import json, requests, urlparse

class SigmundHandler(Handler):

    def __init__(self):
        super(SigmundHandler, self).__init__()

    def emit(self, record):
        if not hasattr(settings, 'SIGMUND_URL') or not hasattr(
                       settings, 'SIGMUND_USERNAME') or not hasattr(
                       settings, 'SIGMUND_API_KEY'):
            return

        url = urlparse.urljoin(settings.SIGMUND_URL, '/api/v1/sigmund/')

        headers = {
            'Authorization': 'ApiKey {username}:{api_key}'.format(
                username=settings.SIGMUND_USERNAME,
                api_key=settings.SIGMUND_API_KEY),
            'Content-Type': 'application/json',
        }

        try:
            timestamp = datetime.utcfromtimestamp(record.created).isoformat()
        except:
            timestamp = ''

        params = {
            'message': self.format(record),
            'level': record.levelname,
            'filename': record.filename,
            'line': record.lineno,
            'timestamp': timestamp,
        }

        requests.post(url, json.dumps(params), headers=headers)
