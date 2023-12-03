from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as drf_views
from api import views


router = routers.DefaultRouter()
router.register(r'scores', views.HighScoreViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'tagged', views.TaggedMachineViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tag', views.Tag.as_view()),
    # url(r'^/games/tagged/', views.TaggedGames.as_view()),
    path('token-auth/', drf_views.obtain_auth_token)
]
