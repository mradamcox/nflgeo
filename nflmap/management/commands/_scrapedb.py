from django.conf import settings
from nflmap.models import Player, Team, College, HighSchool
import psycopg2
import requests
from bs4 import BeautifulSoup
import string
import csv
import shapefile
import os

def delete_all_players():
    Player.objects.all().delete()
    
def delete_all_colleges():
    College.objects.all().delete()

def get_or_make_college(name):

    print name

    try:
        col_obj = College.objects.get(nfl_name=name)
        
    except:
    
        col_obj = College(nfl_name=name)
        
        shp = os.path.join(settings.SHP_DIR,'CollegesUniversities.shp')

        sf = shapefile.Reader(shp)
        recs = sf.shapeRecords()

        wkt = None
        for rec in recs:
            match_name = rec.record[39]
            if name.encode('utf-8').lower() == match_name:
                print "got geom"
                x,y = rec.shape.points[0][0],rec.shape.points[0][1]
                wkt = 'POINT({} {})'.format(x,y)
                break
        col_obj.geom = wkt

    col_obj.save()

    return col_obj
    
def get_schools(playerid):

    url = 'http://www.nfl.com/player/a/{}/profile'.format(playerid)
    req = requests.request('GET',url)
    soup = BeautifulSoup(req.content, "html.parser")
    ss = soup.findAll('strong')
    college,hs = '',''
    for i in ss:
        if i.text == "College":
            college = i.nextSibling.replace(":","").lstrip().rstrip()
        if i.text == "High School":
            hs = i.nextSibling.replace(":","").lstrip().rstrip()

    ret_college = get_or_make_college(college)
    
    if not hs == '':
        try:
            hs_obj = HighSchool.objects.get(name=hs)
        except:
            # uffda. gonna be a trick to make high schools with geometry...
            hs_obj = HighSchool(name=hs)
            hs_obj.save()
            print "new high school:",hs
    else:
        hs_obj = None
        
    return (ret_college,hs_obj)
        
def process_row(row):

    data = row.findAll('td')

    # get name
    name = data[2].text
    l_name = name.split(',')[0]
    f_name = name.split(',')[1].lstrip().rstrip()

    # get team and position
    team = data[12].text
    position = data[0].text

    # get player nflid to find teams    
    p_url = data[2].a['href']
    nflid = p_url.split('/')[3]
    
    try:
        Player.objects.get(nfl_id=nflid)
        return
    
    except:
        college, hs = get_schools(nflid)
        player = Player(first_name=f_name)
        player.last_name = l_name
        player.team = Team.objects.get(code=team)
        player.position = position
        player.nfl_id = nflid
        player.college = college
        player.highschool = hs

        player.save()
        print "new player:",l_name+', '+f_name
    
def process_page(pagesoup):

    table = pagesoup.tbody
    rows = table.findAll('tr')
    for row in rows:
        process_row(row)

def run_the_site():

    for letter in string.ascii_uppercase:
        print letter
        for n in range(1,10):
            params = {'d-447263-p':n,'filter':letter,'category':'lastName','playerType':'current'}
            req = requests.get('http://www.nfl.com/players/search?',params)
            soup = BeautifulSoup(req.content, "html.parser")
            results = soup.find('div',{'id':'searchResults'})
            if "No players found." in results.text:
                break
            process_page(soup)
