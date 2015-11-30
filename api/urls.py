from django.conf.urls import include, url
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'scores', views.HighScoreViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'tagged', views.TaggedGameViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^tag$', views.Tag.as_view()),
    # url(r'^/games/tagged/', views.TaggedGames.as_view()),
]
