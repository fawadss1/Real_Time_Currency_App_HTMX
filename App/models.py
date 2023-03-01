from django.db import models


class Currency(models.Model):
    curreny = models.CharField(max_length=50)
    curreny_rate = models.IntegerField()
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.curreny
