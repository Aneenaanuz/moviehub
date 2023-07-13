from rest_framework import serializers
from django.contrib.auth.models import User
from myapp.models import Movies,Genres,Reviews


class Userserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=['id','username','email','password']

    def create(self, validated_data):                            # create method overriding because the purpose of password hiding
        return User.objects.create_user(**validated_data)
    
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genres
        fields=['id','genre']

class ReviewSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    #movie=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        exclude=("movie",)
    
class MoviesSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    #genre_names=GenreSerializer(read_only=True,many=True)
    genres=serializers.SlugRelatedField(many=True,read_only=True,slug_field='genre')
    reviews=ReviewSerializer(many=True,read_only=True)
    class Meta:
        model=Movies
        fields="__all__"

class GenreReadSerializer(serializers.ModelSerializer):
    genre=serializers.CharField(read_only=True)
    class Meta:
        model=Genres
        fields=["genre"]