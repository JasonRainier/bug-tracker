# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150219_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='Team',
            field=models.ForeignKey(to='main.Team', null=True),
            preserve_default=True,
        ),
    ]
