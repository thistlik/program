from django.db import models

class Entry(models.Model):
    text = models.CharField(max_length=52)

    def __str__(self):
        return self.text
