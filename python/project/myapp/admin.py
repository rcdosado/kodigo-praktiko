from django.contrib import admin
from .models import Project, Team, Person


class PersonAdmin(admin.ModelAdmin):
	list_display = ('name', )
	search_fields = ('name',)

admin.site.register(Person, PersonAdmin)

class TeamAdmin(admin.ModelAdmin):
	list_display = ('leader','type')

admin.site.register(Team, TeamAdmin)

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = ('title',)


admin.site.register(Project, ProjectAdmin)