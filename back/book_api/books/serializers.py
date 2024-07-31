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
    # It can be both options
    autor = serializers.CharField(source='autor.autor')
    categoria = serializers.StringRelatedField()
    editorial = serializers.StringRelatedField()

    class Meta:
        model = Books
        fields = '__all__'
