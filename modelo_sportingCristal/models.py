from django.db import models

# Create your models here.

class stadium(models.Model):
    name = models.CharField()
    city = models.CharField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()

class referee(models.Model):
    name = models.CharField()

class team(models.Model):
    name =  models.CharField()
    shortName = models.CharField()
    image = models.CharField()

class championship(models.Model):
    context = models.CharField()
    name = models.CharField

class actions(models.Model):
    type = models.CharField()
    icon = models.ImageField()
    url = models.CharField()

class state(models.Model):
    name = models.CharField()
    type = models.CharField()

class meta(models.Model):
    own_side = models.CharField()
    is_own_match = models.IntegerField()


class match(models.Model):
    context = models.CharField()
    championship = models.ForeignKey(championship)
    local = models.ForeignKey(team)
    away = models.ForeignKey(team)
    local_goals = models.IntegerField()
    local_penalty_goals = models.IntegerField()
    away_goals = models.IntegerField()
    away_penalty_goals = models.IntegerField()
    scorer = models.CharField()
    stadium = models.ForeignKey(stadium)
    referee = models.ForeignKey(referee)
    ticketing = models.CharField()
    dateTime = models.CharField()
    timeStamp= models.CharField()
    actions = [models.ForeignKey(actions)]
    meta = models.ForeignKey(meta)
    period = models.CharField()
    state = models.ForeignKey(state)
    selected = models.BooleanField()
    on_live = models.BooleanField()
    is_confirmed = models.BooleanField()
