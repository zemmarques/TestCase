import unittest
from django.test import TestCase
from django.test.client import Client
from django.http import HttpRequest
from forumApp.views import homepage, login, registo,



class HomePageTest(unittest.TestCase):

	def setUp(self):

		self.c = Client()
		#self.c.login(username='test', password='test')



	# HomePage tests #
	def test_homepage_get_status_response(self):
		''' See if the response of the homepage in the url:"/" is ok (satus_code 200)'''

		response = self.c.get('/')
		self.assertEqual(response.status_code, 200)

	def test_homepage_title_text_is_correct(self):
		'''Confirm the Correct presentation of the Homepage'''
	 	
	 	request = HttpRequest()
	 	response = homepage (request)

	 	self.assertIn(b'<h1><center> Space Forum Homepage </center></h1>', response.content)


	# LoginPage tests
	def test_loginPage_get_status_response(self):
		''' See if the response of the LoginPage in the url:"/forum/login/" is ok (satus_code 200)'''

		response = self.c.get('/forum/login/')
		self.assertEqual(response.status_code, 200)

	def test_loginPage_title_text_is_correct(self):
		'''Confirm the Correct presentation of the Homepage'''
	 	
	 	request = HttpRequest()
	 	response = login (request)

	 	self.assertIn(b'<h2>Login</h2>', response.content)

	# def test_login_page_load(self):
	# 	''' Ensure that the LoginPage loads correctly'''

	# 	response = self.c.post('/forum/login/', data = dict(username='test', password='test'), follow_redirects = True)
	# 	self.assertIn(b'<h2> <center> Topicos Recentes </center> </h2>', response.content)


	# RegistoPage tests
	def test_registo_get_status_response(self):
		''' See if the response of the RegisterPage in the url:"/forum/registo/" is ok (status_code 200)'''

		response = self.c.get('/forum/registo/')
		self.assertEqual(response.status_code, 200)

	def test_RegistoPage_title_text_is_correct(self):
		'''Confirm the Correct presentation of the Homepage'''
	 	
	 	request = HttpRequest()
	 	response = registo (request)

	 	self.assertIn(b'<h2>Registo de Novo Utilizador</h2>', response.content)

	# LogoutPage tests
	def test_logout_get_status_response(self):
		'''See if the response of the LogoutPage in the url:"/forum/" is ok (status_code 200)'''
		'''The page is redirect to the homepage   <-- see it better '''

		response = self.c.get('/forum/')
		self.assertEqual(response.status_code, 200)
