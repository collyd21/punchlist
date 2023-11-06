from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Punch(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField('PunchImage', related_name='punchImages')

    def __str__(self):
        return self.title
class PunchImage(models.Model):
    image = models.ImageField(upload_to='punch_images/')
    punch = models.ForeignKey(Punch, on_delete=models.CASCADE, related_name='punchimages') 


class Meta:
        order_with_respect_to = 'title'



