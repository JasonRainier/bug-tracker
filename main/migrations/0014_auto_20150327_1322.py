# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150327_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Category',
            field=models.ForeignKey(blank=True, to='main.Category', null=True),
            preserve_default=True,
        ),
    ]
