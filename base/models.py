from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    giantbomb_id = models.IntegerField(null=True)
    name = models.CharField(max_length=200)
    aliases = models.TextField(blank=True, null=True)
    release_date = models.DateField('Year released', null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=18, null=True, blank=True, default=None)
    longitude = models.DecimalField(max_digits=21, decimal_places=18, null=True, blank=True, default=None)
    date_created = models.DateTimeField('Date created', auto_now_add=True)
    date_modified = models.DateTimeField('Date modified', auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.year)


class HighScore(models.Model):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    score = models.CharField(max_length=200)
    photo = models.ImageField()
    date_created = models.DateTimeField('Date created', auto_now_add=True)
