from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from profiles_api import serializers, models, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters


class HelloAPIView(APIView):
    serializer_class = serializers.HelloSerializer
    """ Test API View"""
    def get(self, request, format=None):
        an_api_view = [
            'Uses HTTP methods as functions(get, post, patch, put, delete)',
            'Is similar to a tradiional Django View',
            'Gives you the most control over the application logic',
            'Is Mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_api_view': an_api_view})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # Retrieve the name field
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Handle updating an object """
        return Response({'method': 'PUT'})

    def patch(self, request,pk=None):
        """ Handle partially updating an object """
        return Response({'method': 'PATCH'})
    def delete(self, request,pk=None):
        """ Handle deleting an object """
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer
    """ Test API ViewSet """

    def list(self, request):
        """ Return a Hello Message """
        a_view_set = [
            'Uses actions(list, create, retrieve,update, partial_update',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello', 'a_view_set': a_view_set})
    
    def create(self, request):
        """ create a new hello message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )    
    def retrieve(self, request, pk=None):
        """ Handle Getting an object by Id """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ Handle Updating an entire Object """
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """ Handle partial updating an object """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ Handle removing an object """
        return Response({'http_method': 'DELETE'})


class UserProfileViewset(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.updateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')