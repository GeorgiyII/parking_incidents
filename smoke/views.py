from rest_framework.views import APIView
from rest_framework.response import Response


class Smoke(APIView):
    def get(self, request):
        data = {
            "data": "hello world"
        }
        return Response(data)
