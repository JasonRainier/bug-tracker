# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20150424_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Category',
            field=models.ForeignKey(to='main.Category'),
            preserve_default=True,
        ),
    ]
