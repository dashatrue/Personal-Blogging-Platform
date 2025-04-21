from rest_framework import viewsets, permissions, filters  
from django_filters.rest_framework import DjangoFilterBackend  
from rest_framework.decorators import action  
from rest_framework.response import Response  
from .models import Profile, Category, Post, Comment  
from .serializers import ProfileSerializer, CategorySerializer, PostSerializer, CommentSerializer  
from .permissions import IsOwnerOrReadOnly 

posts = [
	{
    	'author': 'Администратор',
    	'title': 'Это первый пост',
    	'content': 'Содержание первого поста.',
    	'date_posted': '7 марта, 2025'
	},
	{
    	'author': 'Пользователь',
    	'title': 'Это второй пост',
    	'content': 'Подробное содержание второго поста.',
    	'date_posted': '16 марта, 2025'
	},
    {
        'author': 'Пользователь#2',
    	'title': 'Это третий пост',
    	'content': 'Содержание третьего поста.',
    	'date_posted': '19 апреля, 2025'
	}
]

"""def home(request):
    context = {
    	'posts': posts
	}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'О разработчике'})"""

class ProfileViewSet(viewsets.ModelViewSet):  
    """Представление для профилей пользователей"""  
    queryset = Profile.objects.all()  
    serializer_class = ProfileSerializer  
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  
  
    def perform_create(self, serializer):  
        serializer.save(user=self.request.user)