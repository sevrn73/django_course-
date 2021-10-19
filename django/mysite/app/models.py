from django.db import models

class StableRate(models.Model):
    x = models.CharField(max_length=30)
    y = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.x  + ' секунду'