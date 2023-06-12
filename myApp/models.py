from django.db import models

class League(models.Model):
    abbr = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.abbr

class Team(models.Model):
    abbr = models.CharField(max_length=3)
    name = models.CharField(max_length=150)
    league = models.ForeignKey(League, to_field="abbr", db_column="league_abbr", on_delete=models.CASCADE)

    def __str__(self):
        return self.abbr

