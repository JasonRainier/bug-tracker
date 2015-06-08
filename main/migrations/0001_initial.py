# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=1028)),
                ('created', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('role', models.CharField(max_length=128)),
                ('created', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'teams',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reporter', models.CharField(max_length=128)),
                ('priority', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1028)),
                ('created', models.DateField()),
                ('closed', models.DateField()),
                ('Category', models.ForeignKey(to='main.Category')),
                ('Comment', models.ForeignKey(to='main.Comment')),
            ],
            options={
                'verbose_name_plural': 'tickets',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('created', models.DateField()),
                ('Team', models.ForeignKey(to='main.Team')),
            ],
            options={
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ticket',
            name='Reporter',
            field=models.ForeignKey(to='main.User'),
            preserve_default=True,
        ),
    ]
