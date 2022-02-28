from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Upload
from .serializers import UploadSerializer
from rest_framework import status

@api_view(['GET'])
def getData(request):
    uploads = Upload.objects.all()
    serializer = UploadSerializer(uploads, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addFile(request):
    serializer = UploadSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)