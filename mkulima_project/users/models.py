from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=150, null=True) #important so that someone can start empty

    def __str__(self):
        return f'{self.user.username} Profile'

    #https://stackoverflow.com/questions/52351756/django-typeerror-save-got-an-unexpected-keyword-argument-force-insert
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(os.path.join(settings.MEDIA_ROOT, self.image.path))

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
