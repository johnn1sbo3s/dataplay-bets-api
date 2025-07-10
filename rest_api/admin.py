from django.contrib import admin
from .models import Fixture, Bet, BetModel

# Register your models here.
@admin.register(Fixture)
class FixtureAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'date',
        'time',
        'source',
        'league',
        'home',
        'away',
        'home_ht_score',
        'away_ht_score',
        'home_ft_score',
        'away_ft_score',
        'home_odds',
        'draw_odds',
        'away_odds',
        'over_25_odds',
        'under_25_odds',
        'btts_yes_odds',
        'btts_no_odds',
        'created_at',
        'updated_at',
    )

@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fixture',
        'bet_model',
        'odds',
        'result',
        'created_at',
        'updated_at',
    )

@admin.register(BetModel)
class BetModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'feature_generator',
        'active',
        'created_at',
        'updated_at',
    )
