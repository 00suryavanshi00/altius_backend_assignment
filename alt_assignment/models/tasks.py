
from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):


    title = models.CharField( max_length=50)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    # will add db indexes later for faster querying 
    class Meta:
        pass


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reversed("Task_detail", kwargs={"pk": self.pk})
