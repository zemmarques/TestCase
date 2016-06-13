from django import forms
from forumApp.models import Topic, Reply


class TopicForm(forms.ModelForm):

	class Meta:
		model = Topic
		fields = "__all__"
		widgets = {'pubdate': forms.HiddenInput(),'idUser':forms.HiddenInput()}


class ReplyForm(forms.ModelForm):

	class Meta:
		model = Reply
		fields = "__all__"
		widgets = {'idTopic': forms.HiddenInput(),'idUser':forms.HiddenInput()}