# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_twig_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tree',
            name='created_by',
        ),
        migrations.AddField(
            model_name='tree',
            name='category',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tree',
            name='saved_by',
            field=models.ManyToManyField(to='app.User'),
        ),
        migrations.AddField(
            model_name='trunk',
            name='created_by',
            field=models.ForeignKey(default=None, to='app.User'),
        ),
        migrations.AddField(
            model_name='trunk',
            name='language',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tree',
            name='sorted_twigs',
            field=models.ForeignKey(default=None, to='app.Twig'),
        ),
    ]
