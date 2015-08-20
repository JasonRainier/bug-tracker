# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20150628_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Team',
            field=models.ForeignKey(to='main.Team', blank=True),
            preserve_default=True,
        ),
    ]
