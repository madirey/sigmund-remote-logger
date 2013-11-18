from models import LogEntry
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

class SigmundResource(ModelResource):
    class Meta:
        queryset = LogEntry.objects.all()
        authentication = Authentication()
        authorization = Authorization()
        serializer = Serializer(formats=['json', 'jsonp'])

    def hydrate(self, bundle):
        bundle.data['ip_address'] = bundle.request.META.get('REMOTE_ADDR')
        bundle.data['user_agent'] = bundle.request.META.get('HTTP_USER_AGENT')
        return bundle
