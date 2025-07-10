from django.urls import path
from .views import FixtureViewSet, BetModelViewSet, BetViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('fixtures', FixtureViewSet)
router.register('bets', BetViewSet, basename='bet')
router.register('bet-models', BetModelViewSet, basename='betmodel')

urlpatterns = []
