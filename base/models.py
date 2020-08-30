from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel


class Game(TimeStampedModel):
    giantbomb_id = models.IntegerField(null=True)
    name = models.CharField(max_length=200)
    aliases = models.TextField(blank=True, null=True)
    release_date = models.DateField('Year released', null=True)

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.name, self.release_date)


class Machine(TimeStampedModel):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    latitude = models.DecimalField(max_digits=20, decimal_places=18, null=True, blank=True, default=None)
    longitude = models.DecimalField(max_digits=21, decimal_places=18, null=True, blank=True, default=None)

    def __str__(self):
        return "{} ({}, {})".format(self.game.name, self.latitude, self.longitude)


class HighScore(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    score = models.CharField(max_length=200)
    photo = models.ImageField()

    def __str__(self):
        return "{} - {} - {}".format(self.user.username, self.machine.game.name, self.score)
