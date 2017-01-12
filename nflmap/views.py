from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from models import Player, Team, College, HighSchool

def index(request):

    q1 = College.objects.all()
    q2 = q1.order_by('nfl_name')
    
    json = serialize('geojson', q2,geometry_field="geom",
          fields=('nfl_name',))
    context = {
        "teams":Team.objects.all(),
        "col_json":json,
    }
    return render(request, 'index.html', context)

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
        
def get_colleges_json(self,code="all"):

    if code == "all":
        q1 = College.objects.all()
        q2 = q1.order_by('nfl_name')

    else:
        upcode = code.upper()
        team = Team.objects.get(code=upcode)
        players = team.get_players()
        p_ids = [p.college.pk for p in players]
        q1 = College.objects.filter(pk__in=p_ids)
        q2 = q1.order_by('nfl_name')
    
    json = serialize('geojson', q2,geometry_field="geom",
          fields=('nfl_name',))
    
    #return JsonResponse(json, safe=False)
    return HttpResponse(json, content_type='application/json')