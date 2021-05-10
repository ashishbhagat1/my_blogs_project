from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    GENDER = (
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
        ("OTHER", "OTHER"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    gender = models.CharField(max_length=6, choices=GENDER, default="None")


def __str__(self):  # what i want to show on front page so that can i easy find out like name or title
    return f"{self.user.username}"
