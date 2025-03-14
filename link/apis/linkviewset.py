from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from link.models import Link
from link.serializers import LinkSerializer


@extend_schema_view(
    list=extend_schema(description="List all Link"),
    retrieve=extend_schema(description="Retrieve a specific Link"),
    create=extend_schema(description="Create a new Link"),
    update=extend_schema(description="Update an existing Link"),
    partial_update=extend_schema(description="Partially update a Link"),
    destroy=extend_schema(description="Delete a Link (soft delete)"),
)
class LinkViewSet(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def list(self, request, *args, **kwargs):
        self.queryset = Link.objects.filter(user=request.user)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.queryset = Link.objects.filter(user=request.user)
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.queryset = Link.objects.filter(user=request.user)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.queryset = Link.objects.filter(user=request.user)
        return super().destroy(request, *args, **kwargs)
