from rest_framework import viewsets
from rest_framework.response import Response

from tinyapp.serializers.tiny import TinySerializer
from tinyapp.models import ShortenedURLStore


class TinyViewSet(viewsets.ModelViewSet):
    queryset = ShortenedURLStore.objects.all()
    http_method_names = [
        "post",
        "get",
    ]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TinySerializer
        elif self.request.method == "GET":
            return TinySerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                "title": "TinyUrl",
                "message": "Created successfully",
                "data": response.data,
            }
        )

    def list(self, request, *args, **kwargs):
        url = self.request.query_params.get("url")

        if not url:
            response = super().list(request, *args, **kwargs)
            return Response(
                {
                    "title": "Tiny",
                    "message": "Listed successfully",
                    "data": response.data,
                }
            )

        else:
            url = ShortenedURLStore.objects.filter(custom_url=url)
            if not url.exists():
                return Response(
                    {
                        "title": "Tiny",
                        "message": "TinyUrl Not found",
                    }
                )
            else:
                url = url.first()
                return Response(
                    {
                        "title": "Tiny",
                        "message": "Retrieved successfully",
                        "data": f"Original URL is: {url.original_url}",
                    }
                )
