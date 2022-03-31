from django.db import models

class AthletesAndResults(models.Model):
    CHOICES_TP_SEX = [("M", "Male"), ("F", "Female")]
    CHOICES_TP_MEDAL = [("Gold", "Gold"), ("Silver", "Silver"), ("Bronze", "Bronze"), ("NA", "NA")]
    CHOICES_TP_SEASON = [("Summer", "Summer"), ("Winter", "Winter")]
 
    pk_athlete = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    sex = models.CharField(max_length=1, blank=False, null=False, choices=CHOICES_TP_SEX)
    age = models.CharField(max_length=255, blank=False, null=False)
    height = models.CharField(max_length=255, blank=False, null=False)
    weight = models.CharField(max_length=255, blank=False, null=False)
    team = models.CharField(max_length=255, blank=False, null=False)
    noc = models.CharField(max_length=255, blank=False, null=False)
    games = models.CharField(max_length=255, blank=False, null=False)
    year = models.CharField(max_length=255, blank=False, null=False)
    season = models.CharField(max_length=6, blank=False, null=False, choices=CHOICES_TP_SEASON)
    city = models.CharField(max_length=255, blank=False, null=False)
    sport = models.CharField(max_length=255, blank=False, null=False)
    event = models.CharField(max_length=255, blank=False, null=False)
    medal = models.CharField(max_length=6, blank=False, null=False, choices=CHOICES_TP_MEDAL)

