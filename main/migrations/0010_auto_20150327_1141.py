# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150327_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Team',
            field=models.ForeignKey(blank=True, to='main.Team', null=True),
            preserve_default=True,
        ),
    ]
