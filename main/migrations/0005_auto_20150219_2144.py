# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_ticket_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='closed',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
