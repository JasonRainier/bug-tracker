import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticket_tracker.settings')

import django
django.setup()

from main.models import Category, Ticket, Comment, User, Team


def populate():
	cat1 = add_category(name = "test Cat 1")

	cat2 = add_category(name = "test Cat 2")

	add_ticket(category = cat1,
		reporter = "user 1",
		priority = "high",
		title = "Primary",
		desc = "this is a test category")

	add_ticket(category = cat2,
		reporter = "user 55",
		priority = "low",
		title = "another one",
		desc = "this is a test category")

	add_ticket(category = cat2,
		reporter = "user 13",
		priority = "low",
		title = "address this",
		desc = "fu")

	add_team(name = "best team",
		role = "make this work")

	add_team(name = "other team",
		role = "do everything else")


def add_category(name):
	c = Category.objects.get_or_create(name=name)[0]
	return c

def add_ticket(category, reporter, priority, title, desc):
	tick = Ticket.objects.get_or_create(Category=category, reporter=reporter,
		title=title, description=desc)[0]
	return tick
def add_team(name, role):
	t = Team.objects.get_or_create(name=name, role=role)[0]
	return t

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()