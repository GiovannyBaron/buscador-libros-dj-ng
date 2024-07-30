from rest_framework import serializers

from .models import Authors, Books, Categories, Publishers

# HACK ModelSerializer from models, Serializer from raw data


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['autor']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['categoria']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishers
        fields = ['editorial']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
