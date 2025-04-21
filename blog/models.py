from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):  
    """Расширение модели User для добавления дополнительных полей"""  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    bio = models.TextField(blank=True)  
  
    def __str__(self):  
        return f'Профиль пользователя {self.user.username}'
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True)  
    
    class Meta:  
        ordering = ['-published'] 

    def __str__(self):
        return self.title
    