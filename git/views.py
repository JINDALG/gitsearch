from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import list_route
from rest_framework.response import Response
from git.models import User
from git.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @list_route(methods=['get', ])
    def search(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        data = serializer.search(**request.query_params)
        if 'errors' in data:
            return Response(data)
        serializer = UserSerializer(data, many=True)
        for user in serializer.data:
            user.pop('id')
            login = user.pop('login')
            User.objects.update_or_create(login=login, defaults=dict(user))
        return Response(serializer.data)

