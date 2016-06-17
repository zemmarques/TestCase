import datetime
from django.test import TestCase

from forumApp.models import Topic


class TopicTestCase(TestCase):
	""" this test case was NOT written before de implementation code. So, for now,
	I am NOT using the TDD method ... """


	def setUp(self):
		Topic.objects.create(title="Test topic for testing", bodyText="yes, I am the bodyText of the topic", 
			pubDate=datetime.datetime(year=2015, month=11, day=28),idUser_id=1)

	def test_model_basic(self):
		""" test that the model entity added in set up method is present """

		testTitle = "Test topic for testing"
		try:
			topic = Topic.objects.get(title=testTitle)
		except Topic.DoesNotExist:
			self.fail("the object created in the setUp is not present in the database!!")
		assert topic.title == testTitle

	def test_model_bodyText(self):
		""" test if the bodytext was well saved"""

		b = "yes, I am the bodyText of the topic"
		try:
			bText = Topic.objects.get(bodyText=b)
		except Topic.DoesNotExist:
			print ("opss o topico nao existe!!")
		
		try:
			assert bText.bodyText == b
		except UnboundLocalError:
			print ("Assert failed!") 

	# def ...proximo teste 
