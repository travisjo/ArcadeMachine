from django.http import JsonResponse
from django.contrib.auth import User
from django.db.models import Q
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
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


class Tag(View):
    @csrf_exempt
    def post(self, request):
        print request
        print request.POST
        print request.FILES
        user = User.objects.get(pk=1)
        game = Game.objects.get(pk=2)
        instance = HighScore(user=user, game=game, score="12345", photo=request.FILES['picture'])
        instance.save()
        return JsonResponse({'success': 1}, status=200)
