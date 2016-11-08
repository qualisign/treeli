# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20160111_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch_Circle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('radius', models.IntegerField(default=98.88543819200001)),
                ('tip_x', models.IntegerField(default=0)),
                ('tip_y', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Leaf_Circle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('radius', models.IntegerField(default=37.77087639081845)),
                ('center_x', models.IntegerField(default=0)),
                ('center_y', models.IntegerField(default=0)),
                ('tip_x', models.IntegerField(default=0)),
                ('tip_y', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Menu_Circle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('radius', models.IntegerField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trunk_Circle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('radius', models.IntegerField(default=320)),
            ],
        ),
        migrations.CreateModel(
            name='Twig_Circle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('radius', models.IntegerField(default=61.11456179014908)),
                ('tip_x', models.IntegerField(default=0)),
                ('tip_y', models.IntegerField(default=0)),
                ('branch_circle', models.ForeignKey(to='app.Branch_Circle', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='trunk',
            name='base_x',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='leaf_circle',
            name='twig_circle',
            field=models.ForeignKey(to='app.Twig_Circle'),
        ),
        migrations.AddField(
            model_name='branch_circle',
            name='trunk_circle',
            field=models.ForeignKey(to='app.Trunk_Circle', null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='branch_circle',
            field=models.ForeignKey(to='app.Branch_Circle', null=True),
        ),
        migrations.AddField(
            model_name='leaf',
            name='leaf_circle',
            field=models.ForeignKey(to='app.Leaf_Circle', null=True),
        ),
        migrations.AddField(
            model_name='twig',
            name='twig_cirlce',
            field=models.ForeignKey(to='app.Twig_Circle', null=True),
        ),
    ]
