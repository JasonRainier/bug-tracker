# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150327_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Category',
            field=models.ForeignKey(to='main.Category', blank=True),
            preserve_default=True,
        ),
    ]
