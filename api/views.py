from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination

from base.models import HighScore, Game, Machine

from .serializers import HighScoreSerializer, HighScoreUploadedSerializer, GameSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000


class HighScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows high scores to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = HighScore.objects.all().order_by('created')
    serializer_class = HighScoreSerializer
    pagination_class = LargeResultsSetPagination

    def create(self, request):
        serializer = HighScoreSerializer(data={
            'user': request.user.id,
            'game': request.data['game'],
            'score': request.data['score'],
            'photo': request.data['photo'],
        })
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(HighScoreUploadedSerializer(serializer.instance).data, status=200)
        return JsonResponse({}, status=400)


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that lists games
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Game.objects.all().order_by('-created')
    serializer_class = GameSerializer


class TaggedMachineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that shows tagged games
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Machine.objects.exclude(Q(latitude__isnull=True) | Q(longitude__isnull=True)).order_by('-created')
    serializer_class = GameSerializer


class TaggedMachines(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        games = Machine.objects.exclude(Q(latitude__isnull=True) | Q(longitude__isnull=True))
        return Response(games)


class Tag(View):
    @csrf_exempt
    def post(self, request):
        print(request)
        print(request.POST)
        print(request.FILES)
        user = User.objects.get(pk=1)
        game = Game.objects.get(pk=2)
        instance = HighScore(user=user, game=game, score="12345", photo=request.FILES['picture'])
        instance.save()
        return JsonResponse({'success': 1}, status=200)
