from modelo_sportingCristal.models import *
import requests

def run():
    r = requests.get('http://futbol.funx.io/api/v2/sporting-cristal/home/match/')
    texto = r.text
    replace = ['{', '}', '[', ']', ',', ':']
    for simbol in replace:
        texto = texto.replace(simbol, '"')
    a = texto.split('"')
    while a.__contains__(''):
        a.remove('')
    while a.__contains__(':'):
        a.remove(':')
    print(a)

    indiceChampionship = a.index('championship')
    indiceStadium = a.index('stadium')
    indiceReferee = a.index('referee')
    indiceLocal = a.index('local')
    indiceAway = a.index('away')
    indiceLocalGoals = a.index('local_goals')
    indiceAwayGoals = a.index('away_goals')
    indiceLocalPenaltyGoals = a.index('local_penalty_goals')
    indiceAwayPenaltyGoals = a.index('away_penalty_goals')
    indiceScorer = a.index('scorer')
    indiceTicketing = a.index('ticketing')
    indiceActions = a.index('actions')
    indiceState = a.index('state')
    indiceMeta = a.index('meta')
    indiceDateTime = a.index('datetime')
    indiceTimeStamp = a.index('timestamp')
    indicePeriod = a.index('period')
    indiceSelected = a.index('selected')
    indiceOnLive = a.index('on_live')
    indiceIsConfirmed = a.index('is_confirmed')

    championship = Championship.create(a[indiceChampionship + 2], a[indiceChampionship + 4])
    referee = Referee.create(a[indiceReferee + 2])
    local = Team.create(a[indiceLocal +2], a[indiceLocal + 4], a[indiceLocal + 6], a[indiceLocal+8]+':'+a[indiceLocal+9])
    away = Team.create(a[indiceAway + 2], a[indiceAway + 4], a[indiceAway + 6], a[indiceAway+8]+':'+a[indiceAway+9])
    stadium = Stadium.create(a[indiceStadium + 2], a[indiceStadium + 4], a[indiceStadium + 6], a[indiceStadium + 8], a[indiceStadium + 10])
    meta = Meta.create(a[indiceMeta + 2], a[indiceMeta + 4])

    print(championship.__str__())
    print(referee.__str__())
    print(local.__str__())
    print(away.__str__())
    print(stadium.__str__())
    print(meta.__str__())

