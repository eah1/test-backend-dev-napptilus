from .models import OompaLoompa
from .serializers import OompaLoompaSerializer,\
                         OompaLoompaCreateSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.


class OompaLoompaList(generics.ListCreateAPIView):

    queryset = OompaLoompa.objects.all()
    serializer_class = OompaLoompaCreateSerializer
    pagination_class = LimitOffsetPagination

    def get(self, request):

        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = OompaLoompaSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = OompaLoompaSerializer(queryset, many=True)
        return Response(serializer.data)


class OompaLoompaDetall(generics.RetrieveUpdateDestroyAPIView):

    queryset = OompaLoompa.objects.all()
    serializer_class = OompaLoompaCreateSerializer
