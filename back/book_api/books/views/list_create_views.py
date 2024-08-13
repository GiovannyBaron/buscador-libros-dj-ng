from typing import Type

from django.db import models
from django.http import Http404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Authors, Books, Categories, Publishers
from ..serializers import (AuthorSerializer, BookSerializer,
                           CategorySerializer, PublisherSerializer)


class BaseSaver:
    def __init__(self, serializer: Type[serializers.ModelSerializer],
                 model: Type[models.Model], filter_keys):
        self.serializer = serializer
        self.model = model
        self.filter_keys = filter_keys

    def save_in_model(self, data: dict):
        serialized_data = self.serializer(data=data)
        if not serialized_data.is_valid():
            raise Http404('Datos no válidos')

        validated_data = serialized_data.validated_data
        args_to_filter = {key: value for key,
                          value in validated_data.items() if key in self.filter_keys}
        if self.model.objects.filter(**args_to_filter).exists():
            raise Http404('El registro ya existe')

        data = self.model(**validated_data)
        data.save()

        return data


class GenericCRUD(APIView):
    def get(self, request):
        objects = self.model.objects.all()
        objects_serialized = self.serializer(objects, many=True)
        return Response(objects_serialized.data)


class Author(GenericCRUD):
    def __init__(self):
        self.serializer = AuthorSerializer
        self.model = Authors
        self.filter_keys = ['autor']
        self.base_saver = BaseSaver(
            self.serializer, self.model, self.filter_keys)

    def get(self, request):
        authors = self.model.objects.all()
        authors_serialized = self.serializer(authors, many=True)
        return Response(authors_serialized.data)

    def post(self, request, **kwargs):
        if (data := self.base_saver.save_in_model(request.data)):

            return Response({"message": f"Autor/a {data.autor} fue agregado/a"})

        return Response({"message": "Hubo un error al agregar al autor"})


class Category(GenericCRUD):
    def __init__(self):
        self.serializer = CategorySerializer
        self.model = Categories
        self.filter_keys = ['categoria']
        self.base_saver = BaseSaver(
            self.serializer, self.model, self.filter_keys)

    def post(self, request):
        if (data := self.base_saver.save_in_model(request.data)):

            return Response({"message": f"Categoría {data.categoria} fue agregada"})

        return Response({"message": "Hubo un error al agregar la categoría"})


class Publisher(GenericCRUD):
    def __init__(self):
        self.serializer = PublisherSerializer
        self.model = Publishers
        self.filter_keys = ['editorial']
        self.base_saver = BaseSaver(
            self.serializer, self.model, self.filter_keys)

    def post(self, request):
        if (data := self.base_saver.save_in_model(request.data)):

            return Response({"message": f"Editorial {data.editorial} fue agregada"})

        return Response({"message": "Hubo un error al agregar la editorial"})


class Book(APIView):
    def __init__(self):
        self.serializer = BookSerializer
        self.model = Books
        self.filter_keys = ['titulo']
        self.base_saver = BaseSaver(
            self.serializer, self.model, self.filter_keys)

    def post(self, request):
        if (data := self.base_saver.save_in_model(request.data)):

            return Response({"message": f"Libro {data.titulo} fue agregado"})

        return Response({"message": "Hubo un error al agregar el libro"})
