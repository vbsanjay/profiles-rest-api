from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as functions post, patch, put, delete",
            "is similar to traditional django, but specifically inded to use for api",
        ]

        return Response({'messgae': 'Hello!', 'an_apiview': an_apiview})


