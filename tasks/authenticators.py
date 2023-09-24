from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class UnauthenticatedAccessAuthentication(BaseAuthentication):
    def authenticate(self, request):
        if request.resolver_match.url_name in ['api-register', 'api-login']:
            return None  
        return super().authenticate(request)
