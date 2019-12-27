from modelo_sportingCristal.models import *
import requests
import json

def run():
    r = requests.get('http://futbol.funx.io/api/v2/sporting-cristal/home/match/')
    texto = r.text
    listaDePartidos = json.loads(texto)
    numeroDePartidos = listaDePartidos.__len__()
    contador = 0
    while contador < numeroDePartidos:
        championship = Championship.create(listaDePartidos[contador].get('championship').get('slug'),
                                           listaDePartidos[contador].get('championship').get('name'))
        stadium = Stadium.create(listaDePartidos[contador].get('stadium').get('slug'),
                                 listaDePartidos[contador].get('stadium').get('name'),
                                 listaDePartidos[contador].get('stadium').get('city'),
                                 listaDePartidos[contador].get('stadium').get('latitude'),
                                 listaDePartidos[contador].get('stadium').get('longitude'))
        referee = Referee.create(listaDePartidos[contador].get('referee').get('name'))
        local = Team.create(listaDePartidos[contador].get('local').get('slug'),
                            listaDePartidos[contador].get('local').get('name'),
                            listaDePartidos[contador].get('local').get('short_name'),
                            listaDePartidos[contador].get('local').get('image'))
        away = Team.create(listaDePartidos[contador].get('away').get('slug'),
                            listaDePartidos[contador].get('away').get('name'),
                            listaDePartidos[contador].get('away').get('short_name'),
                            listaDePartidos[contador].get('away').get('image'))
        actionsCalendar = ActionsCalendar.create(listaDePartidos[contador].get('actions')[0].get('icon'),
                                                 listaDePartidos[contador].get('actions')[0].get('url'))
        actionsUrl = ActionsUrl.create(listaDePartidos[contador].get('actions')[1].get('icon'),
                                       listaDePartidos[contador].get('actions')[1].get('icon'))
        state = State.create(listaDePartidos[contador].get('state').get('name'),
                             listaDePartidos[contador].get('state').get('type'))
        meta = Meta.create(listaDePartidos[contador].get('meta').get('own_side'),
                           listaDePartidos[contador].get('meta').get('is_own_match'))
        championship.save()
        stadium.save()
        referee.save()
        local.save()
        away.save()
        actionsCalendar.save()
        actionsUrl.save()
        state.save()
        meta.save()
        match = Match.create(slug=listaDePartidos[contador].get('slug'),
                             championship=championship,
                             local=local,
                             away=away,
                             local_goals=listaDePartidos[contador].get('local_goals'),
                             local_penalty_goals=listaDePartidos[contador].get('local_penalty_goals'),
                             away_goals=listaDePartidos[contador].get('away_goals'),
                             away_penalty_goals=listaDePartidos[contador].get('away_penalty_goals'),
                             scorer=listaDePartidos[contador].get('scorer'),
                             stadium=stadium,
                             referee=referee,
                             ticketing=listaDePartidos[contador].get('ticketing'),
                             datetime=listaDePartidos[contador].get('datetime'),
                             timestamp=listaDePartidos[contador].get('timestamp'),
                             actionsCalendar=actionsCalendar,
                             actionsUrl=actionsUrl,
                             meta=meta,
                             period=listaDePartidos[contador].get('period'),
                             state=state,
                             selected=listaDePartidos[contador].get('selected'),
                             on_live=listaDePartidos[contador].get('on_live'),
                             is_confirmed=listaDePartidos[contador].get('is_confirmed'))
        match.save()
        contador += 1

