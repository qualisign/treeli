# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160106_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='twig',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
