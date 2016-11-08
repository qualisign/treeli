# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20160110_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trunk',
            name='created_by',
            field=models.ForeignKey(default=None, to='app.User', null=True),
        ),
    ]
