from django.db import models


class Profile(models.Model):

    name = models.CharField( max_length=50)
    profile_picture = models.ImageField(upload_to=None,)
    bio = models.TextField()


    class Meta:
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("Profile_detail", kwargs={"pk": self.pk})
