
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from books.models import Book
from .serializer import BookSerializer , UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@api_view(["POST"])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message" : "User has been registered successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
            "success": False,
            "errors" : serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def index(request):
    posts = Book.objects.all()
    serializers = BookSerializer(instance=posts, many=True)
    return Response(data=serializers.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message" : "Book has been created succussfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
            "success": False,
            "errors" : serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def edit(request, id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(data={
            "success": True,
            "message" : "Book has not found"
        },status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message" : "Book has been updated succussfully"
        }, status=status.HTTP_202_ACCEPTED)

    return Response(data={
            "success": False,
            "errors" : serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete(request, id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(data={
            "success": True,
            "message" : "Book has not found"
        },status=status.HTTP_404_NOT_FOUND)

    book.delete()
    return Response(data={
            "success": True,
            "message" : "Book has been deleted succussfully"
        }, status=status.HTTP_204_NO_CONTENT)

