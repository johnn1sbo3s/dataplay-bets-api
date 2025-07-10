from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Fixture, Bet, BetModel
from .serializers import FixtureSerializer, BetSerializer, BetModelSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import F, Case, When, Sum, DecimalField, IntegerField
from django.db.models.functions import TruncMonth
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class FixtureViewSet(viewsets.ModelViewSet):
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'source', 'league', 'home', 'away']

    @action(detail=True, methods=['get'])
    def bets(self, request, pk=None):
        fixture = self.get_object()
        serializer = BetSerializer(fixture.bets.all(), many=True)
        return Response(serializer.data)

class BetModelViewSet(viewsets.ModelViewSet):
    queryset = BetModel.objects.all()
    serializer_class = BetModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'feature_generator', 'active']

    @action(detail=True, methods=['get'])
    def bets(self, request, pk=None):
        bet_model = self.get_object()
        serializer = BetSerializer(bet_model.bets.all(), many=True)
        return Response(serializer.data)

class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fixture', 'fixture__date', 'bet_model']

class MonthlyResultsView(APIView):
    def get(self, request):
        queryset = Bet.objects.all()

        results = (
            queryset
            .annotate(month=TruncMonth('fixture__date'))
            .values('month')
            .annotate(
                profit=Sum(
                    Case(
                        When(bet_model__type='back', result='green', then=F('odds') - 1),
                        When(bet_model__type='back', result='red', then=-1),
                        When(bet_model__type='lay', result='green', then=((1.0 / (F('odds') - 1)) - 1)),
                        When(bet_model__type='lay', result='red', then=-1),
                        When(result='void', then=0),
                        default=0,
                        output_field=DecimalField(max_digits=10, decimal_places=2),
                    )
                ),
                total_bets=Sum(
                    Case(
                        When(result__in=['green', 'red'], then=1),
                        When(result='void', then=0),
                        default=0,
                        output_field=IntegerField(),
                    )
                )
                .order_by('month')
            )
        )

        return Response(list(results))