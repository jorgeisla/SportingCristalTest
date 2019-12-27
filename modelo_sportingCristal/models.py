from django.db import models

# Modelo de datos inicial

'''Clase Stadium
donde se incluye su nombre, ciudad, latitud y longitud
'''


class Stadium(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField()
    city = models.CharField()
    latitude = models.CharField()
    longitude = models.CharField()

    @classmethod
    def create(cls, slug, name, city, latitude, longitude):
        stadium = cls(slug=slug, name=name, city=city, latitude=latitude, longitude=longitude)
        return stadium

    def __str__(self):
        return self.slug + self.name + self.city + self.latitude + self.longitude

'''Clase Referee
se utiliza para almacenar los nombres de los arbitros
'''


class Referee(models.Model):
    name = models.CharField()

    @classmethod
    def create(cls, name):
        referee = cls(name=name)
        return referee

    def __str__(self):
        return self.name

'''Clase Team
se utiliza para almacenar los distintos equipos con su nombre, shortName y una imagen. 
'''


class Team(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField()
    shortName = models.CharField()
    image = models.CharField()

    @classmethod
    def create(cls, slug, name, shortName, image):
        team = cls(slug=slug, name=name, shortName=shortName, image=image)
        return team

    def __str__(self):
        return self.slug + self.name + self.shortName + self.image


'''Clase Championship
se utilizara para almacenar los distintos torneos con su nombre y un contexto
'''


class Championship(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField()

    @classmethod
    def create(cls, slug, name):
        championship = cls(slug=slug, name=name)
        return championship

    def __str__(self):
        return self.slug + self.name


'''Clase ActionsCalendar
almacena las aciciones de calendario
'''


class ActionsCalendar(models.Model):
    icon = models.ImageField()
    url = models.CharField()

    @classmethod
    def create(cls, icon, url):
        actionsCalendar = cls(icon=icon, url=url)
        return actionsCalendar


'''Clase ActionsUrl
almacena las aciciones de Url
'''


class ActionsUrl(models.Model):
    icon = models.ImageField()
    url = models.CharField()

    @classmethod
    def create(cls, icon, url):
        actionsUrl = cls(icon=icon, url=url)
        return actionsUrl


'''Clase State
se utilizará para almacenar los distintos estados de un partido con un nombre y un tipo
'''


class State(models.Model):
    name = models.CharField()
    type = models.CharField()

    @classmethod
    def create(cls, name, type):
        state = cls(name=name, type=type)
        return state

    def __str__(self):
        return self.name + self.type

'''Clase Meta'''


class Meta(models.Model):
    own_side = models.CharField()
    is_own_match = models.CharField()

    @classmethod
    def create(cls, own_side, is_own_match):
        meta = cls(own_side=own_side, is_own_match=is_own_match)
        return meta

    def __str__(self):
        return self.own_side + self.is_own_match


'''Clase Match
se utilizara para almacenar todo lo relacionado a un partido
'''


class Match(models.Model):
    slug = models.SlugField(unique=True)
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE)
    local = models.ForeignKey(Team, on_delete=models.CASCADE)
    away = models.ForeignKey(Team, on_delete=models.CASCADE)
    local_goals = models.CharField()
    local_penalty_goals = models.CharField()
    away_goals = models.CharField()
    away_penalty_goals = models.CharField()
    scorer = models.CharField()
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)
    ticketing = models.CharField()
    dateTime = models.CharField()
    timeStamp = models.CharField()
    actionsCalendar = models.ForeignKey(ActionsCalendar, on_delete=models.CASCADE)
    actionsUrl = models.ForeignKey(ActionsUrl, on_delete=models.CASCADE)
    meta = models.ForeignKey(Meta, on_delete=models.CASCADE)
    period = models.CharField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    selected = models.BooleanField()
    on_live = models.BooleanField()
    is_confirmed = models.BooleanField()

    @classmethod
    def create(cls, slug, championship, local, away, local_goals, local_penalty_goals, away_goals,
               away_penalty_goals,
               scorer, stadium, referee, ticketing, datetime, timestamp, actions, meta, period, state, selected,
               on_live, is_confirmed):
        match = cls(slug=slug, championship=championship, local=local, away=away, local_goals=local_goals,
                    local_penalty_goals=local_penalty_goals, away_goals=away_goals,
                    away_penalty_goals=away_penalty_goals, scorer=scorer, stadium=stadium, referee=referee,
                    ticketing=ticketing, datetime=datetime, timestamp=timestamp, actions=actions, meta=meta,
                    period=period, state=state, selected=selected, on_live=on_live, is_confirmed=is_confirmed)
        return match
