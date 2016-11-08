# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20160115_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch_circle',
            name='trunk_circle',
        ),
        migrations.RemoveField(
            model_name='leaf_circle',
            name='twig_circle',
        ),
        migrations.DeleteModel(
            name='Menu_Circle',
        ),
        migrations.RemoveField(
            model_name='twig_circle',
            name='branch_circle',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='branch_circle',
        ),
        migrations.RemoveField(
            model_name='leaf',
            name='leaf_circle',
        ),
        migrations.RemoveField(
            model_name='twig',
            name='twig_circle',
        ),
        migrations.AlterField(
            model_name='branch',
            name='base_x',
            field=models.IntegerField(default=440),
        ),
        migrations.AlterField(
            model_name='branch',
            name='trunk',
            field=models.ForeignKey(default=None, to='app.Trunk', null=True),
        ),
        migrations.AlterField(
            model_name='trunk',
            name='base_x',
            field=models.IntegerField(default=320),
        ),
        migrations.AlterField(
            model_name='trunk',
            name='base_y',
            field=models.IntegerField(default=640),
        ),
        migrations.AlterField(
            model_name='trunk',
            name='tip_x',
            field=models.IntegerField(default=320),
        ),
        migrations.AlterField(
            model_name='trunk',
            name='tip_y',
            field=models.IntegerField(default=440),
        ),
        migrations.DeleteModel(
            name='Branch_Circle',
        ),
        migrations.DeleteModel(
            name='Leaf_Circle',
        ),
        migrations.DeleteModel(
            name='Trunk_Circle',
        ),
        migrations.DeleteModel(
            name='Twig_Circle',
        ),
    ]
