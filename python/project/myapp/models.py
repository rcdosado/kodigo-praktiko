from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return self.name

class Team(models.Model):
	TYPE_CHOICES = (
		('1', 'Development'),
		('2', 'Implementation'),
		('3', 'Unknown'),
	)
	# project_name=models.ForeignKey('ProjectTeam', blank=True)
	leader = models.ForeignKey(Person)
	type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=3)


	def __str__(self):
		# return self.project_acronym()
		return self.leader.name

class Project(models.Model):
	STATUS_CHOICES = (
		('1','Unknown'),
		('2','Ongoing'),
		('3','Completed'),
		('4','Extended')
	)
	title = models.TextField(max_length=255, unique=True)
	team = models.ManyToManyField(Team, help_text="Create/Select a team for this project", related_name="ProjectTeam",
		blank=True)
	
	# lets you print the project that this team handled
	def get_team_projects(self, team):
		ps = Project.objects.filter(self.team=team)
		return ",".join([pr.title for pr in ps])
