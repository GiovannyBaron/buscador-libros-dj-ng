
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError


from ..models import Authors, Books, Categories, Publishers
from ..serializers import (AuthorSerializer, BookSerializer,
                           CategorySerializer, PublisherSerializer)

# HACK request.data for json, request.POST for FORM

class GenericCRUD(APIView):
    def __generic_put_patch(self, request: Request, id: str,  partial: bool):
        object = get_object_or_404(self.model, id=id)
        serialized_data = self.serializer(
            object, data=request.data, partial=partial)
        if not serialized_data.is_valid():
            raise ValidationError(
                {"error": "Invalid data", "details": serialized_data.errors})

        serialized_data.save()
        return serialized_data.data

    def get(self, request: Request, id: str):
        object = get_object_or_404(self.model, id=id)
        return Response(self.serializer(object).data)

    def patch(self, request: Request, id: str):
        data = self.__generic_put_patch(request, id, partial=True)
        return Response(data)

    def put(self, request: Request, id: str):
        data = self.__generic_put_patch(request, id, partial=False)
        return Response(data)

    def delete(self, request: Request, id: str):
        object = get_object_or_404(self.model, id=id)
        object_rep = object.__str__()
        object.delete()
        return Response({'message': f'{object_rep} fue eliminado'})


class AuthorDetail(GenericCRUD):
    def __init__(self):
        self.model = Authors
        self.serializer = AuthorSerializer


class CategoryDetail(GenericCRUD):
    def __init__(self):
        self.model = Categories
        self.serializer = CategorySerializer


class PublisherDetail(GenericCRUD):
    def __init__(self):
        self.model = Publishers
        self.serializer = PublisherSerializer


class BookDetail(GenericCRUD):
    def __init__(self):
        self.model = Books
        self.serializer = BookSerializer
