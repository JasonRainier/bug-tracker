from django.db import models
from django.template.defaultfilters import slugify

#User structure
class Team(models.Model):
	name = models.CharField(max_length=128, unique=True)
	role = models.CharField(max_length=128)
	created = models.DateTimeField(unique=True)

	class Meta:
		verbose_name_plural = "teams"

	def __unicode__(self):
		return self.name

class User(models.Model):
	#
	# Learn Django Auth first
	#
	Team = models.ForeignKey(Team)
	name = models.CharField(max_length=128, unique=True)
	created = models.DateTimeField()

	class Meta:
		verbose_name_plural = "users"

	def __unicode__(self):
		return self.name
#
# Add URLs to models for links
#

#ticketing structure
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	created = models.DateTimeField()
	slug = models.SlugField()

	class Meta:
		verbose_name_plural = "categories"

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

class Comment(models.Model):
	#User = models.ForeignKey()
	text = models.CharField(max_length=1028)
	created = models.DateTimeField()

	class Meta:
		verbose_name_plural = "comments"

	def __unicode__(self):
		return self.text[:30]

class Ticket(models.Model):
	LOW = 'low'
	HIGH = 'high'
	PRIORITY_CHOICES = (
		(LOW, 'low'),
		(HIGH, 'high')
	)
	Category = models.ForeignKey(Category, blank=True, null=True, default="None")
	Team = models.ForeignKey(Team, null=True, blank=True)
	#Reporter = models.ForeignKey(User)
	reporter = models.CharField(max_length=128)
	#Comment = models.ForeignKey(Comment, blank=True)
	priority = models.CharField(max_length=4,choices=PRIORITY_CHOICES, default='low')
	name = models.CharField(max_length=256)
	description = models.CharField(max_length=1028)
	created = models.DateTimeField(auto_now=True)
	closed = models.DateTimeField(blank=True, null=True)
	slug =  models.SlugField(unique=True)

	class Meta:
		verbose_name_plural = "tickets"

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Ticket, self).save(*args, **kwargs)
