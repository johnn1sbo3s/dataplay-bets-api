from rest_framework import serializers
from rest_api.models import Fixture, Bet, BetModel

class FixtureSerializer(serializers.ModelSerializer):
    bets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Fixture
        fields = '__all__'

class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = '__all__'

class BetModelSerializer(serializers.ModelSerializer):
    bets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = BetModel
        fields = '__all__'