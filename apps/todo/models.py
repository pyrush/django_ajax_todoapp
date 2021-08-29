from django.db import models
from django.urls import reverse


class TODOModel(models.Model):
    title = models.CharField(max_length=101)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("todo:task_list_url")
