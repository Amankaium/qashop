from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)


class Good(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name="good",
    )
