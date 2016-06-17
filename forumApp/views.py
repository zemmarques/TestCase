# This Python file uses the following encoding: utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect


#from jinja2 import Environment

from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

from django.db import IntegrityError
import datetime

from forumApp.models import Topic, Reply
from forumApp.forms import TopicForm, ReplyForm
#import jinja2


def homepage (request):
	'''chama a página inicial do forum '''

	#print request

	return render_to_response('forumApp/homepage.html',{'topicos':Topic.objects.all()})


def registo(request):
	''' chama a página de registo da tabela de Users do Sistema Admin'''
	if request.method =='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/forum")
	else:
		formulario = UserCreationForm()

	args = {}
	args.update(csrf(request))

	args['formulario'] = formulario

	return render_to_response('forumApp/registo.html', args)


def login(request):
	''' chama a página de login'''
	c = {}
	c.update(csrf(request))

	#print c
	#print request

	return render_to_response('forumApp/login.html', c)
	

def autenticacao(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate( username = username, password = password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/forum/inicio')
	else:
		return HttpResponseRedirect('/forum/login')


def inicio(request):
	'''chama a página inicial com login feito'''

	if request.user.is_authenticated():
		return render_to_response('forumApp/homepage_login.html',{'topicos':Topic.objects.all(), 'username': request.user.username})
	else:
		#return render_to_response('Forum/homepage.html',{'topicos':Topico.objects.all()})
		return HttpResponseRedirect("/forum/login")
	

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/forum')


def topico(request, topico_id = 1):
	'''Mostra o link dos tópicos apenas se o utilizador estiver autenticado'''
	if request.user.is_authenticated():
		if request.POST:
			formulario = ReplyForm(request.POST)
			if formulario.is_valid():
				formulario.save()
				return HttpResponseRedirect("/forum/inicio")
		else:
			formulario = ReplyForm(initial={'idTopic':topico_id,'idUser': request.user.id })

		args = {}
		args.update(csrf(request))

		args['formulario'] = formulario

		return render(request,'forumApp/topico.html', {'topico':Topic.objects.get(id=topico_id),
			'resposta': Reply.objects.all(), 'formulario': args['formulario']})
	else:
		return HttpResponseRedirect("/forum/login")


def novoTopico(request):
	if request.user.is_authenticated():
		if request.POST:
			formulario = TopicForm(request.POST)
			if formulario.is_valid():
				formulario.save()
				return HttpResponseRedirect("/forum/inicio")
		else:
			formulario = TopicForm(initial={'idUser': request.user.id } )

		args = {}
		args.update(csrf(request))

		args['formulario'] = formulario

		return render_to_response("forumApp/novoTopico.html", args)
	else:
		#return render_to_response('Forum/homepage.html',{'topicos':Topico.objects.all()})
		return HttpResponseRedirect("/forum/login")






# def index(request):
# 	''' the first page made from this app'''
# 	return HttpResponse("Hello from the index page")

