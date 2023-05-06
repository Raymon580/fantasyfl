from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string 

# Create your models here.

"""
def unique_code(self):
    N = 6
    while True:
        res = ''.join(random.choices(string.ascii_letters + string.digits, k=N))
        if League.objects.filter(code=res).count == 0:
            break
        return res
"""

class User(AbstractUser):
    pass

class Season(models.Model):
    year = models.IntegerField(unique=True)

class GameWeek(models.Model):
    season = models.ForeignKey(Season, on_delete=models.PROTECT, related_name="gameweeks")
    gameweek = models.IntegerField()
    
    def __str__(self):
        return f"GW {self.gameweek} of {self.season}"

class Position(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=3)
    
    def __str__(self):
        return self.code

class Club(models.Model):
    name = models.CharField(max_length=64)

class Player(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    club = models.ForeignKey(Club, on_delete=models.RESTRICT, related_name="players")
    position = models.ForeignKey(Position, on_delete=models.RESTRICT, related_name="pos_players")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.club}"

class Fixture(models.Model):
    home_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="home")
    away_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="away")
    gameweek = models.ForeignKey(GameWeek, on_delete=models.RESTRICT, related_name="fixtures")
    
    def __str__(self):
        return f"{self.home_club} vs {self.away_club} GW: {self.gameweek}"

class Goal(models.Model):
    scorer = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="goals")
    provider = models.ForeignKey(Player, on_delete=models.RESTRICT, related_name="assists")
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE, related_name="match_goals")
    
    def __str__(self):
        return f"Goal by {self.scorer}"

class Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    lineup = models.ManyToManyField(Player, related_name="starters")
    bench = models.ManyToManyField(Player, related_name="benched")
    
    def __str__(self):
        return f"{self.name}"

class League(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leagues_created")
    name = models.CharField(max_length=64)
    teams = models.ManyToManyField(Team)
    code =models.CharField(max_length=8, default="", unique=True)
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"