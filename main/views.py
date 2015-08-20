from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from main.models import Category, Ticket, TicketComment, Team
from main.forms import TicketForm, UserForm, UserProfileForm

def newUser(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data = request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	
	return render(request,'main/newUser.html', {'user_form' : user_form, 'profile_form' : profile_form, 'registered' : registered})

def userLogin(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/home')
			else:
				return HttpResponse("Your account is disabled")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'main/login.html', {})

@login_required
def userLogout(request):
	logout(request)
	return render(request, 'main/login.html')

@login_required
def home(request):
	category_list = Category.objects.all()
	ticket_list = Ticket.objects.order_by('-created')[:10]
	team_list = Team.objects.all()

	context_dict = {'categories' : category_list,
	'tickets' : ticket_list,
	'teams' : team_list
	}

	return render(request, 'main/home.html', context_dict)

@login_required
def categories(request):
	category_list = Category.objects.all()
	ticket_list = Ticket.objects.all()
	context_dict = {'categories' : category_list,
	'tickets' : ticket_list
	}

	return render(request, 'main/categories.html', context_dict)

@login_required
def category(request, slug):
	context_dict = {}
	try:
		category = Category.objects.get(slug=slug)
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass
	context_dict['tickets'] = Ticket.objects.filter(Category = category)
	return render(request, 'main/category.html', context_dict)

@login_required
def tickets(request):
	ticket_list = Ticket.objects.all()
	form = TicketForm
	context_dict = {'tickets' : ticket_list, 'form' : form}

	#process new ticket
	if request.method == 'POST':
		form = TicketForm(request.POST)
		if form.is_valid():
			temp = form.save(commit = False)
			temp.reporter = request.user
			temp.save()

		else:
			print form.error
	else:
		form = TicketForm()
	return render(request, 'main/tickets.html', context_dict)

@login_required
def viewTicket(request, slug, ticketSlug):
	context_dict = {}
	try:

		ticket = Ticket.objects.get(slug=ticketSlug)
		context_dict['ticket'] = ticket
	except Category.DoesNotExist:
		pass
	return render(request, 'main/viewTicket.html', context_dict)

@login_required
def teams(request):
	team_list = Team.objects.all()

	context_dict = {'teams' : team_list}

	return render(request, 'main/teams.html', context_dict)