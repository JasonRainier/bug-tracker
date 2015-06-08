# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_ticket_reporter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Comment',
            field=models.ForeignKey(to='main.Comment', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='closed',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
    ]
