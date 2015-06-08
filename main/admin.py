from django.contrib import admin
from main.models import Category, Ticket, Comment, User, Team

class TicketAdmin(admin.ModelAdmin):
	list_display = ('Category', 'Team', 'name' ,'reporter', 'priority', 'created', 'slug')

class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'role', 'created')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'created', 'slug')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Ticket, TicketAdmin)