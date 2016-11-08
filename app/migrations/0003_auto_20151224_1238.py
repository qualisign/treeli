# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151223_0751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tree',
            name='trunk',
        ),
        migrations.AddField(
            model_name='trunk',
            name='tree',
            field=models.OneToOneField(null=True, default=None, to='app.Tree'),
        ),
        migrations.AddField(
            model_name='twig',
            name='branch',
            field=models.ForeignKey(to='app.Branch', null=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='trunk',
            field=models.ForeignKey(to='app.Trunk', null=True),
        ),
        migrations.AlterField(
            model_name='leaf',
            name='twigs',
            field=models.ManyToManyField(to='app.Twig', null=True),
        ),
        migrations.AlterField(
            model_name='tree',
            name='created_by',
            field=models.ForeignKey(to='app.User', null=True),
        ),
        migrations.AlterField(
            model_name='tree',
            name='sorted_twigs',
            field=models.ForeignKey(to='app.Twig', null=True),
        ),
    ]
