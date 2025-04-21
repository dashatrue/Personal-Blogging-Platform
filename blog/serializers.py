from rest_framework import serializers  
from .models import Category, Post, Profile
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):  
    """Сериализатор для модели User"""  
  
    class Meta:  
        model = User  
        fields = ('id', 'username')

class ProfileSerializer(serializers.ModelSerializer):  
    """Сериализатор для профиля пользователя"""  
    user = UserSerializer(read_only=True)  
  
    class Meta:  
        model = Profile  
        fields = ('id', 'user', 'bio')  
class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для поста"""  
    author = UserSerializer(read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'category', 'published', 'updated')

class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категории""" 
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'posts')