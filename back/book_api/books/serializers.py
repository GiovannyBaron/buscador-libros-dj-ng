from rest_framework import serializers

from .models import Authors, Books, Categories, Publishers

# HACK ModelSerializer from models, Serializer from raw data


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['id', 'autor']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'categoria']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishers
        fields = ['id', 'editorial']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['autor'] = instance.autor.autor
        representation['categoria'] = instance.categoria.categoria
        representation['editorial'] = instance.editorial.editorial
        return representation
