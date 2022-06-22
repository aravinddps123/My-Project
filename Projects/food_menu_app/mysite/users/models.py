from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete = models.CASCADE)
    #THIS models.CaseCade will delete the child field if the parent field is deleted
    #there is no point in having the profile when the user is deleted
    image = models.ImageField(default='profilepic.jpg', upload_to="profile_pictures")
    location = models.CharField(max_length=100)


    def __str__(self):

        return self.user.username
