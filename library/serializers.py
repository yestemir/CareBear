from django.contrib.auth.models import User
from rest_framework import serializers

# from library.models import Book, SavedBook, RentedBook, Review, Genre


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = (
#             'id', 'title', 'description', 'author', 'genre', 'rating',
#             'image', 'created', 'release_date', 'isbn', 'quantity',
#             'language',
#         )
#
#
# class SavedBookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SavedBook
#         fields = ('id', 'book', 'user', 'created')
#
#
# class RentedBookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RentedBook
#         fields = ('id', 'book', 'user', 'created', 'state', 'term')
#
#
# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ('id', 'book', 'user', 'created', 'text', 'rating')
#
#
# class GenreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = ('id', 'title')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = User(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance
