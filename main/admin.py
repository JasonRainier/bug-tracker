from django.contrib import admin
from main.models import Category, Ticket, Comment, User, Team, UserProfile

class TicketAdmin(admin.ModelAdmin):
	list_display = ('Category', 'Team', 'name' ,'reporter', 'priority', 'created', 'slug')

class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'role', 'created')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'created', 'slug')

#class UserAdmin(admin.ModelAdmin):
#	list_display = ('first_name', 'last_name', 'username', 'email', 'last_login', 'date_joined')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(UserProfile)