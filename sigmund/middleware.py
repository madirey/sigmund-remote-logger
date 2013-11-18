import re
from django import http
from django.conf import settings

class SigmundAllowOriginMiddleware(object):
    def process_request(self, request):
        if 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = http.HttpResponse()
            origin = request.META.get('HTTP_ORIGIN')
            origin_regex = getattr(settings, 'SIGMUND_ALLOW_ORIGIN', None)
            if origin_regex and re.match(origin_regex, origin):
                response['Access-Control-Allow-Headers'] = 'Accept,Origin,Content-Type'
                response['Access-Control-Allow-Methods'] = 'POST,GET,OPTIONS,PUT'
                response['Access-Control-Allow-Origin'] = origin
            else:
                response['Access-Control-Allow-Origin'] = 'null'
            return response
        return None

    def process_response(self, request, response):
        if response.has_header('Access-Control-Allow-Origin'):
            return response
        origin = request.META.get('HTTP_ORIGIN')
        response['Access-Control-Allow-Headers'] = 'Accept,Origin,Content-Type'
        response['Access-Control-Allow-Methods'] = 'POST,GET,OPTIONS,PUT'
        response['Access-Control-Allow-Origin'] = origin
        return response
