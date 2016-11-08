from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from assets.models import get_place_options


class AssetsViewSet(GenericViewSet):
    @list_route(methods=['GET'])
    def place_options(self, request):
        return Response(get_place_options())
