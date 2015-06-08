# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20150424_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='created',
            field=models.DateTimeField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
    ]
