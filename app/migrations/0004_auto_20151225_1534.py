# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151224_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='base_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='branch',
            name='base_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='branch',
            name='drawing',
            field=models.CharField(default=b'blank', max_length=8),
        ),
        migrations.AddField(
            model_name='branch',
            name='tip_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='branch',
            name='tip_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='leaf',
            name='base_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='leaf',
            name='base_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='leaf',
            name='drawing',
            field=models.CharField(default=b'blank', max_length=8),
        ),
        migrations.AddField(
            model_name='leaf',
            name='tip_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='leaf',
            name='tip_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trunk',
            name='base_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trunk',
            name='base_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trunk',
            name='drawing',
            field=models.CharField(default=b'blank', max_length=8),
        ),
        migrations.AddField(
            model_name='trunk',
            name='tip_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trunk',
            name='tip_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='twig',
            name='base_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='twig',
            name='base_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='twig',
            name='drawing',
            field=models.CharField(default=b'blank', max_length=8),
        ),
        migrations.AddField(
            model_name='twig',
            name='tip_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='twig',
            name='tip_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaf',
            name='twigs',
            field=models.ManyToManyField(to='app.Twig'),
        ),
    ]
