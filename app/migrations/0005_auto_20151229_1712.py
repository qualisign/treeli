# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20151225_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaf',
            old_name='base_x',
            new_name='center_x',
        ),
        migrations.RenameField(
            model_name='leaf',
            old_name='base_y',
            new_name='center_y',
        ),
        migrations.RenameField(
            model_name='leaf',
            old_name='tip_x',
            new_name='height',
        ),
        migrations.RenameField(
            model_name='leaf',
            old_name='tip_y',
            new_name='rotate',
        ),
        migrations.AddField(
            model_name='leaf',
            name='width',
            field=models.IntegerField(default=0),
        ),
    ]
