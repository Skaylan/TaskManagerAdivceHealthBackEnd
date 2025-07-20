from django.db import models
from django.utils import timezone
from api.models.user import User

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    color = models.CharField(max_length=10, default='#8B5CF6')
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)