from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    temp docstring
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="profile")
    username = models.CharField(max_length=80)
    id_user = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    profile_image = CloudinaryField('image', default='https://t3.ftcdn.net/jpg/03/46/83/96/360_\
    F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg')

    def __str__(self):
        return self.user.username

