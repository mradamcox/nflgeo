from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.core.serializers import serialize

class Team(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    conference = models.CharField(max_length=20)
    division = models.CharField(max_length=20)
    geom = models.PointField()
    
    def __str__(self):
        return self.name
        
    def get_players(self):
        q1 = Player.objects.filter(team=self)
        q2 = q1.order_by('last_name')
        return q2
        
    def get_colleges(self):
        players = self.get_players()
        p_ids = [p.college.pk for p in players]
        q1 = College.objects.filter(pk__in=p_ids)
        q2 = q1.order_by('nfl_name')
        
        
        return q2
        
    def get_college_json(self):
        colleges = self.get_colleges()
        json = serialize('geojson', colleges,
          geometry_field='geom',
          fields=('nfl_name',))
        return json
    
class College(models.Model):
    nfl_name = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    conference = models.CharField(max_length=6)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    geom = models.PointField(null=True)
    
    def __str__(self):
        return self.nfl_name
    
class HighSchool(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    geom = models.PointField(null=True)
    
    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nfl_id = models.IntegerField(primary_key=True)
    position = models.CharField(max_length=5)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    college = models.ForeignKey(College, null=True, on_delete=models.CASCADE)
    highschool = models.ForeignKey(HighSchool, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


    
