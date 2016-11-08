# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20160130_0856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tree',
            name='sorted_twigs',
        ),
        migrations.AddField(
            model_name='twig',
            name='tree',
            field=models.ForeignKey(to='app.Tree', null=True),
        ),
    ]
