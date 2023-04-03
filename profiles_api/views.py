from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

'''
class HelloApiView(APIView):
    """Test API View"""
    serializer_class=serializers.HelloSerializer
    def get(self, request, format=None):
        api_view=['hello from list']
        return Response({'message':'Hello','an_apiview':api_view})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f"Hello {name}"
            return Response({'message':message})  

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
    
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        """Handles a partial update of an object"""
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        """Handles deletion of object"""
        return Response({'message':'DELETE'})
    

class HelloViewSet(viewsets.ViewSet):
    """Test ApiViewSet"""

    serializer_class=serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        api_response=['Uses action lsit crete retrieve partial update update, Automaticlay maps to URls using Routers']

        return Response({'message':'Hello','api_response':api_response})

    def create(self, request):
        """Create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f"Hello {name}"
            return Response({'message':message})
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def retrieve(self, request, pk=None):
        """Retreives detaield data"""

        return Response({'http_method':'GET'})


    def update(self, reuqest,pk=None):
        """Handle updating object""" 

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object""" 

        return Response({'http_method':'PATCH'})


    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method':'GET'})

'''

from profiles_api import models


class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class=serializers.UserProfileSeriazer
    queryset=models.UserProfile.objects.all()
    