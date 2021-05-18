from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photo', null=True, blank=True)
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user}'

class UsersRelation(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return f'{self.from_user} following {self.to_user}'
