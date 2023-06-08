from django.db import models

class Groceries(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name