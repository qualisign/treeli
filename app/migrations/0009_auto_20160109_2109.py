# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160109_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trunk',
            name='created_by',
            field=models.ForeignKey(to='app.User', null=True),
        ),
    ]
