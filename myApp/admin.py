from django.contrib import admin

from myApp.models import League, Team

# username: admin
# password: password

class TeamInline(admin.StackedInline):
    model = Team

class LeagueAdmin(admin.ModelAdmin):
    list_display = ('abbr', 'name')
    inlines = [TeamInline]
admin.site.register(League, LeagueAdmin)



class TeamAdmin(admin.ModelAdmin):
    list_display = ('abbr', 'name', 'league')


admin.site.register(Team, TeamAdmin)

