from rest_framework import mixins, viewsets
from rest_framework.response import Response

from assets.models import get_place_options


class PlaceOptionsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    def list(self, request, *args, **kwargs):
        return Response(get_place_options())
