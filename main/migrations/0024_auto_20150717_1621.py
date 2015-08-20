# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '__first__'),
        ('main', '0023_auto_20150628_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketComment',
            fields=[
                ('comment_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='comments.Comment')),
                ('text', models.CharField(max_length=1028)),
                ('created', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'comments',
            },
            bases=('comments.comment',),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
