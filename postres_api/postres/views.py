from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostreSerializer

# Lista en memoria
postres_data = []

class PostreListCreate(APIView):
    def get(self, request):
        return Response(postres_data)

    def post(self, request):
        serializer = PostreSerializer(data=request.data)
        if serializer.is_valid():
            postres_data.append(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostreDetail(APIView):
    def get_object(self, pk):
        for postre in postres_data:
            if postre['id'] == pk:
                return postre
        return None

    def get(self, request, pk):
        postre = self.get_object(pk)
        if postre:
            return Response(postre)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        postre = self.get_object(pk)
        if not postre:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostreSerializer(data=request.data)
        if serializer.is_valid():
            postres_data.remove(postre)
            postres_data.append(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        postre = self.get_object(pk)
        if postre:
            postres_data.remove(postre)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
