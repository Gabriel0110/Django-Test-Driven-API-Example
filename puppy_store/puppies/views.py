from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Puppy
from .serializers import PuppySerializer

# Create your views here.

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_puppy(request, pk):
    try:
        puppy = Puppy.objects.get(pk=pk)
    except Puppy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    if request.method == 'GET': # get details of a single puppy
        return Response({})
    elif request.method == 'DELETE': # delete a single puppy
        return Response({})
    elif request.method == 'PUT': # update details of a single puppy
        return Response({})

@api_view(['GET', 'POST'])
def get_post_puppies(request):
    if request.method == 'GET': # get all puppies
        return Response({})
    elif request.method == 'POST': # insert a new record for a puppy
        return Response({})