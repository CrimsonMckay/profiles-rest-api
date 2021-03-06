from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API VIEW"""
    serializer_class =serializers.HelloSerializer
    
    def get(self,request,format=None):
        """Returns API features """
        an_apiview=['Uses HTTP methods as functions(get,post,patch,put,delete)',
                    'Is similar to traditional api view'
                    'Gives you most control over your application logic',
                    'is mapped manually to URLS',
                    ]
        
        return Response({'message':'Hello','an_apiview':an_apiview})
    
    def post(self,request):
        """create a welcome note with our name"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )
            
    def put(self,request,pk=None):
        """Handling updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        """Handling a partial update of an object"""
        return Response({'method': 'PATCH'})
    
    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})        
    
 
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a message"""
        
        a_viewset = [
            'Uses action (list,create,retrieve,update,partial_update',
            'Automatically maps to URLS using Routers'
            'Provides more functionality with less code',
         ]
        
        return Response({'message':"Response form api",'a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})    