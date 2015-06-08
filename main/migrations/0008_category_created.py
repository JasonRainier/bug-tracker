# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_ticket_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 20, 17, 44, 48, 558000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
