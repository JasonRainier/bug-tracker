# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='slug',
            field=models.SlugField(null=True),
            preserve_default=True,
        ),
    ]
