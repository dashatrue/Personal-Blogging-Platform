from rest_framework import viewsets, permissions, filters  
from django_filters.rest_framework import DjangoFilterBackend  
from rest_framework.decorators import action  
from rest_framework.response import Response  
from .models import Profile, Category, Post 
from .serializers import ProfileSerializer, CategorySerializer, PostSerializer
from .permissions import IsOwnerOrReadOnly 

class ProfileViewSet(viewsets.ModelViewSet):  
    """Представление для профилей пользователей"""  
    queryset = Profile.objects.all()  
    serializer_class = ProfileSerializer  
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  
  
    def perform_create(self, serializer):  
        serializer.save(user=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    """Представление для категорий"""  
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class PostViewSet(viewsets.ModelViewSet):  
    """Представление для постов"""  
    queryset = Post.objects.all()  
    serializer_class = PostSerializer  
    permission_classes = [IsOwnerOrReadOnly]  
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  
    filterset_fields = ['category__name', 'author__username']  
    search_fields = ['title', 'content']  
    ordering_fields = ['published', 'author__username']  
  
    def perform_create(self, serializer):  
        serializer.save(author=self.request.user)