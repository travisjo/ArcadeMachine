from rest_framework import serializers

from base.models import HighScore, Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('name', 'year', 'latitude', 'longitude', 'date_created', 'date_created', 'date_modified')


class HighScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = HighScore
        fields = ('user', 'game', 'score', 'photo', 'date_created')
