# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20160201_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaf',
            name='height',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='leaf',
            name='width',
            field=models.IntegerField(default=2),
        ),
    ]
