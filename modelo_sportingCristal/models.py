from django.db import models


# Modelo de datos inicial

'''Clase stadium
donde se incluye su nombre, ciudad, latitud y longitud'''
class stadium(models.Model):
    name = models.CharField()
    city = models.CharField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()

'''Clase referee
se utiliza para almacenar los nombres de los arbitros'''
class referee(models.Model):
    name = models.CharField()

'''Clase team
se utiliza para almacenar los distintos equipos con su nombre, shortName y una imagen. 
'''
class team(models.Model):
    name =  models.CharField()
    shortName = models.CharField()
    image = models.CharField()

'''Clase championship
se utilizara para almacenar los distintos torneos con su nombre y un contexto'''
class championship(models.Model):
    context = models.CharField()
    name = models.CharField

'''Clase actions
no se realmente como se utilizará
'''
class actions(models.Model):
    type = models.CharField()
    icon = models.ImageField()
    url = models.CharField()

'''Clase state
se utilizará para almacenar los distintos estados de un partido con un nombre y un tipo'''
class state(models.Model):
    name = models.CharField()
    type = models.CharField()

'''Clase meta'''
class meta(models.Model):
    own_side = models.CharField()
    is_own_match = models.IntegerField()

'''Clase match
se utilizara para almacenar todo lo relacionado a un partido
'''
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
