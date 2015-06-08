# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150219_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='Comment',
        ),
    ]
