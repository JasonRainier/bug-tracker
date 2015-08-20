from django import forms
from django.contrib.auth.models import User
from django.contrib.comments.forms import CommentForm
from main.models import Ticket, Category, TicketComment, UserProfile

class TicketForm(forms.ModelForm):
	Category = forms.ModelChoiceField(queryset=Category.objects.order_by('name'))
	reporter = forms.CharField()
	name = forms.CharField(max_length=256, help_text="Issue Title.")
	description = forms.CharField(max_length=1028, help_text="Please descibe your issue.")

	class Meta:
		model = Ticket
		fields = ('Category', 'name', 'description',)

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=256, help_text="Issue Title.")

	class Meta:
		model = Category
		fields = ('name',)

class CommentForm(forms.ModelForm):
	text = forms.CharField(max_length=1028)

	class Meta:
		model = TicketComment
		fields = ('text',)

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'first_name', 'last_name',)

class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('picture',)