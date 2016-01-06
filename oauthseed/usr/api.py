from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer


class RegistrationViewSet(viewsets.GenericViewSet):

    serializer_class = RegisterSerializer

    @list_route(methods=['POST'], permission_classes=[AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        r = dict(token=user.auth_token.key)
        r.update(serializer.data)
        return Response(r, status=status.HTTP_201_CREATED)
