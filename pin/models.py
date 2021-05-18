import uuid
from django.db import models
from django.contrib.auth.models import User



class Board(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    description = models.TextField(max_length = 300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pin = models.ManyToManyField('Pin' , related_name="pin")

    def __str__(self):
        return f'{self.title}'


class Pin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE , related_name='board')
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='media', default='default.jpg')
    caption = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'

class QuickSave(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ManyToManyField(User)
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pin}'