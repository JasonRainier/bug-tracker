from django import forms
from main.models import Ticket, Category, Comment

class TicketForm(forms.ModelForm):
	reporter = forms.CharField(max_length=128, help_text="Please enter your name.")
	name = forms.CharField(max_length=256, help_text="Issue Title.")
	description = forms.CharField(max_length=1028, help_text="Please descibe your issue.")

	class Meta:
		model = Ticket
		fields = ('reporter', 'name', 'description',)

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=256, help_text="Issue Title.")

	class Meta:
		model = Category
		fields = ('name',)

class CommentForm(forms.ModelForm):
	text = forms.CharField(max_length=1028)

	class Meta:
		model = Comment
		fields = ('text',)
		#add user to fields