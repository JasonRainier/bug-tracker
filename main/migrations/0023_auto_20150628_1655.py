# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20150628_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Team',
            field=models.ForeignKey(blank=True, to='main.Team', null=True),
            preserve_default=True,
        ),
    ]
