from rest_framework import serializers

from base.models import HighScore, Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('name', 'year', 'latitude', 'longitude', 'date_created', 'date_created', 'date_modified')


class HighScoreSerializer(serializers.ModelSerializer):
    game_name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    class Meta:
        model = HighScore
        fields = ('username', 'user', 'game_name', 'game', 'score', 'photo', 'date_created')

    def create(self, validated_data):
        score = HighScore(
            user=validated_data['user'],
            game=validated_data['game'],
            score=validated_data['score'],
            photo=validated_data['photo'],
        )
        score.save()
        return score

    def get_game_name(self, obj):
        return obj.game.name

    def get_username(self, obj):
        return obj.user.username
