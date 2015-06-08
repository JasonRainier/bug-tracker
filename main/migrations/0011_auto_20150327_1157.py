# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20150327_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
