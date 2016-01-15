from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from .permissions import UserPermission
from django.contrib.auth import get_user_model, authenticate, login
from collections import OrderedDict


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated, UserPermission, )


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


class LoginViewSet(viewsets.GenericViewSet):

    serializer_class = LoginSerializer
    permission_classes = (AllowAny, )

    @list_route(methods=['POST'])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vdata = serializer.validated_data
        user = authenticate(username=vdata['email'], password=vdata['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                resp = OrderedDict(id=user.pk, token=user.auth_token.key)
                return Response(resp, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
