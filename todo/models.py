from django.db import models


class Todo(models.Model):
    added_date = models.DateField()
    text = models.TextField()

    def __str__(self):
        return self.text
