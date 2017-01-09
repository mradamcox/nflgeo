from django.shortcuts import render
from models import Player, Team, College, HighSchool

def team_list(request):
    teams = Team.objects.all()
    context = {
        "teams":teams,
    }
    return render(request, 'team_list.html', context)
    
def team_page(request,code):
    upcode = code.upper()
    team = Team.objects.get(code=upcode)
    context = {
        "team":team,
        "teams": Team.objects.all(),
        "players":team.get_players(),
        "colleges":team.get_colleges(),
        "col_json":team.get_college_json(),
    }
    return render(request, 'team_page.html', context)
