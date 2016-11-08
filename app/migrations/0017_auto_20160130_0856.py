# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20160128_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trunk',
            name='tree',
        ),
        migrations.AddField(
            model_name='tree',
            name='trunk',
            field=models.OneToOneField(default=None, to='app.Trunk'),
        ),
    ]
