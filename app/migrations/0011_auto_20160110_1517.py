# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20160110_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trunk',
            name='created_by',
            field=models.ForeignKey(default=None, to='app.User'),
        ),
    ]
