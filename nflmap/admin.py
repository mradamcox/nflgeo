from django.contrib import admin
from models import Player, Team, College, HighSchool



class PlayerInline(admin.TabularInline):
    model = Player
    
class CollegeAdmin(admin.ModelAdmin):
    inlines = [
        PlayerInline,
    ]

class TeamAdmin(admin.ModelAdmin):
    inlines = [
        PlayerInline,
    ]
    
class HighSchoolAdmin(admin.ModelAdmin):
    inlines = [
        PlayerInline,
    ]
    
admin.site.register(Team,TeamAdmin)
admin.site.register(College,CollegeAdmin)
admin.site.register(HighSchool,HighSchoolAdmin)
admin.site.register(Player)