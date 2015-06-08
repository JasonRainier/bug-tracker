from django.shortcuts import render
from django.core.urlresolvers import reverse
from main.models import Category, Ticket, Comment, User, Team
from main.forms import TicketForm

def home(request):
	category_list = Category.objects.all()
	ticket_list = Ticket.objects.order_by('-created')[:10]
	team_list = Team.objects.all()

	context_dict = {'categories' : category_list,
	'tickets' : ticket_list,
	'teams' : team_list
	}

	return render(request, 'main/home.html', context_dict)
def categories(request):
	category_list = Category.objects.all()
	ticket_list = Ticket.objects.all()
	context_dict = {'categories' : category_list,
	'tickets' : ticket_list
	}

	return render(request, 'main/categories.html', context_dict)
def category(request, slug):
	context_dict = {}
	try:
		category = Category.objects.get(slug=slug)
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass
	context_dict['tickets'] = Ticket.objects.filter(Category = category)
	return render(request, 'main/category.html', context_dict)

def tickets(request):
	ticket_list = Ticket.objects.all()
	form = TicketForm
	context_dict = {'tickets' : ticket_list, 'form' : form}

	#process new ticket
	if request.method == 'POST':
		form = TicketForm(request.POST)
		if form.is_valid():
			form.save(commit = True)
		else:
			print form.error
	else:
		form = TicketForm()
	return render(request, 'main/tickets.html', context_dict)

def viewTicket(request, slug, ticketSlug):
	context_dict = {}
	try:
		category = Category.objects.get(slug=slug)
		
		ticket = Category.objects.get(slug=ticketSlug)
		context_dict['category'] = category
		context_dict['ticket'] = ticket
	except Category.DoesNotExist:
		pass
	return render(request, 'main/viewTicket.html', context_dict)

def teams(request):
	team_list = Team.objects.all()

	context_dict = {'teams' : team_list}

	return render(request, 'main/teams.html', context_dict)