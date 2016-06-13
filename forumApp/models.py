from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User


class Topic(models.Model):
	title = models.CharField(max_length = 254)
	bodyText = models.TextField()
	pubDate = models.DateTimeField(auto_now_add = True)
	idUser = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

	def replyTopic(self):
		replyes =  Reply.objects.all()
		counter=0
		for r in replyes:
			if r.idTopic_id==self.id:
				counter=counter + 1
		return counter


class Reply(models.Model):
	text = models.TextField()
	pubDate = models.DateTimeField(auto_now_add = True)
	idTopic = models.ForeignKey(Topic)
	idUser = models.ForeignKey(User)

	def __unicode__(self):
		return self.text
