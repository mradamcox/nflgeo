from nflmap.models import Team
from django.conf import settings
import os
import shapefile

team_dict = {
    'Arizona Cardinals':'ARI',
    'Atlanta Falcons':'ATL',
    'Baltimore Ravens':'BAL',
    'Buffalo Bills':'BUF',
    'Carolina Panthers':'CAR',
    'Chicago Bears':'CHI',
    'Cincinnati Bengals':'CIN',
    'Cleveland Browns':'CLE',
    'Dallas Cowboys':'DAL',
    'Denver Broncos':'DEN',
    'Detroit Lions':'DET',
    'Green Bay Packers':'GB',
    'Houston Texans':'HOU',
    'Indianapolis Colts':'IND',
    'Jacksonville Jaguars':'JAX',
    'Kansas City Chiefs':'KC',
    'Los Angeles Rams':'LA',
    'Miami Dolphins':'MIA',
    'Minnesota Vikings':'MIN',
    'New England Patriots':'NE',
    'New Orleans Saints':'NO',
    'New York Giants':'NYG',
    'New York Jets':'NYJ',
    'Oakland Raiders':'OAK',
    'Philadelphia Eagles':'PHI',
    'Pittsburgh Steelers':'PIT',
    'San Diego Chargers':'SD',
    'San Francisco 49ers':'SF',
    'Seattle Seahawks':'SEA',
    'Tampa Bay Buccaneers':'TB',
    'Tennessee Titans':'TEN',
    'Washington Redskins':'WAS'
}

con = {
    'American':'AFC',
    'National':'NFC',
}

def delete_all_teams():
    Team.objects.all().delete()

def make_teams():

    team_shp = os.path.join(settings.BASE_DIR,'nflmap','shp','Stadiums_NFL.shp')
    sf = shapefile.Reader(team_shp)
    shapeRecs = sf.shapeRecords()
    for s in shapeRecs:
        team = s.record[30]
        conference = con[s.record[26]]
        div = s.record[27].upper()
        point = s.shape.points[0]
        coords = "POINT({} {})".format(point[0],point[1])
        newteam = Team(code=team_dict[team],name=team,division=div,conference=conference,geom=coords)
        newteam.save()