from django.db import models

# Create your models here.
class TimestampModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Fixture(TimestampModel):
    class Meta:
        verbose_name = 'Fixture'
        verbose_name_plural = 'Fixtures'
        db_table = 'fixtures'
        ordering = ['date', 'time']
        unique_together = [['date', 'source', 'home', 'away']]
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['date', 'source']),
        ]

    class Source(models.TextChoices):
        EXCHANGE = 'exchange', 'Exchange'
        BOOKIE = 'bookie', 'Bookie'

    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=100, choices=Source.choices)
    league = models.CharField(max_length=100)
    home = models.CharField(max_length=100)
    away = models.CharField(max_length=100)
    home_ht_score = models.IntegerField(null=True)
    away_ht_score = models.IntegerField(null=True)
    home_ft_score = models.IntegerField(null=True)
    away_ft_score = models.IntegerField(null=True)
    home_odds = models.DecimalField(max_digits=5, decimal_places=2)
    draw_odds = models.DecimalField(max_digits=5, decimal_places=2)
    away_odds = models.DecimalField(max_digits=5, decimal_places=2)
    over_25_odds = models.DecimalField(max_digits=5, decimal_places=2)
    under_25_odds = models.DecimalField(max_digits=5, decimal_places=2)
    btts_yes_odds = models.DecimalField(max_digits=5, decimal_places=2)
    btts_no_odds = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Id: {self.id} - {self.home} x {self.away} ({self.date})'

class BetModel(TimestampModel):
    class Meta:
        verbose_name = 'BetModel'
        verbose_name_plural = 'BetModels'
        db_table = 'bet_models'

    class BetType(models.TextChoices):
        BACK = 'back', 'Back'
        LAY = 'lay', 'Lay'

    name = models.CharField(primary_key=True, max_length=100)
    feature_generator = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=BetType.choices)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Bet(TimestampModel):
    class Meta:
        verbose_name = 'Bet'
        verbose_name_plural = 'Bets'
        db_table = 'bets'
        indexes = [
            models.Index(fields=['bet_model']),
        ]

    class Result(models.TextChoices):
        GREEN = 'green', 'Green'
        RED = 'red', 'Red'
        VOID = 'void', 'Void'

    fixture = models.ForeignKey(Fixture, related_name='bets', on_delete=models.CASCADE)
    bet_model = models.ForeignKey(BetModel, related_name='bets', on_delete=models.CASCADE)
    odds = models.DecimalField(max_digits=5, decimal_places=2)
    result = models.CharField(max_length=10, choices=Result.choices)

    def __str__(self):
        return f'{self.fixture.home} x {self.fixture.away} ({self.bet_model.name})'