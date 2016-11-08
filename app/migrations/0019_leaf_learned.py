# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20160131_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaf',
            name='learned',
            field=models.BooleanField(default=False),
        ),
    ]
