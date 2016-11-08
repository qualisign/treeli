# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_leaf_learned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaf',
            name='reminders',
            field=models.IntegerField(default=1),
        ),
    ]
