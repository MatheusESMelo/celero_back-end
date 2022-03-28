from django.db import models

class AthletesAndResults(models.Model):
    CHOICES_TP_SEX = [(1, "M"), (2, "F")]
    CHOICES_TP_MEDAL = [(1, "Gold"), (2, "Silver"), (3, "Bronze"), (4, "NA")]
 
    pk_athlete = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    sex = models.IntegerField(blank=False, null=False, choices=CHOICES_TP_SEX)
    age = models.IntegerField(max_length=3, blank=False, null=False)
    height = models.CharField(max_length=255, blank=False, null=False)
    weight = models.CharField(max_length=255, blank=False, null=False)
    team = models.CharField(max_length=255, blank=False, null=False)
    noc = models.CharField(max_length=255, blank=False, null=False)
    games = models.CharField(max_length=255, blank=False, null=False)
    year = models.DateField(blank=False, null=False)
    season = models.CharField(max_length=255, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    sport = models.CharField(max_length=255, blank=False, null=False)
    event = models.CharField(max_length=255, blank=False, null=False)
    medal = models.IntegerField(blank=False, null=False, choices=CHOICES_TP_MEDAL)
