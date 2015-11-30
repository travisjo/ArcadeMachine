from django.db.models import Q
from rest_framework import viewsets
from rest_framework.views import APIView

from base.models import HighScore, Game

from .serializers import HighScoreSerializer, GameSerializer


class HighScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows high scores to be viewed or edited.
    """
    queryset = HighScore.objects.all().order_by('-date_created')
    serializer_class = HighScoreSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows high scores to be viewed or edited.
    """
    queryset = Game.objects.all().order_by('-date_created')
    serializer_class = GameSerializer


class TaggedGameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows high scores to be viewed or edited.
    """
    queryset = Game.objects.exclude(Q(latitude__isnull=True) | Q(longitude__isnull=True)).order_by('-date_created')
    serializer_class = GameSerializer


class TaggedGames(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        games = Game.objects.exclude(Q(latitude__isnull=True) | Q(longitude__isnull=True))
        return Response(games)
