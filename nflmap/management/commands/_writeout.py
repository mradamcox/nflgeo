from django.conf import settings
from nflmap.models import Player,Team,College,HighSchool
import csv
import os

outdir = os.path.join(settings.BASE_DIR,'nflmap','writeouts')

def write_players():
    
    players = Player.objects.all()
    outfile = os.path.join(outdir,'players.csv')
    
    with open(outfile,'wb') as f:
        w = csv.writer(f)
        w.writerow(['id','f_name','l_name','position','team','college','highschool'])
        for p in players:
            if not p.college:
                cpk = ''
            else:
                cpk = p.college.pk
            if not p.highschool:
                hspk = ''
            else:
                hspk = p.highschool.pk
            w.writerow([p.nfl_id,p.first_name,p.last_name,p.position,p.team.pk,cpk,hspk])
            
def write_teams():
    
    teams = Team.objects.all()
    outfile = os.path.join(outdir,'teams.csv')
    
    with open(outfile,'wb') as f:
        w = csv.writer(f)
        w.writerow(['id','name','code','conference','division','geom'])
        for t in teams:
            w.writerow([t.pk,t.name,t.code,t.conference,t.division,t.geom])
            
def write_colleges():
    
    colleges = College.objects.all()
    outfile = os.path.join(outdir,'colleges.csv')
    
    with open(outfile,'wb') as f:
        w = csv.writer(f)
        w.writerow(['id','name','conference','city','state','geom'])
        for c in colleges:
            w.writerow([c.pk,c.name,c.conference,c.city,c.state,c.geom])

def write_highschools():
    
    highschools = HighSchool.objects.all()
    outfile = os.path.join(outdir,'highschools.csv')
    
    with open(outfile,'wb') as f:
        w = csv.writer(f)
        w.writerow(['id','name','city','state','geom'])
        for hs in highschools:
            w.writerow([hs.pk,hs.name,hs.city,hs.state,hs.geom])