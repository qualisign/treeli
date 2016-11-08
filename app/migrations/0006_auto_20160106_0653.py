# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20151229_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaf',
            name='reminders',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tree',
            name='twigs_learned',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='twig',
            name='misses',
            field=models.ManyToManyField(to='app.Leaf'),
        ),
    ]
