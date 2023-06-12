from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import Team
from collections import defaultdict


def index(request):
    return HttpResponse("Hello, world. You're at the index")

# return all Teams grouped by League
def get_teams_by_league(request):
    league_teams = defaultdict(list)

    teams = Team.objects.all().order_by('abbr')
    for team in teams:
        league_teams[team.league.abbr].append(f"{team.abbr} - {team.name}")

    res = []

    for league_name in sorted(league_teams.keys()):
        res.append([league_name, league_teams[league_name]])

    return render(request, "teams.html", {'leagueTeams': res})
